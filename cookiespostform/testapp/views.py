from django.shortcuts import render
from . import forms

# Create your views here.
'''COOKIES CODE'''
def index(request):
    form=forms.studentRegustration()
    response=render(request,'testapp/wish.html',{'form':form})
    if request.method=='POST':
        print('inside post')
        form=forms.studentRegustration(request.POST)
        if(form.is_valid()):
          print("inside 2nd post")
          #name=request.POST['name']
          #roll_no=request.POST['roll_No']
          name=form.cleaned_data['name']
          roll_no=form.cleaned_data['roll_No']
          response.set_cookie('name',name)
          response.set_cookie('roll_no',roll_no)
          print(name,roll_no)
    return response

    
'''SESSION CODE'''
'''def index(request):
    form=forms.studentRegustration()
    
    if request.method=='POST':
        print('inside post')
        form=forms.studentRegustration(request.POST)
        if(form.is_valid()):
          print("inside 2nd post")
          #name=request.POST['name']
          #roll_no=request.POST['roll_No']
          name=form.cleaned_data['name']
          roll_no=form.cleaned_data['roll_No']
          request.session['name']=name
          request.session['roll_no']=roll_no
          print(name,roll_no)
    return render(request,'testapp/wish.html',{'form':form})'''

def show(request):
    return render(request,'testapp/index.html')