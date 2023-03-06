from . import views
from django.urls import path

urlpatterns = [
    path('',views.qrGenerator_view.as_view(), name='qrGenerator_view')
]