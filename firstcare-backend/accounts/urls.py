from django.urls import path,include
from .views import *


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('userType/',userType,name="userType"),
    path('getToken/',getToken,name="getToken"),
]
