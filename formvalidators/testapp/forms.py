from django import forms
from django.core import validators

def validate_po(value):
   if value<1000:
      raise forms.ValidationError("Rollno must be greater than 1000")
   
class feedbackForm(forms.Form):
    name = forms.CharField()
    roll_no = forms.IntegerField(validators=[validate_po])
    address = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(3)])

    def clean_name(self):
       print("inside clean")
       name1 = self.cleaned_data['name']
       if len(name1) < 6:
          print("HEllo")
          raise forms.ValidationError("Name should be greater than 6")
       return name1
    def clean(self):
       cleaned_data=super().clean()
       if(len(cleaned_data['address'])<5):
          raise forms.ValidationError("should be 7")
