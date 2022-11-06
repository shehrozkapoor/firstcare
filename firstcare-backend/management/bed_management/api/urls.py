from django.urls import path,include
from .views import *


urlpatterns = [
    path('bedtags/',bed_tags,name="bed_tags"),
    path('bedtypes/',bed_type,name="bed_type"),
    path('bedlayouts/',bed_layout,name="bed_layout"),
]