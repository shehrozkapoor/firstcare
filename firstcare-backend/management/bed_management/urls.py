from django.urls import path,include



urlpatterns = [
    path('api/',include('management.bed_management.api.urls'))
]