from django.urls import path,include



urlpatterns = [
    path('api/',include('management.schedule_management.api.urls'))
]