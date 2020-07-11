from django import forms

class StudentForms(forms.Form):
    name=forms.CharField()
    college=forms.CharField()
    feedback=forms.CharField(widget=forms.Textarea())
