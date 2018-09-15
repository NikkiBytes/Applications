from .models import BIDSModel
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from myapp.forms import BIDSForm
from django.urls import reverse_lazy
# Create your views here.


class HomeView(TemplateView):
    template_name = 'base.html'

class FeatView(TemplateView):
    template_name = "feat_analysis_view.html"

class fMRIView(TemplateView):
    template_name = 'fmriprep_view.html'

class BIDSView(TemplateView):
    template_name = 'BIDS_view.html'
   # form_class = BIDSForm
   # success_url = reverse_lazy('bidsconversion')
    model = BIDSModel
    def post(self, request):
        sub = request.POST['subject_name']
        out_dir = request.POST['output_directory']
        in_dir =  request.POST['input_directory']
        password =  request.POST['pass']
        hpc_address =  request.POST['hpc_address']
        dicom_path =  request.POST['dicom_path']
        return render(request, self.template_name, { 'sub': sub, 'out': out_dir, 'in': in_dir })


'''   def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form} )
'''
class OsirixView(FormView):
     template_name = 'osirixview.html'
     form_class = BIDSForm
# pattern_name = 'data'

   # def get_redirect_url(self, *args, **kwargs):
     #   response = HttpResponseRedirect("data/")

    #    return response
