from django.urls import path
from .views import *


urlpatterns = [
    path('contactinformation/',contactInformation,name="contactinformation"),
    path('patient/',patient,name="patient"),
    path('getSpecificPatient/',getSpecificPatient,name="getSpecificPatient"),
    path('patientList/',patient_list,name="patient_list"),
    path('searchpatient/',searchPatient,name="searchPatient"),
    
    path('patientinsurance/',patientInsurance,name="patientInsurance"),
    
    path('patientsearchnsurance/',getSearchInsurancePatient,name="getSearchInsurancePatient"),
]