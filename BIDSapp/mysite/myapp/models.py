
from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.

class BIDSModel(models.Model):
    sub_name = models.CharField(max_length=100)
    out_dir = models.CharField(max_length=200)
    in_dir = models.CharField(max_length=200)
    multi_sess_pass = models.BooleanField()

    def __str__(self):
        return self.sub_name

class OsirixModel(models.Model):
    sub_name = models.CharField(max_length=100)
    out_dir = models.CharField(max_length=200)
    #will have to add password/username

