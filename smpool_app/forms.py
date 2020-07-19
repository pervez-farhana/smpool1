from django import forms 
from smpool_app.models import content_service
from smpool_app.models import website_content_info

class serviceform(forms.ModelForm):
    class Meta:
        model= content_service
        fields = ['service_desc','service_cost']

class contentform(forms.ModelForm):
    class Meta:
        model= website_content_info
        fields = ['body_text','body_pos']