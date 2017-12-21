from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, RedirectView
from .models import SubjectName, OutputDirectory



# Create your views here.


class HomeView(TemplateView):
    template_name = 'base.html'


class BIDSView(FormView):
    template_name = 'datapage.html'
    form_class = BIDSForm
    
    def form_valid(self, form)
        form.bids_conversion()
    return super().form_valid(form)   
# pattern_name = 'data'
    
   # def get_redirect_url(self, *args, **kwargs):
     #   response = HttpResponseRedirect("data/")

    #    return response 

