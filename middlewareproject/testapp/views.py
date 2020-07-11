from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
 print("Now in view")
 #print(10/0)
 return HttpResponse("<h1>Welcome to Middleware Demo.See console log to verify whether middleware called or not")