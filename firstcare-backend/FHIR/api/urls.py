from django.urls import path
from .views import *


urlpatterns = [
    path('testfhir/',testfhir,name="testfhir"),
    
    
    path('eligibilityrequestauto/',submit_eligibility_request_patient_healthcare_record,name="submit_eligibility_request_patient_healthcare_record"),
    path('eligibilityresponse/',submit_eligibility_response,name="submit_eligibility_response"),
    
    path('eligibilityrequestmanual/',submit_eligibility_request_manual,name="submit_eligibility_request_manual"),
    path('resendeligibilityrequest/',resendEligibilityRequest,name="resendEligibilityRequest"),
    
    path('priorauthrequest/',submit_priorauth_request,name="submit_priorauth_request"),
    path('priorauthresponse/',submit_priorauth_response,name="submit_priorauth_response"),
    path('priorauthrequestmanual/',submit_priorauth_requestManual,name="submit_priorauth_requestManual"),
    path('priorauthresponsemanual/',submit_priorauth_response_manual,name="submit_priorauth_response_manual"),

    path('claimrequest/',submit_claim_request,name="submit_claim_request"),
    path('claimresponse/',submit_claim_response,name="submit_claim_response"),
    
    path('claimrequestmanual/',submit_claim_request_manual,name="submit_claim_request_manual"),
    path('claimresponsemanual/',submit_claim_response_manual,name="submit_claim_response_manual"),
    
    path('communicationrequest/',submit_communication_request,name="submit_communication_request"),
    path('communicationresponse/',submit_communication_response,name="submit_communication_response"),
    
    path('paymentreconciliation/',submit_payment_reconciliation,name="submit_payment_reconciliation"),
    
    path('paymentnotice/',submit_payment_notice,name="submit_payment_notice"),
    
    path('cancelrequest/',submit_cancel_request,name="submit_cancel_request"),
    path('cancelresponse/',submit_cancel_response,name="submit_cancel_response"),
    
    path('statusrequest/',submit_status_request,name="submit_status_request"),
    path('statusresponse/',submit_status_response,name="submit_status_response"),
    
    path('pollrequest/',submit_poll_request,name="submit_poll_request"),
    path('pollresponse/',submit_poll_response,name="submit_poll_response"),
    
    path('batchrequest/',submit_batch_request,name="submit_batch_request"),
    
    path('checkcoverage/',checkCoverage,name="checkcoverage"),
    path('testfhir/',testfhir,name="testfhir"),

    path('supportinginfo/',supporting_info,name="supporting_info"),
    path('diagnosisinformation/',diagnosis_information,name="diagnosis_information"),
    path('careteam/',care_team,name="care_team"),
    path('items/',items,name="items"),
    path('claims/',claims,name="claims"),
]