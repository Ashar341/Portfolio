from . import views
from django.urls import path

urlpatterns = [
    path('',views.toDoList.as_view(), name='toDoList')
]