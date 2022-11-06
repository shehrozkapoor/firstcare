from django.urls import path,include



urlpatterns = [
    path('api/',include('Laboratory.api.urls')),
    path('administration/',include('Laboratory.administration.urls'))
]