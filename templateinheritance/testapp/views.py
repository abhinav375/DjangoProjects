from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/base.html')
def sports(request):
    return render(request,'testapp/sports.html')
