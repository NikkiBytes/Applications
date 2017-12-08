from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from .models import SubjectName, OutputDirectory

def index(request):
    return HttpResponse("hello I a here")


# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'

class OsirixView(RedirectView):
    subject = SubjectName
    output_dir = OutputDirectory
    template_name = 'osirixpage.html'
   


class BidsView(TemplateView):
    template_name = 'bidspage.html'
