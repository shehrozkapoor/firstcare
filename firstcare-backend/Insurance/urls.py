from django.urls import path,include



urlpatterns = [
    path('api/',include('Insurance.api.urls')),
    path('administration/',include('Insurance.insurance_administration.urls')),
    path('claims/',include('Insurance.claims.urls'))
]