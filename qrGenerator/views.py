from django.shortcuts import render
from django.views import generic

# Create your views here.

class qrGenerator_view (generic.TemplateView):
    template_name = 'qrGenerator.html'