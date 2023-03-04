from django.shortcuts import render
from django.views import generic

# Create your views here.

class home_view(generic.TemplateView):
    template_name = 'home.html'