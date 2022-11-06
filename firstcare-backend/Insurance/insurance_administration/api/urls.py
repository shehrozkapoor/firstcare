from django.urls import path
from .views import *


urlpatterns = [
    # product
    path('region/',region,name="Region"),
    path('district/',district,name="district"),
    path('conversion/',conversion,name="conversion"),
    path('treatment/',treatment,name="treatment"),
    path('insuree/',insuree,name="insuree"),
    path('policy/',policy,name="policy"),
    path('extramemberceiling/',extra_member_ceiling,name="extra_member_ceiling"),
    path('maximumceiling/',maximum_ceiling,name="maximum_ceiling"),
    path('number/',number,name="number"),
    path('ceiling/',ceiling,name="ceiling"),
    path('distribution/',distribution,name="distribution"),
    path('level/',level,name="level"),
    path('sublevel/',sub_level,name="sub_level"),
    path('capitationpayment/',capitation_payment,name="capitation_payment"),
    path('product/',product,name="product"),
    # health facility
    path('healthfacilitylegalform/',health_facility_legal_form,name="health_facility_legal_form"),
    path('healthfacilitysublevel/',health_facility_sub_level,name="health_facility_sub_level"),
    path('caretype/',care_type,name="care_type"),
    path('servicespricelist/',services_price_list,name="services_price_list"),
    path('itempricelist/',item_price_list,name="item_price_list"),
    path('healthfacilities/',health_facilities,name="health_facilities"),
    # medical services
    path('servicetype/',service_type,name="service_type"),
    path('servicecategory/',service_category,name="service_category"),
    path('servicelevel/',service_level,name="service_level"),
    path('medicalservices/',medical_services,name="medical_services"),
    # medical items
    path('itemtype/',item_type,name="item_type"),
    path('medicalitem/',medical_item,name="medical_item"),
    # medical services price list
    path('medicalservicespricelist/',medical_services_price_list,name="medical_services_price_list"),
    # medical items price list
    path('medicalitemspricelist/',medical_items_price_list,name="medical_items_price_list"),
    # payer
    path('payertype/',payer_type,name="payer_type"),
    path('payer/',payer,name="payer"),
    # contribution plan
    path('contributionrules/',contribution_rules,name="contribution_rules"),
    path('contributionplan/',contribution_plan,name="contribution_plan"),

]