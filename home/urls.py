from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_view.as_view(), name='home_view')
]