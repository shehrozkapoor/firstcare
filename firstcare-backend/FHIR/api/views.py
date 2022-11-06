from cmath import e
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRBatchRequestBundle import FHIRBatchRequestBundle
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRClaimRequestBundle import FHIRClaimRequestBundle
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRCommunicationResponseBundle import FHIRCommunicationResponseBundle
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRPaymentNoticeBundle import FHIRPaymentNoticeBundle
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRPreAuthRequestBundle import FHIRPreAuthRequestBundle
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIRTaskBundle import FHIRTaskBundle
from FHIR.NAPHIES_FHIR_REQUEST.FHIRCommunication import FHIRCommunication
from FHIR.NAPHIES_FHIR_REQUEST.BUNDLES.FHIREligibilityRequestBundle import FHIREligibilityRequestBundle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import asyncio
from FHIR.NAPHIES_FHIR_REQUEST.FHIRCoverage import FHIRCoverage
from FHIR.NAPHIES_FHIR_REQUEST.FHIROrganization import FHIROrganization
from Patient_health_record.models import Document, Encounter
from ..NAPHIES_FHIR_REQUEST.constants import FHIR
from billing.models import Billing
import json
import nest_asyncio
from FHIR.models import *
from django.conf import settings
from fhirpy.base.exceptions import OperationOutcome
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from .tasks import checkStatus
try:
    nest_asyncio.apply()
except:
    pass

try:
    loop = asyncio.get_event_loop()
except:
    loop = asyncio.new_event_loop()

@api_view(['POST'])
def submit_eligibility_request_patient_healthcare_record(request):
    billing_id = request.POST.get('billing-id',None)
    if billing_id is None:
        data={
            "status":"error",
            "message":"billing-id is required"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        bill = Billing.objects.get(id=billing_id)
    except:
        data={
            "status":"error",
            "message":"Invalid billing-id!"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    
    try:
        bundle = FHIREligibilityRequestBundle()
        
        location_id = bill.appointment.clinic.doctor.location.all().first().fhir_location_id
        patient_id = bill.patient.account_id
        bundle_response = loop.run_until_complete(bundle.CreateEligibilityRequestBundle(location_id=location_id,patient_id=patient_id))
        
        eligibility_bundle = CoverageEligibilityBundle(request_bundle_id=bundle_response.id,request_bundle=bundle_response,eligibility_request_id=bundle.coverage_eligibility_request.id)
        eligibility_bundle.save()
        bill.eligibility_bundle = eligibility_bundle
        bill.save()
    except:
        data = {
            "status":"error",
            "message":"something went wrong please try again later!"
        }
        return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
    data = {
            "status":"ok",
            "message":"successfull",
            "data":"eligibility request submitted"
    }
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def submit_eligibility_request_manual(request):
    if request.method == 'GET':
        coverage_id = request.GET.get('coverage_id',None)
        if coverage_id is None:
            coverages = CoverageEligibilityBundle.objects.all()
        else:
            coverages = CoverageEligibilityBundle.objects.filter(id=coverage_id)
        coverage_serializer = CoverageEligibilityBundleSerializer(coverages,many=True)
        data = {
            "status":"ok",
            "message":"success",
            "data":coverage_serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        patient_document_id = request.data.get('document_id',None)
        eligibility_purpose = request.data.get('eligibility_purpose',None)
        location_id = request.data.get('location_id',None)
        start_date = request.data.get('start_date',None)
        end_date = request.data.get('end_date',None)
        with open('/Users/shehrozkapoor/Desktop/FIRST_CARE/firstcare/FHIR/api/response.json','rb') as file:
            response = json.load(file)
        
        if patient_document_id is None or eligibility_purpose is None or location_id is None or start_date is None:
            data={
                "status":"error",
                "message":"please provide all the details with *"    
            }
            
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        # try:
        bundle = FHIREligibilityRequestBundle()
        bundle_response,eligibility_bundle = loop.run_until_complete(bundle.CreateEligibilityRequestBundle(location_id=location_id,patient_id=patient_document_id,purpose=eligibility_purpose,start_insurance_date=start_date,end_insurance_date=end_date))
        try:
            checkStatus(response['entry'][1]['resource'],eligibility_bundle)
        except:
            pass
        eligibility_bundle.response_bundle_id = response['id']
        eligibility_bundle.response_bundle_status=True
        eligibility_bundle.response_bundle = response
        eligibility_bundle.eligibility_response_id = response['entry'][1]['resource']['id']
        eligibility_bundle.save()
        # except:
        #     data = {
        #         "status":"error",
        #         "message":"something went wrong please try again later!"
        #     }
        #     return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        
        data = {
                "status":"ok",
                "message":"successfull",
                "data": response
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'PUT':
        eligibility_id = request.data.get('id',None)
        if eligibility_id is None:
            data={
                "status":"error",
                "message":"id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        eligibility = CoverageEligibilityBundle.objects.get(id=id)
        eligibility.response_eligibility_status='cancelled'
        eligibility.save()
        data={
            "status":"ok",
            "message":"Canceled Eligibility Request"
        }
        return Response(data=data,status=status.HTTP_200_OK)
        

@api_view(['GET'])
def resendEligibilityRequest(request):
    if request.method == "GET":
        eligibility_id = request.GET.get('eligibility_id',None)
        if eligibility_id is None:
            data={
                "status":"error",
                "message":"eligibility_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        with open('/Users/shehrozkapoor/Desktop/FIRST_CARE/firstcare/FHIR/api/response.json','rb') as file:
            response = json.load(file)
        try:
            eligibility = CoverageEligibilityBundle.objects.get(id=eligibility_id)
            bundle = FHIREligibilityRequestBundle()
            location_id = eligibility.request_bundle['entry'][1]['resource']['facility']['reference'].split('Location/')[1]
            patient_id = eligibility.request_bundle['entry'][1]['resource']['patient']['reference'].split('Patient/')[1]
            eligibility_purpose = eligibility.request_bundle['entry'][1]['resource']['purpose']
            start_date = eligibility.request_bundle['entry'][1]['resource']['servicedPeriod']['start']
            end_date = eligibility.request_bundle['entry'][1]['resource']['servicedPeriod']['end']
            bundle_response,eligibility_bundle = loop.run_until_complete(bundle.CreateEligibilityRequestBundle(location_id=location_id,patient_id=patient_id,purpose=eligibility_purpose,start_insurance_date=start_date,end_insurance_date=end_date))
            try:
                checkStatus(response['entry'][1]['resource'],eligibility_bundle)
            except:
                pass
            eligibility_bundle.response_bundle_id = response['id']
            eligibility_bundle.response_bundle_status=True
            eligibility_bundle.response_bundle = response
            eligibility_bundle.eligibility_response_id = response['entry'][1]['resource']['id']
            eligibility_bundle.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        coverage_serializer = CoverageEligibilityBundleSerializer(eligibility_bundle)
        data = {
                "status":"ok",
                "message":"successfull",
                "data": coverage_serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_eligibility_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'eligibility-response':
        eligibility_request_id = body['entry'][1]['resource']['request']['identifier']['value'].split('_')[1]
        bill = Billing.objects.get(eligibility_bundle__eligibility_request_id=eligibility_request_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        
        bill.eligibility_bundle.response_bundle_id = bundle_response.id
        bill.eligibility_bundle.response_bundle_status=True
        bill.eligibility_bundle.response_bundle = body
        bill.eligibility_bundle.eligibility_response_id = body['entry'][1]['resource']['id']
        bill.eligibility_bundle.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_priorauth_request(request):
    billing_id = request.POST.get('billing-id',None)
    if billing_id is None:
        data={
            "status":"error",
            "message":"billing-id is required"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        bill = Billing.objects.get(id=billing_id)
    except:
        data={
            "status":"error",
            "message":"Invalid billing-id!"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    
    try:
        bundle = FHIRPreAuthRequestBundle()
        
        patient_id = bill.patient.account_id
        claim_id = bill.fhir_claim_id
        practitioner_id = bill.appointment.clinic.doctor.fhir_practitioner_id
        bundle_response = loop.run_until_complete(bundle.createFhirPreAuthReqBundle(patient_id=patient_id,claim_id=claim_id,practitioner_id=practitioner_id))
        
        pre_auth_bundle = PreAuthBundle(request_bundle_id=bundle_response.id,request_bundle=bundle_response,pre_auth_request_id=bundle.claim.id)
        pre_auth_bundle.save()
        bill.pre_auth_bundle = pre_auth_bundle
        bill.save()
    except:
        data = {
            "status":"error",
            "message":"something went wrong please try again later!"
        }
        return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
    data = {
            "status":"ok",
            "message":"successfull",
            "data":"Pre Authorization request submitted"
    }
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_priorauth_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'priorauth-response':
        pre_auth_id = body['entry'][1]['resource']['request']['identifier']['value'].split('_')[1]
        bill = Billing.objects.get(pre_auth_bundle__pre_auth_request_id=pre_auth_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        bill.pre_auth_bundle.response_bundle_id = bundle_response.id
        bill.pre_auth_bundle.response_bundle_status = True
        bill.pre_auth_bundle.response_bundle = body
        bill.pre_auth_bundle.claim_response_id = body['entry'][1]['resource']['id']
        bill.pre_auth_bundle.save()
        bill.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def submit_priorauth_requestManual(request):
    if request.method == 'GET':
        id = request.GET.get('preauth-id',None)
        if id is not None:
            objs = PreAuthBundle.objects.filter(id=id)
        else:
            objs = PreAuthBundle.objects.all()
        serializer = PreAuthBundleSerializer(instance=objs,many=True)
        data={
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        claim_id = request.POST.get('claim-id',None)
        claim_type = request.POST.get('claim-type',None)
        claim_sub_type = request.POST.get('claim-sub-type',None)
        if claim_id is None:
            data={
                "status":"error",
                "message":"claim-id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        if claim_type is None:
            data={
                "status":"error",
                "message":"claim-type is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        if claim_sub_type is None:
            data={
                "status":"error",
                "message":"claim-sub-type is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            claim = Claim.objects.get(id=claim_id)
        except:
            data={
                "status":"error",
                "message":"Invalid claim-id!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
        try:
            bundle = FHIRPreAuthRequestBundle()
            bundle_response = loop.run_until_complete(bundle.createFhirPreAuthReqBundle(claim_obj=claim,claim_type=claim_type,sub_type=claim_sub_type))
            
            pre_auth_bundle = PreAuthBundle(patient=claim.patient,request_bundle_id=bundle_response.id,request_bundle=bundle_response,pre_auth_request_id=bundle_response['entry'][1]['fullUrl'].split('Claim/')[1],claim=claim)
            pre_auth_bundle.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Pre Authorization request submitted"
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_priorauth_response_manual(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'priorauth-response':
        pre_auth_id = body['entry'][1]['resource']['request']['identifier']['value'].split('_')[1]
        pre_auth_bundle = PreAuthBundle.objects.get(pre_auth_request_id=pre_auth_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        pre_auth_bundle.response_bundle_id = bundle_response.id
        pre_auth_bundle.response_bundle_status = True
        pre_auth_bundle.response_bundle = body
        pre_auth_bundle.claim_response_id = body['entry'][1]['resource']['id']
        pre_auth_bundle.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_claim_request(request):
    billing_id = request.POST.get('billing-id',None)
    if billing_id is None:
        data={
            "status":"error",
            "message":"billing-id is required"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        bill = Billing.objects.get(id=billing_id)
    except:
        data={
            "status":"error",
            "message":"Invalid billing-id!"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    
    try:
        bundle = FHIRClaimRequestBundle()
        
        patient_id = bill.patient.account_id
        claim_id = bill.fhir_claim_id
        practitioner_id = bill.appointment.clinic.doctor.fhir_practitioner_id
        bundle_response = loop.run_until_complete(bundle.createFHIRClaimRequestBundle(patient_id=patient_id,claim_id=claim_id,practitioner_id=practitioner_id))
        claim_bundle = ClaimBundle(request_bundle_id=bundle_response.id,request_bundle=bundle_response,claim_request_id=claim_id)
        claim_bundle.save()
        bill.claim_bundle = claim_bundle
        bill.save()
    except:
        data = {
            "status":"error",
            "message":"something went wrong please try again later!"
        }
        return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
    data = {
            "status":"ok",
            "message":"successfull",
            "data":"Claim request submitted"
    }
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_claim_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'claim-response':
        claim_id = body['entry'][1]['resource']['request']['identifier']['value'].split('_')[1]
        bill = Billing.objects.get(claim_bundle__claim_request_id=claim_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        bill.claim_bundle.response_bundle_id = bundle_response.id
        bill.claim_bundle.response_bundle_status = True
        bill.claim_bundle.response_bundle = body
        bill.claim_bundle.claim_response_id = body['entry'][1]['resource']['id']
        bill.claim_bundle.save()
        bill.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def submit_claim_request_manual(request):
    if request.method == 'GET':
        claim_id = request.GET.get('claim-id',None)
        if claim_id is not None:
            claim = ClaimBundle.objects.filter(id=claim_id)
        else:
            claim = ClaimBundle.objects.all()
            
        serializer = ClaimBundleSerializer(instance=claim,many=True)
        
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        preauth_id = request.POST.get('preauth-id',None)
        claim_type = request.POST.get('claim-type',None)
        claim_sub_type = request.POST.get('claim-sub-type',None)
        
        if claim_type is None:
            data={
                "status":"error",
                "message":"claim-type is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
        
        if claim_sub_type is None:
            data={
                "status":"error",
                "message":"claim-sub-type is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)


        bundle = FHIRClaimRequestBundle()
        
        if preauth_id is None:
            claim_id = request.POST.get('claim-id',None)
            if claim_id is None:
                data={
                    "status":"error",
                    "message":"preauth-id is not given then claim-id is required!"
                }
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    claim = Claim.objects.get(id=claim_id)
                    bundle_response = loop.run_until_complete(bundle.createFHIRClaimRequestBundle(claim_obj=claim,claim_type=claim_type,sub_type=claim_sub_type))
                    claim_bundle = ClaimBundle(patient=claim.patient,request_bundle_id=bundle_response.id,request_bundle=bundle_response,claim_request_id=bundle_response['entry'][1]['fullUrl'].split('Claim/')[1])
                except:
                    data={
                        "status":"error",
                        "message":"Invalid claim-id!"
                    }
                    return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                preauth = PreAuthBundle.objects.get(id=preauth_id)
                bundle_response = loop.run_until_complete(bundle.createFHIRClaimRequestBundle(claim_obj=preauth.claim,claim_type=claim_type,sub_type=claim_sub_type))
                claim_bundle = ClaimBundle(preauth=preauth,patient=preauth.patient,request_bundle_id=bundle_response.id,request_bundle=bundle_response,claim_request_id=bundle_response['entry'][1]['fullUrl'].split('Claim/')[1])
            except:
                data={
                    "status":"error",
                    "message":"Invalid preauth-id!"
                }
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
        claim_bundle.save()
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Claim request submitted"
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_claim_response_manual(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'claim-response':
        claim_id = body['entry'][1]['resource']['request']['identifier']['value'].split('_')[1]
        claim_bundle = ClaimBundle.objects.get(claim_request_id=claim_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        claim_bundle.response_bundle_id = bundle_response.id
        claim_bundle.response_bundle_status = True
        claim_bundle.response_bundle = body
        claim_bundle.claim_response_id = body['entry'][1]['resource']['id']
        claim_bundle.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def submit_communication_request(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'communication-request':
        claim_id = body['entry'][1]['resource']['about'][0]['identifier']['value'].split('_')[1]
        claim = ClaimBundle.objects.get(claim_request_id=claim_id)
        bundle_response = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        communication_bundle = CommunicationBundle(claim=claim,request_bundle_id=bundle_response.id,communication_request_id=body['entry'][1]['resource']['id'],request_bundle=bundle_response,request_payload=body['entry'][1]['resource']['payload'])
        communication_bundle.save()
        return Response(data=bundle_response,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def submit_communication_response(request):
    if request.method == 'GET':
        communication_id = request.POST.get('communication-id',None)
        if communication_id is not None:
            communication = CommunicationBundle.objects.filter(id=communication_id)
        else:
            communication = CommunicationBundle.objects.all()
            
        serializer = CommunicationBundleSerializer(instance=communication,many=True)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        communication_id = request.POST.get('communication-id',None)
        document_id = request.POST.get('document-id',None)
        payload_message = request.POST.get('payload-message',None)
        payload_title = request.POST.get('payload-title',None)
        if communication_id is None:
            data={
                "status":"error",
                "message":"communication-id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            communication = CommunicationBundle.objects.get(id=communication_id)
        except:
            data={
                "status":"error",
                "message":"Invalid communication-id!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
        try:
            bundle = FHIRCommunicationResponseBundle()
            document = Document.objects.get(id=document_id)
            document_path = f"{settings.BASE_DIR}/{document.attachment.url}"
            fhir_communication = FHIRCommunication()
            payload_response = fhir_communication.createPayload(payload_message=payload_message,title=payload_title,pdf_file=document_path)
            bundle_response = loop.run_until_complete(bundle.createCommunicationResponseBundle(patient_id=communication.claim.patient,communication_request_id=communication.communication_request_id,claim_id=communication.claim.claim_request_id,payload=payload_response))
            communication.response_bundle_id = bundle_response.id
            communication.response_bundle_status = True
            communication.response_bundle = bundle_response
            communication.response_payload = bundle_response['entry'][1]['resource']['payload']
            communication.communication_response_id = bundle_response['entry'][1]['resource']['id']
            communication.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Communication response sended"
        }
        return Response(data=data,status=status.HTTP_200_OK)




@api_view(['GET','POST'])
def submit_payment_reconciliation(request):
    if request.method == 'GET':
        payment_id = request.GET.get('id',None)
        if payment_id is not None:
            payment_reconciliation = PaymentReconciliationBundle.objects.filter(id=id)
        else:
            payment_reconciliation = PaymentReconciliationBundle.objects.all()
        serializer = PaymentReconciliationBundleSerializer(instance=payment_reconciliation,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        bundle = FHIR()
        if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'payment-reconciliation':
            claim_request_id = body['entry'][1]['resource']['detail'][0]['request']['identifier']['value'].split('_')[-1]
            claim_response_id = body['entry'][1]['resource']['detail'][0]['response']['identifier']['value'].split('_')[-1]
            claim = ClaimBundle.objects.get(claim_request_id=claim_request_id,claim_response_id=claim_response_id)
            bundle = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
            payment_reconciliation = PaymentReconciliationBundle(claim=claim,claim_request_id=claim_request_id,payment_reconciliation_id=body['entry'][1]['resource']['id'],request_bundle_id=body['id'],request_bundle=body,claim_response_id=claim_response_id)
            payment_reconciliation.save()
            return Response(data=bundle,status=status.HTTP_200_OK)
        return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_payment_notice(request):
    payment_id = request.POST.get('payment-id',None)
    payment_date = request.POST.get('payment-date',None)
    amount = request.POST.get('amount',None)
    payment_status = request.POST.get('payment-status',None)
    
    if payment_id is None:
        data={
            "status":"error",
            "message":"payment-id is required"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        payment = PaymentReconciliationBundle.objects.get(id=payment_id)
    except:
        data={
            "status":"error",
            "message":"Invalid billing-id!"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        bundle = FHIRPaymentNoticeBundle()
        bundle_response = loop.run_until_complete(bundle.createFhirPaymentNotice(patient_id=payment.claim.patient,payment_reconciliation_id=payment.payment_reconciliation_id,payment_date=payment_date,amount=amount,payment_status=payment_status))
        payment_notice = PaymentNoticeBundle(request_bundle_id=bundle_response['id'],request_bundle=bundle_response,payment_reconciliation_id=bundle_response['entry'][1]['resource']['payment']['identifier']['value'])
        payment_notice.save()
    except:
        data = {
            "status":"error",
            "message":"something went wrong please try again later!"
        }
        return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
    data = {
            "status":"ok",
            "message":"successfull",
            "data":"Payment Notice sended!"
    }
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def submit_cancel_request(request):
    if request.method == 'GET':
        task_id = request.GET.get('id',None)
        if task_id is not None:
            cancel_request = TaskBundle.objects.filter(id=id,request_type='cancel')
        else:
            cancel_request = TaskBundle.objects.filter(request_type='cancel')
        serializer = TaskBundleSerializer(instance=cancel_request,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        claim_id = request.POST.get('claim-id',None)
        preauth_id = request.POST.get('preauth-id',None)
        task_status = request.POST.get('status',None)
        intent = request.POST.get('intent',None)
        priority = request.POST.get('priority',None)
        task_reason_code = request.POST.get('task-reason-code',None)
        
        bundle = FHIRTaskBundle()
        
        if claim_id is not None:
            try:
                claim = ClaimBundle.objects.get(id=claim_id)
                patient_id = claim.patient.document_id
                claim_id = claim.claim_request_id
                bundle_response = loop.run_until_complete(bundle.createFHIRTaskBundle(patient_id=patient_id,request_type="cancel-request",status=task_status,intent=intent,priority=priority,focus_resource_type="Claim",focus_resource_type_id=claim_id,task_reason_code=task_reason_code,task_code="cancel"))
            except:
                data={
                    "status":"error",
                    "message":"Invalid claim-id!"
                }
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        else:
            if preauth_id is None:
                data={
                    "status":"error",
                    "message":"if claim-id not passed then preauth-id is compulsory"
                }
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)
            else:
                preauth = PreAuthBundle.objects.get(id=preauth_id)
                claim_id = preauth.request_bundle['entry'][1]['resource']['id']
                patient_id = preauth.patient.document_id
                claim=preauth.claim
                bundle_response = loop.run_until_complete(bundle.createFHIRTaskBundle(patient_id=patient_id,request_type="cancel-request",status=task_status,intent=intent,priority=priority,focus_resource_type="Claim",focus_resource_type_id=claim_id,task_reason_code=task_reason_code,task_code="cancel"))
        try:        
            task_bundle = TaskBundle(claim=claim,request_bundle_id=bundle_response['id'],request_bundle=bundle_response,request_task_id=bundle_response['entry'][1]['fullUrl'].split('Task/')[1],request_type='cancel')
            task_bundle.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Cancel Request Sended!"
        }
        return Response(data=data,status=status.HTTP_200_OK)


@api_view(['POST'])
def submit_cancel_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'cancel-response':
        claim_id = body['entry'][1]['resource']['focus']['identifier']['value'].split('_')[-1]
        task_bundle = TaskBundle.objects.get(claim__claim_request_id=claim_id)
        bundle = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        task_bundle.response_bundle_id=bundle['id']
        task_bundle.response_bundle=bundle
        task_bundle.response_task_id=bundle['entry'][1]['resource']['id']
        task_bundle.save()
        return Response(data=bundle,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def submit_status_request(request):
    if request.method == 'GET':
        task_id = request.GET.get('id',None)
        if task_id is not None:
            status_request = TaskBundle.objects.filter(id=id,request_type='status')
        else:
            status_request = TaskBundle.objects.filter(request_type='status')
        serializer = TaskBundleSerializer(instance=status_request,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        claim_id = request.POST.get('claim-id',None)
        task_status = request.POST.get('status',None)
        intent = request.POST.get('intent',None)
        priority = request.POST.get('priority',None)
        
        if claim_id is None:
            data={
                "status":"error",
                "message":"claim-id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            claim = ClaimBundle.objects.get(id=claim_id)
        except:
            data={
                "status":"error",
                "message":"Invalid claim-id!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            patient_id = claim.patient.document_id
            claim_id = claim.claim_request_id
            
            bundle = FHIRTaskBundle()
            bundle_response = loop.run_until_complete(bundle.createFHIRTaskBundle(patient_id=patient_id,request_type="status-check",status=task_status,intent=intent,priority=priority,focus_resource_type="Claim",focus_resource_type_id=claim_id,task_code="status"))
            
            task_bundle = TaskBundle(claim=claim,request_bundle_id=bundle_response['id'],request_bundle=bundle_response,request_task_id=bundle_response['entry'][1]['fullUrl'].split('Task/')[1],request_type='status')
            task_bundle.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Status Check Request Sended!"
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_status_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'status-response':
        claim_id = body['entry'][1]['resource']['focus']['identifier']['value'].split('_')[-1]
        task_bundle = TaskBundle.objects.get(claim__claim_request_id=claim_id,request_type='status')
        bundle = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        task_bundle.response_bundle_id=bundle['id']
        task_bundle.response_bundle=bundle
        task_bundle.response_task_id=bundle['entry'][1]['resource']['id']
        task_bundle.save()
        return Response(data=bundle,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def submit_poll_request(request):
    if request.method == 'GET':
        poll_id = request.POST.get('id',None)
        if poll_id is None:
            poll = task_bundle = TaskBundle.objects.filter(request_type='poll')
        else:
            poll = task_bundle = TaskBundle.objects.filter(id=poll_id,request_type='poll')
            
        serializer = TaskBundleSerializer(instance=poll,many=True)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        claim_id = request.POST.get('claim-id',None)
        task_status = request.POST.get('status',None)
        intent = request.POST.get('intent',None)
        priority = request.POST.get('priority',None)
        
        if claim_id is None:
            data={
                "status":"error",
                "message":"claim-id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            claim = ClaimBundle.objects.get(id=claim_id)
        except:
            data={
                "status":"error",
                "message":"Invalid claim-id!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            patient_id = claim.patient.document_id
            
            bundle = FHIRTaskBundle()
            bundle_response = loop.run_until_complete(bundle.createFHIRTaskBundle(patient_id=patient_id,request_type="poll-request",status=task_status,intent=intent,priority=priority,task_code="poll"))
            
            task_bundle = TaskBundle(request_bundle_id=bundle_response['id'],request_bundle=bundle_response,request_task_id=bundle_response['entry'][1]['fullUrl'].split('Task/')[1],request_type='poll')
            task_bundle.save()
        except:
            data = {
                "status":"error",
                "message":"something went wrong please try again later!"
            }
            return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
        data = {
                "status":"ok",
                "message":"successfull",
                "data":"Poll Request Sended!"
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_poll_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'poll-response':
        task_bundle_id = body['entry'][1]['resource']['output'][0]['valueReference']['reference'].split('Bundle/')[1]
        task_bundle = TaskBundle.objects.get(request_bundle_id=task_bundle_id,request_type='poll')
        bundle = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        task_bundle.response_bundle_id=bundle['id']
        task_bundle.response_bundle=bundle
        task_bundle.response_task_id=bundle['entry'][1]['resource']['id']
        task_bundle.save()
        return Response(data=bundle,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_batch_request(request):
    claim_id = request.POST.get('claim-id',None)
    if claim_id is None:
        data={
            "status":"error",
            "message":"claim-id is required"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    
    claim_id = claim_id.split(',')
    try:
        claims = Claim.objects.filter(id__in=claim_id)
    except:
        data={
            "status":"error",
            "message":"Invalid claim-id!"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    try:
        bundle = FHIRBatchRequestBundle()
        bundle_response = loop.run_until_complete(bundle.createFHIRBatchRequestBundle(claims))
        
        batch_bundle = BatchRequestBundle(request_bundle_id=bundle_response['id'],request_bundle=bundle_response)
        batch_bundle.save()
    except:
        data = {
            "status":"error",
            "message":"something went wrong please try again later!"
        }
        return Response(data=data,status=status.HTTP_408_REQUEST_TIMEOUT)
    data = {
            "status":"ok",
            "message":"successfull",
            "data":"Batch Request Sended!"
    }
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_poll_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    bundle = FHIR()
    if body['resourceType'] == 'Bundle' and body['type'] == 'message' and body['entry'][0]['resource']['eventCoding']['code'] == 'poll-response':
        bundle_id = body['entry'][1]['resource']['output'][0]['valueReference']['reference'].split('Bundle/')[1]
        task_bundle = TaskBundle.objects.get(request_bundle_id=bundle_id)
        bundle = loop.run_until_complete(bundle.createResourceBundleResponseJson(json_body=body))
        task_bundle.response_bundle_id = bundle['id']
        task_bundle.response_bundle=bundle
        task_bundle.response_task_id=bundle['entry'][1]['resource']['id']
        task_bundle.save()
        return Response(data=bundle,status=status.HTTP_200_OK)
    return Response(data={"status":"error","message":"invalid resource"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','DELETE'])
def supporting_info(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is None:
            obj = SupportingInfo.objects.all()
        else:
            obj = SupportingInfo.objects.filter(id=id)
        serializer = SupportingInfoSerializer(obj,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SupportingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        obj = SupportingInfo.objects.get(id=id)
        obj.delete()
        data = {
            "status":"ok",
            "message":"successfull Deleted",
        }
        return Response(data=data,status=status.HTTP_200_OK)
    
@api_view(['GET','POST','DELETE'])
def diagnosis_information(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is None:
            obj = DiagnosisInformation.objects.all()
        else:
            obj = DiagnosisInformation.objects.filter(id=id)
        serializer = DiagnosisInformationSerializer(obj,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DiagnosisInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        obj = DiagnosisInformation.objects.get(id=id)
        obj.delete()
        data = {
            "status":"ok",
            "message":"successfull Deleted",
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST','DELETE'])
def care_team(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is None:
            obj = CareTeam.objects.all()
        else:
            obj = CareTeam.objects.filter(id=id)
        serializer = CareTeamSerializer(obj,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CareTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        obj = CareTeam.objects.get(id=id)
        obj.delete()
        data = {
            "status":"ok",
            "message":"successfull Deleted",
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST','DELETE'])
def items(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is None:
            print('hello')
            obj = Items.objects.all()
        else:
            print('hello 2')
            obj = Items.objects.filter(id=id)
        serializer = ItemsSerializer(obj,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        obj = Items.objects.get(id=id)
        obj.delete()
        data = {
            "status":"ok",
            "message":"successfull Deleted",
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST','DELETE'])
def claims(request):
    if request.method == 'GET':
        id = request.GET.get('id',None)
        if id is None:
            obj = Claim.objects.all()
        else:
            obj = Claim.objects.filter(id=id)
        serializer = ClaimSerializer(obj,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClaimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        obj = Claim.objects.get(id=id)
        obj.delete()
        data = {
            "status":"ok",
            "message":"successfull Deleted",
        }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET'])
def testfhir(request):
    
    # org = FHIROrganization()
    # org = loop.run_until_complete(org.createOrganization(id="bff3aa1fbd3648619ac082357bf135db",name="Saudi National Hospital",type="prov"))
    # return Response(data=org,status=status.HTTP_200_OK)

    # coverage = FHIRCoverage()
    # coverage = loop.run_until_complete(coverage.createCoverage(patient_id="1323231312-dajkbdsj-dsabds",org_id="bff3aa1fbd3648619ac082357bf135db"))
    # return Response(data=coverage,status=status.HTTP_200_OK)
    

    # bundle = FHIREligibilityRequestBundle()
    # bundle = loop.run_until_complete(bundle.CreateEligibilityRequestBundle(location_id="dca494c0-fd3c-4b9e-89f8-24950d8b4427",patient_id="3083472"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # with open('/Users/shehrozkapoor/Desktop/FIRST_CARE/firstcare/FHIR/demo.json','rb') as file:
    #     data = json.load(file)
    #     print(data)
    # claim = FHIRClaim()
    # claim = loop.run_until_complete(claim.sendClaim(patient_id="3083472",claim_type="institutional-claim",payor_org="bff3aa1fbd3648619ac082357bf135db",processPriority="normal",careTeams=data['care_team'],supportingInfos=data['supporting_info'],diagnosis=data['diagnosis'],product_services=data['product_services'],service_date="2021-08-30",quantity_val=1,unit_price=100,net_price=115,total_amount=115))
    # return Response(data=claim,status=status.HTTP_200_OK)
    

    # bundle = FHIRPreAuthRequestBundle()
    # bundle = loop.run_until_complete(bundle.createFhirPreAuthReqBundle(patient_id="3083472",practitioner_id="1470745",claim_id="25ce8f5e-5e58-4b42-8837-1422ab3f5f2d"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    
    # id:25ce8f5e-5e58-4b42-8837-1422ab3f5f2d
    # bundle = FHIRClaimRequestBundle()
    # bundle = loop.run_until_complete(bundle.createFHIRClaimRequestBundle(patient_id="3083472",claim_id="25ce8f5e-5e58-4b42-8837-1422ab3f5f2d",practitioner_id="1470745"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # bundle = FHIRCommunicationResponseBundle()
    # bundle = loop.run_until_complete(bundle.createCommunicationResponseBundle(patient_id="3083472",communication_id="1632427"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # bundle = FHIRPaymentNotice()
    # bundle = loop.run_until_complete(bundle.createPaymentNotice(payment_reconciliation_id="92284",payment_date="2022-06-09",payment_status="completed",amount=1200))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # bundle = FHIRPaymentNoticeBundle()
    # bundle = loop.run_until_complete(bundle.createFhirPaymentNotice(patient_id="3083472",payment_notice_id="5c91fc8a-99c3-4396-902e-3d8b952b26bf"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # bundle = FHIRTask()
    # bundle = loop.run_until_complete(bundle.createTask(status="requested",intent="order",priority="routine",task_reason_code="prov",focus_resource_type="claim",focus_resource_type_id="25ce8f5e-5e58-4b42-8837-1422ab3f5f2d",payor_org="bff3aa1fbd3648619ac082357bf135db",last_modified=None,task_code="poll"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    
    # bundle = FHIRTaskBundle()
    # bundle = loop.run_until_complete(bundle.createFHIRTaskBundle(task_id="6c307926-7a6d-452f-8352-9e13d171b284",patient_id="3083472"))
    # return Response(data=bundle,status=status.HTTP_200_OK)
    pass
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def checkCoverage(request):
    if request.method == 'GET':
        document_id = request.GET.get('document_id',None)
        if document_id is None or len(document_id) == 0:
            data = {
                "status":"error",
                "message":"document_id is required!!!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        # check eligibility
        fhir_coverage = FHIRCoverage()
        try:
            response = loop.run_until_complete(fhir_coverage.getCoverageByPatientId(document_id=document_id))
            data= {
                "status":"ok",
                "message":"successfull",
                "data":response
            }
            return Response(data=data,status=status.HTTP_200_OK)
        except AttributeError:
            data= {
                "status":"error",
                "message":"No Coverage Found for this Beneficiary",
            }
            print("attribute error")
            
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)