from django.urls import path
from .views import *


urlpatterns = [
    path('insurancecompany/',insurance_company,name="insurance_company"),
    path('insuranceplantype/',insurance_plan_type,name="insurance_plan_type"),
    path('hcfa/',hcfa,name="hcfa"),
    path('subscriber/',subscriber,name="subscriber"),
    path('insurance/',insurance,name="insurance"),

    path('billingsummary/',billingSummary,name="billingSummary"),
    path('liveclaimfields/',live_claim_fields,name="live_claim_fields"),
    path('batchStatusChange/',batchStatusChange,name="batchStatusChange"),
    path('patientpayments/',patient_payments,name="patient_payments"),
    path('patientpaymentssubdata/',patient_payments_sub_data,name="patient_payments_sub_data"),
    path('exportPatientPaymentToCsv/',exportPatientPaymentToCsv,name="exportPatientPaymentToCsv"),
    
    path('updateeligibility/',updateEligibility,name="updateeligibility"),
]