from django.contrib import admin
from .models import *

admin.site.register(AppointmentType)
admin.site.register(ProviderAvail)
admin.site.register(Appointment)
admin.site.register(Slot)