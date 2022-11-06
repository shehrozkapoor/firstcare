from django.contrib import admin
from .models import Product,HealthFacilities,ServiceCategory


admin.site.register(Product)
admin.site.register(HealthFacilities)
admin.site.register(ServiceCategory)