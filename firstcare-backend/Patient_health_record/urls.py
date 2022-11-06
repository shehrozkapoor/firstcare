from django.urls import path,include
from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('api/',include('Patient_health_record.api.urls')),
]