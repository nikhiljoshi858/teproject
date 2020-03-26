from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

class PersonalDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.DecimalField(max_digits=10, decimal_places=0)
    gender = models.CharField(max_length=50, choices=GENDER)
    def __str__(self):
        return self.email



class DiseaseCause(models.Model):
    name = models.CharField(max_length=500)
    cause = models.CharField(max_length=1000)
    def __str__(self):
        return self.cause


class DiseaseSolution(models.Model):
    name = models.CharField(max_length=500)
    solution = models.CharField(max_length=1000)
    def __str__(self):
        return self.solution

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    dname = models.CharField(max_length=50)

    def __str__(self):
        return self.dname


class LandDetails(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=10, decimal_places=3)
    

class DiseaseImage(models.Model):
    image = models.ImageField(upload_to='images/')