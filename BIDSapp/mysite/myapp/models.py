from django.db import models
from django.urls import reverse

# Create your models here.


class SubjectName(models.Model):
    subject_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('bids-success')

class OutputDirectory(models.Model):
    output_directory = models.CharField(max_length=200)

    def __str__(self):
        return self.output_directory

