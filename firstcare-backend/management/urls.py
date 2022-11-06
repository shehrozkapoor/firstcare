from django.urls import path,include




urlpatterns = [
    
    path('ward/',include('management.ward_management.urls')),
    path('bed/',include('management.bed_management.urls')),
    path('outpatient/',include('management.outpatient_management.urls')),
    path('doctor/',include('management.doctor_management.urls')),
    path('schedule/',include('management.schedule_management.urls'))

]