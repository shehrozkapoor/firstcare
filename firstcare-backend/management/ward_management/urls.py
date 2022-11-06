from django.urls import path,include

urlpatterns = [
    path('api/',include('management.ward_management.api.urls')),
]