from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.core import serializers
import cv2
import numpy as np
from django.core.files.storage import default_storage
from django.conf import settings
from tensorflow.keras.models import load_model
from sklearn.tree import DecisionTreeClassifier
import joblib
from datetime import date
# Create your views here.

def homepage(request):
    return render(request=request, template_name='crop/home.html')


def register(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			confpass = form.cleaned_data.get('confirm_password')
			if confpass != password:
				messages.error(request, "Passwords don't match")
			user = User.objects.create_user(username=username,password=password)
			user.save()
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
			else:
				messages.error(request, 'Invalid Credentials')
			return redirect("crop:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
 

	form = UserForm()
	return render(request,
				  "crop/register.html",
				  context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("crop:homepage")

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("crop:homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid Credentials")

	form = LoginForm()
	return render(request,
				  "crop/login.html",
				  {"form":form})


@login_required()
def crop_predict_personal(request):
	if request.method=='POST':
		form = PersonalDetailsForm(request.POST)
		if form.is_valid():
			fn = form.cleaned_data.get('firstname')
			ln = form.cleaned_data.get('lastname')
			email = form.cleaned_data.get('email')
			contact = form.cleaned_data.get('contact')
			gender = form.cleaned_data.get('gender')
			pd = PersonalDetails(user_id=request.user,firstname=fn,lastname=ln,email=email,contact=contact,gender=gender)
			pd.save()
			return redirect('crop:crop_predict_land')
	
	form = PersonalDetailsForm()
	return render(request, 'crop/personal_details.html',context={'form':form})
	

@login_required()
def crop_predict_land(request):
	if request.method == "POST":
		# crop = request.POST["soil"]
		model = joblib.load(settings.MEDIA_ROOT+"/model.h5")
		hum = request.POST["hum"]
		rain = request.POST["rain"]
		temp = request.POST["temp"]
		today = date.today()
		today = today.month
		if today<=3:
			quat = 1
		elif today<=6:
			quat = 2
		elif today<=9:
			quat = 3
		elif today<=12:
			quat = 4
		ls = [quat,rain,temp,hum]+list(request.POST["soil"])
		ls[-1] = int(ls[-1])
		ls[-2] = int(ls[-2])
		ls[-3] = int(ls[-3])
		# return HttpResponse(str(ls))
		result = model.predict([ls])
		prob = model.predict_proba([ls])
		result = int(result)
		if result==0:
			crop = "Tomato"
		elif result==1:
			crop = "Potato"
		elif result==2:
			crop = "Soyabean"
		elif result==3:
			crop = "Strawberry"
		elif result==4:
			crop = "Bell Pepper"
		elif result==5:
			crop = "Raspberry"
		elif result==6:
			crop = "Peach"
		elif result==7:
			crop = "Grapes"
		elif result==8:
			crop = "Orange"
		elif result==9:
			crop = "Corn"
		elif result==10:
			crop = "Cherry"
		prob = max(prob[0]) * 100
		return render(request,"crop/crop_predict.html",{"crop":crop,"prob":prob})
	states = State.objects.all()
	return render(request, 'crop/land_details.html', {"states": states})


@login_required()
def crop_predict(request):
	return render(request,'crop/crop_predict.html')


@login_required()
def disease_predict_upload(request):
    # return HttpResponse('Disease Prediction')
	if request.method=='POST':
		form = DiseaseImageForm(request.POST,request.FILES)
		if form.is_valid():
			img = request.FILES['image']
			file_name = default_storage.save(img.name, img)
			img = cv2.imread(settings.MEDIA_ROOT+"/"+file_name)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			# image = tf.cast(img, tf.float32)
			img3 = np.asarray([img])
			# return HttpResponse(img3.shape)
			loaded_model = load_model(settings.MEDIA_ROOT+"/disease_model_final.h5")
			predicted = loaded_model.predict_classes(img3)
			prob = max(loaded_model.predict_proba(img3)[0]) * 100
			# return HttpResponse(prob)
			mapping = {'Apple___Apple_scab': 0,
			'Apple___Black_rot': 1,
			'Apple___Cedar_apple_rust': 2,
			'Apple___healthy': 3,
			'Blueberry___healthy': 4,
			'Cherry_(including_sour)___Powdery_mildew': 5,
			'Cherry_(including_sour)___healthy': 6,
			'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 7,
			'Corn_(maize)___Common_rust_': 8,
			'Corn_(maize)___Northern_Leaf_Blight': 9,
			'Corn_(maize)___healthy': 10,
			'Grape___Black_rot': 11,
			'Grape___Esca_(Black_Measles)': 12,
			'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 13,
			'Grape___healthy': 14,
			'Orange___Haunglongbing_(Citrus_greening)': 15,
			'Peach___Bacterial_spot': 16,
			'Peach___healthy': 17,
			'Pepper,_bell___Bacterial_spot': 18,
			'Pepper,_bell___healthy': 19,
			'Potato___Early_blight': 20,
			'Potato___Late_blight': 21,
			'Potato___healthy': 22,
			'Raspberry___healthy': 23,
			'Soybean___healthy': 24,
			'Squash___Powdery_mildew': 25,
			'Strawberry___Leaf_scorch': 26,
			'Strawberry___healthy': 27,
			'Tomato___Bacterial_spot': 28,
			'Tomato___Early_blight': 29,
			'Tomato___Late_blight': 30,
			'Tomato___Leaf_Mold': 31,
			'Tomato___Septoria_leaf_spot': 32,
			'Tomato___Spider_mites Two-spotted_spider_mite': 33,
			'Tomato___Target_Spot': 34,
			'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 35,
			'Tomato___Tomato_mosaic_virus': 36,
			'Tomato___healthy': 37}
			predict = predicted[0]
			st = ""
			for key,value in mapping.items():
				if value == predict:
					st = key
			crop,disease = st.split("___")
			return render(request, "crop/disease_predict.html", context={'file_name':file_name,"st":st,"crop":crop,"disease":disease,'prob':prob})
		else:
			return HttpResponse("error")
	form = DiseaseImageForm()
	return render(request, 'crop/disease_image.html', context={'form':form})


@login_required()
def disease_predict(request):
	return render(request, 'crop/disease_predict.html')

def disease_solutions(request,st):
	disease = st.split('___')[1]
	causes = DiseaseCause.objects.filter(name=st)
	solutions = DiseaseSolution.objects.filter(name=st)
	return render(request, 'crop/disease_solutions.html', context={'disease':disease,'causes':causes, 'solutions':solutions})




# get district for ajax
def get_dist(request):
	dists = District.objects.filter(state=request.GET['state'])
	dists = serializers.serialize("json",dists)
	# crop = dists
	return JsonResponse(dists, safe=False)