import imp
from django.urls import path,include

urlpatterns = [
    path('api/',include('management.doctor_management.api.urls')),
]