from django.contrib import admin
from testapp.models import Madam
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename','esal','eaddr','etitle','edesignation','ephonenumber']
admin.site.register(Madam,EmployeeAdmin)
    

