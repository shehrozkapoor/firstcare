from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('claimservices/',claim_services,name="claim_services"),
    path('claimitems/',claim_items,name="claim_items"),
    path('claims/',claims,name="claims"),
    path('reviewclaims/',review_claims,name="review_claims"),
]