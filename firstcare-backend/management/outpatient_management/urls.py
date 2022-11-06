from django.urls import path,include




urlpatterns = [
    path('clinic/',include('management.outpatient_management.clinic_management.urls'))
]