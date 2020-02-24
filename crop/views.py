from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from .forms import NewUserForm
# Create your views here.
def homepage(request):
    return render(request=request, template_name='crop/home.html')
    # return HttpResponse('HTTP')