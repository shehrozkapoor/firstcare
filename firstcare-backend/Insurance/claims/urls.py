from django.urls import path,include



urlpatterns = [
    path('api/',include('Insurance.claims.api.urls'))
]