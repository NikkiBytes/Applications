from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello I a here")

from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'
