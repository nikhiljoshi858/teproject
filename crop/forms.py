from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

STATE = (
    ('Jharkhand','Jharkhand'), ('Uttarakhand','Uttarakhand'), ('Karnataka', 'Karnataka'),('Madhya Pradesh','Madhya Pradesh'),
    ('Sikkim','Sikkim'), ('Haryana','Haryana'),('Bihar','Bihar'), ('Odisha','Odisha'), ('Uttar Pradesh','Uttar Pradesh'),
    ('Maharashtra','Maharashtra'), ('Chandigarh','Chandigarh'), ('Delhi','Delhi'), ('Jammu And Kashmir','Jammu And Kashmir'),
    ('Tamil Nadu','Tamil Nadu'), ('Assam','Assam'), ('Rajasthan','Rajasthan'), ('Punjab','Punjab'), ('Meghalaya','Meghalaya'),
    ('Himachal Pradesh','Himachal Pradesh'), ('Mizoram','Mizoram'), ('Gujarat','Gujarat'), ('Nagaland','Nagaland'),('Chhattisgarh','Chhattisgarh'), 
    ('Lakshadweep','Lakshadweep'), ('Kerala','Kerala'), ('West Bengal','West Bengal'),('Andaman & Nicobar Islands','Andaman & Nicobar Islands'), 
    ('Arunachal Pradesh','Arunachal Pradesh'), ('Andhra Pradesh','Andhra Pradesh'),('Manipur','Manipur'), ('Goa','Goa'), 
    ('Daman & Diu','Daman & Diu'), ('Tripura','Tripura'), ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),('Pondicherry','Pondicherry'), 
    ('Telangana','Telangana')
)


class UserForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)
    confirm_password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)

    class Meta:
        model = User
        fields = ('Username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)


class PersonalDetailsForm(forms.Form):
    firstname = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    lastname = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    email = forms.CharField(label='Email Address', required=True, widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
    contact = forms.CharField(label='Contact Number', required=True, widget=forms.TextInput(attrs={'class':'form-control','type':'number'}))
    gender = forms.ChoiceField(required=True, choices=GENDER)


# class LandDetails(forms.Form):

class DiseaseImageForm(forms.Form):
    image = forms.ImageField(required=True)



# class CropPredictionForm(forms.Form):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                