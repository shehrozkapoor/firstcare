from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/',room,name="room"),
    path('wards/',ward,name="ward"),
    path('hospital/',hospital,name="hospital"),
]