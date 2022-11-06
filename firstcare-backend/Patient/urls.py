from django.urls import path,include


urlpatterns = [
    path('api/',include('Patient.api.urls')),

]
