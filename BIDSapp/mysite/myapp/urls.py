from django.urls import path
from . import views
from myapp.views import HomeView, BIDSView, OsirixView

app_name= 'myapp'
urlpatterns = [
    path('',  HomeView.as_view(), name='index'),
    path('bidsconversion/', BIDSView.as_view(),  name="bids"),
    path('osirixscrape/', OsirixView.as_view(), name="osirix"),
    #path("data/", DataView.as_view()),
]
