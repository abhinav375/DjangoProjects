from django.contrib import admin
from . import models

# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display=['name','color','taste','price']
admin.site.register(models.Beer,BeerAdmin)