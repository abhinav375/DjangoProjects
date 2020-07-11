from django import forms

class studentRegustration(forms.Form):
    name=forms.CharField()
    roll_No=forms.IntegerField()