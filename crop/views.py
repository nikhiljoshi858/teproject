from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
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


def crop_predict(request):
    return HttpResponse('Crop Prediction')

def disease_predict(request):
    return HttpResponse('Disease Prediction')
