from unicodedata import name
from django.urls import path,include
from .views import *


urlpatterns = [
    path('insuranceuserpermissions/',insurance_user_permissions,name="insurance_user_permissions"),
    path('insuranceuserroles/',insurance_user_roles,name="insurance_user_roles"),
    path('insuranceuser/',insurance_user,name="insurance_user"),
    path('familytype/',family_type,name="family_type"),
    path('confirmationtype/',confirmation_type,name="confirmation_type"),
    path('family/',family,name="family"),
    path('relationship/',relation_ship,name="relation_ship"),
    path('profession/',profession,name="profession"),
    path('education/',education,name="education"),
    path('idtype/',id_type,name="id_type"),
    path('headinsuree/',head_insuree,name="head_insuree"),
    path('healthfacilitylevel/',health_facility_level,name="health_facility_level"),
    path('healthfacility/',health_facility,name="health_facility"),
    path('firstservicepoint/',first_service_point,name="first_service_point"),
    path('insurance/',insurance,name="insurance"),

    path('insuree/',insuree,name="insuree"),

    path('products/',products,name="products"),
    path('policydetails/',policy_details,name="policy_details"),
    path('deductable/',deductable,name="deductable"),
    path('remunerated/',remunerated,name="remunerated"),
    path('policiesvalues/',policies_values,name="policies_values"),
    path('policies/',policies,name="policies"),
    
    path('paymenttype/',payment_type,name="payment_type"),
    path('contributioncategory/',contribution_category,name="contribution_category"),
    path('contribution/',contribution,name="contribution"),
    
    path('legalform/',legal_form,name="legal_form"),
    path('activitycode/',activity_code,name="activity_code"),
    path('policyholders/',policy_holders,name="policy_holders"),
    
    path('contract/',contract,name="contract"),
    
    path('diagnosis/',diagnosis,name="diagnosis"),




]