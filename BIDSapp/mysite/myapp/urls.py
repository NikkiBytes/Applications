from django.urls import path
from . import views
from myapp.views import HomeView, DataView, BidsView


urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path("data/", DataView.as_view(), name="data"),
]
