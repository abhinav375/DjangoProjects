from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def displaytime(request):
    date=datetime.datetime.now()
    msg='<h1> Today date is'+str(date)+'</h1'
    return HttpResponse(msg)
    
