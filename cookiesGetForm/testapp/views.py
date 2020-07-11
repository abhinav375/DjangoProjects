from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    form=forms.studentRegustration()
    return render(request,'testapp/wish.html',{'form':form})
def show(request):
    name=request.GET['name']
    roll_no=request.GET['roll_No']
    return render(request,'testapp/index.html',{'name':name,'roll_no':roll_no})