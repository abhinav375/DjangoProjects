from django.shortcuts import render
from testapp.models import Madam

# Create your views here.
param=Madam.objects.all()
my_dict={'emp_list':param}
def showtemplate(request):
    return render(request,'testapp/wish.html',context=my_dict)