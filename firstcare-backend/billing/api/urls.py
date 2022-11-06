from django.urls import path
from .views import *



urlpatterns = [
    path('paymenttype/',payment_type,name="payment_type"),
    path('paymentmethod/',payment_method,name="payment_method"),
    path('payment/',payment,name="payment"),
    path('paymentprofile/',payment_profile,name="payment_profile"),
    path('onsetdatatype/',onset_data_type,name="onset_data_type"),
    path('otherdatatype/',other_data_type,name="other_data_type"),
    path('hcfabox/',hcfa_box,name="hcfa_box"),
    path('icd10/',icd_10,name="icd_10"),
    path('icd9/',icd_9,name="icd_9"),
    path('cptitem/',cpt_item,name="cpt_item"),
    path('cptcode/',cpt_code,name="cpt_code"),
    path('hcpcs/',hcpcs,name="hcpcs"),
    path('hcpcscode/',hcpcs_code,name="hcpcs_code"),
    path('billing/',billing,name="billing"),
]