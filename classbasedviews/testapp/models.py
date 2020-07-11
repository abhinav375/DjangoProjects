from django.db import models
from django.urls import reverse

# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=80)
    taste=models.CharField(max_length=80)
    color=models.CharField(max_length=80)
    price=models.IntegerField()
    
    def get_absolute_url(self):
    # return reverse('details',kwargs={'pk':self.pk})
      return reverse('home')
 