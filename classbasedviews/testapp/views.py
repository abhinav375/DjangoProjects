from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from . import models
# Create your views here.
class listview(ListView):
    model=models.Beer

class detailview(DetailView):
    model=models.Beer
    
class createview(CreateView):
    model=models.Beer
    fields='__all__'

class updateview(UpdateView):
    model=models.Beer
    fields='__all__'

class deleteview(DeleteView):
    model=models.Beer
    success_url=reverse_lazy('home')
    