from django.urls import path,include


urlpatterns =[

    path('api/',include('management.outpatient_management.clinic_management.api.urls'))
]