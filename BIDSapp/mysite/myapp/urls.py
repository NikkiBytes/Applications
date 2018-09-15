from django.urls import path
from . import views
from myapp.views import HomeView, BIDSView, fMRIView, FeatView

app_name= 'myapp'
urlpatterns = [
    path('',  HomeView.as_view(), name='index'),
    path('convertbids/', BIDSView.as_view(),  name="bids"),
    path('runfmriprep/', fMRIView.as_view(), name="fmriprep"),
    path('featureanalysis/', FeatView.as_view(), name="featanalysis"),
    #path('osirixscrape/', OsirixView.as_view(), name="osirix"),
    #path("data/", DataView.as_view()),
]
