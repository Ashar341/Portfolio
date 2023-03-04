from . import views
from django.urls import path

urlpatterns = [
    path('',views.resume_view.as_view(), name='resume_view')
]