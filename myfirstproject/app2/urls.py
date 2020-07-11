
from django.urls import path
from django.urls import include
from app2 import views

urlpatterns = [
   
   #path('welcome/',views.welcome),
    path('date/',views.displaytime),
    path('date1/',views.displaytime),
    path('date2/',views.displaytime),
    path('date3/',views.displaytime),

]
