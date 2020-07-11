from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

@login_required
def java(request):
    return render(request,'testapp/java.html')

@login_required
def python(request):
    return render(request,'testapp/python.html')

def logout(request):
    return render(request,'testapp/logout.html')

def signup(request):
    if request.method=='GET':
     form=forms.signup()
    if request.method=='POST':
        form=forms.signup(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
            
            
    return render(request,'testapp/signup.html',{'form':form})