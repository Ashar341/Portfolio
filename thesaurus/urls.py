from . import views
from django.urls import path

urlpatterns = [
    path('',views.thesaurus_view, name='thesaurus_view')
]