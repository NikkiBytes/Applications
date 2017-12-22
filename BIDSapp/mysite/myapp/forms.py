
from django import forms
from django.forms import ModelForm 
from myapp.models import BIDSModel, OsirixModel 


class BIDSForm(ModelForm):
    class Meta: 
        model = BIDSModel 
        fields = ['sub_name', 'in_dir', 'out_dir', 'multi_sess_pass'] 

class OsirixForm(ModelForm):
    class Meta:
        model = OsirixModel 
        fields = ['sub_name', 'out_dir']

