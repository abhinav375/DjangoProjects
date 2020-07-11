from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request,'testapp/index.html')

def submitform(request):
    if request.method=='GET':
        print("r u okay123")
        form=forms.studentForm()
    if request.method=='POST':
        print("r u okaypost")
        form=forms.studentForm(request.POST)
        print("r u okay")
        if form.is_valid():
           print("inside valis")
           form.save(commit=True)
           return index(request)
    return render(request,'testapp/addform.html',{'form':form})


def showform(request):
    model=models.Student.objects.all()
    return render(request,'testapp/showform.html',{'model':model})
    