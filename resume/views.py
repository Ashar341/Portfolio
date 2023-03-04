from django.shortcuts import render
from django.views import generic

# Create your views here.

class resume_view (generic.TemplateView):
    template_name = 'resume.html'
