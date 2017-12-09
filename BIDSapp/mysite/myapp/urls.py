from django.urls import path
from . import views
from myapp.views import HomeView, OsirixView, BidsView


urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('/osirix/', OsirixView.as_view(), name="osirix"),
    path('bidsconverter/', BidsView.as_view(), name="bids"),
]
