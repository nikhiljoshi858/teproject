from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)
    confirm_password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)

    class Meta:
        model = User
        fields = ('Username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'form-control','type':'password'}), required=True)