from django.shortcuts import render
from django.views import generic

# Create your views here.

class toDoList(generic.TemplateView):
    template_name = 'toDoList.html'