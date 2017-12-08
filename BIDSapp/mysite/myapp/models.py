from django.db import models

# Create your models here.

class SubjectName(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name

class OutputDirectory(models.Model):
    output_directory = models.CharField(max_length=200)

    def __str__(self):
        return self.output_directory

