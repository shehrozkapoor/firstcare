from pydoc import doc
from django.urls import path
from .views import *

urlpatterns = [

    path('department/',department,name="department"),
    path('doctor/',doctor,name="doctor")
    
]