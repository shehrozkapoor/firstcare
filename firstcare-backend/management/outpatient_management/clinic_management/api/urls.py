from django.urls import path
from .views import *


urlpatterns = [
    path('clinic/',clinic,name="clinic")
]