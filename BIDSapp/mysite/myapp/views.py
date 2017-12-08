from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello I a here")

# Create your views here.
