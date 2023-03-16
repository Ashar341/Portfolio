from django.shortcuts import render
from django.views import generic

# Create your views here.

class toDoList(generic.TemplateView):
    my_list = ["task1", "task2"]
    template_name = 'toDoList.html'