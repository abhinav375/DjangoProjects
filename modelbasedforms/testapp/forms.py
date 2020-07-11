from django import forms
from django.core import validators
from . import models

class studentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields='__all__'
    
        
    
    