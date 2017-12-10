from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, RedirectView
from .models import SubjectName, OutputDirectory



# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'

class DataView(RedirectView):
    subject = SubjectName
    output_dir = OutputDirectory
    template_name = 'datapage.html'
   # pattern_name = 'data'
    
   # def get_redirect_url(self, *args, **kwargs):
     #   response = HttpResponseRedirect("data/")

    #    return response 

