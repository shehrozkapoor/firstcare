from django.urls import path,include
from .views import *


urlpatterns = [
    path('generateAccessionNumber/',generateAccessionNumber,name="generateAccessionNumber"),
    path('sampletype/',sample_type,name="sample_type"),
    path('availabletests/',available_tests,name="available_tests"),
    path('sample/',sample,name="sample"),
    path('unitofmeasure/',unit_of_measure,name="unit_of_measure"),
    path('refusalreason/',refusal_reason,name="refusal_reason"),
    path('nonconformity/',non_conformity,name="non_conformity"),
]