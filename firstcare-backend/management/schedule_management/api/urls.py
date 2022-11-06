from django.urls import path
from .views import *

urlpatterns = [
    path('appointmenttype/',appointmentType,name="appointmenttype"),
    path('provideravail/',providerAvail,name="providerAvail"),
    path('appointment/',appointment,name="appointment"),
    path('findslots/',findSlots,name="findslots"),
]