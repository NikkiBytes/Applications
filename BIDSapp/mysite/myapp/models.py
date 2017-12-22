
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
'''class BIDSForm(ModelForm):
    class Meta: 
        model = BIDSModel 
        fields = ['sub_name', 'in_dir', 'out_dir', 'multi_sess_pass'] 

class OsirixForm(ModelForm):
    class Meta:
        model = OsirixModel 
        fields = ['sub_name', 'out_dir']
    

class SubjectName(models.Model):
    subject_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('bids-success')

class OutputDirectory(models.Model):
    output_directory = models.CharField(max_length=200)

    def __str__(self):
        return self.output_directory
'''
