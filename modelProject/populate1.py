import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelProject.settings')
import django
django.setup()
from testapp.models import Madam
from faker import Faker
from random import *
fakegen=Faker()
def genNumber():
    num=randint(7,9)
    num=''+str(num)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
     name=fakegen.name()
     sal=randint(0,9)*100*randint(0,8)*.5
     add=fakegen.address()
     title=fakegen.random_element(elements=('bca','mca','bsc','btech'))
     designation=fakegen.random_element(elements=('se','as','sse'))
     number=genNumber()
     phonenumber=genNumber()

     objectrecords=Madam.objects.get_or_create(ename=name,esal=sal,eaddr=add,etitle=title,edesignation=designation,ephonenumber=phonenumber)

populate(100)