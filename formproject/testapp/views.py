from django.shortcuts import render
from . import forms
# Create your views here.
def showforms(request):
    form=forms.StudentForms()
    sent=False
    if(request.method=='POST'):
        form1=forms.StudentForms(request.POST)
        if form1.is_valid():
            sent=True
            print('Name:',form1.  cleaned_data['name'])
            print('college:',form1.cleaned_data['college'])
            print('feedback:',form1.cleaned_data['feedback'])
            
    return render(request,'testapp/wish.html',{'form':form,'sent':sent})