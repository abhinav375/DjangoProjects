from django.shortcuts import render
import datetime
# Create your views here.

def tempview(request):
    date=datetime.datetime.now()
    my_dict={'dt':date}
    return render(request,'testapp/wish.html',context=my_dict)