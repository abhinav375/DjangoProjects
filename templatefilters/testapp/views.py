from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    inf=models.myinf.objects.all()
    return render(request,'testapp/index.html',{'inf':inf})