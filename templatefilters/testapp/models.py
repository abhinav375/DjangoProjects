from django.db import models

class myinf(models.Model):
    name=models.CharField(max_length=30)
    roll_no=models.IntegerField()
    address=models.CharField(max_length=30)
