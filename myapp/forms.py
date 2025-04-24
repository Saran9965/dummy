from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'service_type', 'description', 'address', 'contact_no']
