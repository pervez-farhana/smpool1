from django import forms 
from smpool_app.models import smservices

class serviceform(forms.ModelForm):
    class Meta:
        model= smservices
        fields = ['service_desc','service_cost']