from django.urls import path
from . import views
from myapp.views import HomeView, DataView

app_name= 'myapp'
urlpatterns = [
    path('',  HomeView.as_view(), name='index'),
    #path("data/", DataView.as_view()),
]
