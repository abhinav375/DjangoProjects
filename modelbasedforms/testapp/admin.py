from django.contrib import admin
from . import models
# Register your models here.
class adminStudent(admin.ModelAdmin):
    list_display=['name','roll_no','address']
admin.site.register(models.Student,adminStudent)
