from django.urls import path,include
from .views import *


urlpatterns = [
    path('api/',include('drchrono_insurance.api.urls')),
    path('',index,name="index")
]