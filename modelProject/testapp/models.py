from django.db import models

# Create your models here.


class Madam(models.Model):
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)
    etitle=models.CharField(max_length=30)
    edesignation=models.CharField(max_length=30)
    ephonenumber=models.IntegerField()
    