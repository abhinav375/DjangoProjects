from django.shortcuts import render
from . import forms
# Create your views here.

def displayform(request):
    sent=False
    name=''
    if request.method=='GET':
             form=forms.feedbackForm()
    if request.method=='POST':
        sent=True
        
        form=forms.feedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            print('Name:',name)
            roll_no=form.cleaned_data['roll_no']
            print("rooll_no:",roll_no)
            address=form.cleaned_data['address']
            print("address:",address)
            feedback=form.cleaned_data['feedback']
            print("feedback:",feedback)     
    return render(request,'testapp/wish.html',{'form':form,'name':name,'sent':sent})