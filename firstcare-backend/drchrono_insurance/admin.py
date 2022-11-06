from django.contrib import admin
from .models import *

admin.site.register(Insurance)
admin.site.register(InsuranceCompany)
admin.site.register(InsurancePlanType)
admin.site.register(HCFA)
admin.site.register(Subscriber)