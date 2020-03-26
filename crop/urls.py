"""teproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'crop'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    path('crop/personal/', views.crop_predict_personal, name='crop_predict'),
    path('crop/land/', views.crop_predict_land, name='crop_predict_land'),
    path('crop/predict/', views.crop_predict, name='crop_predict'),
    path('disease/upload', views.disease_predict_upload, name='disease_predict_upload'),
    path('disease/predict/', views.disease_predict, name='disease_predict'),
    path('disease/solutions/', views.disease_solutions, name='disease_solutions'),
    path('disease/solutions/<st>', views.disease_solutions, name='disease_solutions'),
    
    path("get_dist", views.get_dist,name="get_dist"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
