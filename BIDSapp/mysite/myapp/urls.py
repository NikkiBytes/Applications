from django.urls import path
from . import views
from myapp.views import HomeView, BIDSView

app_name= 'myapp'
urlpatterns = [
    path('',  HomeView.as_view(), name='index'),
    path('bids-success/', BIDSView.as_view(),  name="bids"),
    #path("data/", DataView.as_view()),
]
