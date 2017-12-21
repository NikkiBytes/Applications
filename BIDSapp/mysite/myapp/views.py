from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, RedirectView
from .models import SubjectName, OutputDirectory
from django.views.generic.edit import FormView
from myapp.forms import BIDSForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'base.html'


class BIDSView(FormView):
    template_name = 'datapage.html'
    form_class = BIDSForm
    
    def form_valid(self, form):
        form.bids_conversion()
        return super().form_valid(form)   

class OsirixView(FormView):
     template_name = 'osirixview.html'
     form_class = BIDSForm     
# pattern_name = 'data'
    
   # def get_redirect_url(self, *args, **kwargs):
     #   response = HttpResponseRedirect("data/")

    #    return response 

