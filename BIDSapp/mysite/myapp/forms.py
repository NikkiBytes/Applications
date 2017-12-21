
from django import forms

class BIDSForm(forms.Form):
    subject_name = forms.CharField()
    input_directory =  forms.CharField()
    output_directory = forms.CharField()
    
    multi_sess_boolean = forms.BooleanField()
    multi_sess_count = forms.IntegerField()
    multi_sess_name = forms.CharField()

    def bids_conversion(self):
        pass     
