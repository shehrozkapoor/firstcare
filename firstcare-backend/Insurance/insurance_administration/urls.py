from django.urls import path,include



urlpatterns = [
    path('api/',include('Insurance.insurance_administration.api.urls'))
]