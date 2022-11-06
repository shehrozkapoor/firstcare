from django.urls import path,include



urlpatterns = [
    path('api/',include('Laboratory.administration.api.urls'))
]