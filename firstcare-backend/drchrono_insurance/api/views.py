from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from Patient.api.serializers import PatientSerializer
from billing.api.serializers import BillingSerializer, PaymentSerializer

from billing.models import Billing, Payment
from .serializers import *
from rest_framework import status
from drchrono_insurance.models import *
from datetime import date, datetime,timedelta
from django.db.models import Q
from dateutil.relativedelta import relativedelta
import json
import csv
from FHIR.NAPHIES_FHIR_REQUEST.FHIRCoverage import FHIRCoverage
from FHIR.NAPHIES_FHIR_REQUEST.FHIRPatient import FHIRPatient
from FHIR.NAPHIES_FHIR_REQUEST.FHIROrganization import FHIROrganization
from FHIR.NAPHIES_FHIR_REQUEST.FHIRClaim import FHIRClaim

import asyncio
try:
    loop = asyncio.get_event_loop()
except:
    loop = asyncio.new_event_loop()


'''
CRUD operation on the insurance company
'''

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def insurance_company(request):
    if request.method == 'GET':
        obj = InsuranceCompany.objects.all()
        serializer = InsuranceCompanySerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        insurance_company_id = request.POST.get('insurance_company_id',None)
        if insurance_company_id is None:
            data = {
                "status":"error",
                "message":"insurance_company_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = InsuranceCompany.objects.get(id=insurance_company_id)
        serializer = InsuranceCompanySerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        insurance_company_id = request.POST.get('insurance_company_id',None)
        if insurance_company_id is None:
            data = {
                "status":"error",
                "message":"insurance_company_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = InsuranceCompany.objects.get(id=insurance_company_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the insurance plan type
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def insurance_plan_type(request):
    if request.method == 'GET':
        obj = InsurancePlanType.objects.all()
        serializer = InsurancePlanTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsurancePlanTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        insurance_plan_type_id = request.POST.get('insurance_plan_type_id',None)
        if insurance_plan_type_id is None:
            data = {
                "status":"error",
                "message":"insurance_plan_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = InsurancePlanType.objects.get(id=insurance_plan_type_id)
        serializer = InsurancePlanTypeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        insurance_plan_type_id = request.POST.get('insurance_plan_type_id',None)
        if insurance_plan_type_id is None:
            data = {
                "status":"error",
                "message":"insurance_plan_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = InsurancePlanType.objects.get(id=insurance_plan_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the hcfa
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hcfa(request):
    if request.method == 'GET':
        obj = HCFA.objects.all()
        serializer = HCFASerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HCFASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        hcfa_id = request.POST.get('hcfa_id',None)
        if hcfa_id is None:
            data = {
                "status":"error",
                "message":"hcfa_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCFA.objects.get(id=hcfa_id)
        serializer = HCFASerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        hcfa_id = request.POST.get('hcfa_id',None)
        if hcfa_id is None:
            data = {
                "status":"error",
                "message":"hcfa_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCFA.objects.get(id=hcfa_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

'''
CRUD operation on the subscriber
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscriber(request):
    if request.method == 'GET':
        obj = Subscriber.objects.all()
        serializer = SubscriberSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        subscriber_id = request.POST.get('subscriber_id',None)
        if subscriber_id is None:
            data = {
                "status":"error",
                "message":"subscriber_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Subscriber.objects.get(id=subscriber_id)
        serializer = SubscriberSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        subscriber_id = request.POST.get('subscriber_id',None)
        if subscriber_id is None:
            data = {
                "status":"error",
                "message":"subscriber_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Subscriber.objects.get(id=subscriber_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the insurance
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def insurance(request):
    if request.method == 'GET':
        document_id = request.GET.get('document_id','')
        print(document_id)
        if len(document_id) !=0:
            obj = Insurance.objects.filter(patient__document_id=document_id)
        else:
            obj = Insurance.objects.all()
        serializer = InsuranceSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        insurance_id = request.POST.get('insurance_id',None)
        if insurance_id is None:
            data = {
                "status":"error",
                "message":"insurance_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            obj = Insurance.objects.get(id=insurance_id)
        except:
            data = {
                "status":"error",
                "message":"no insurance found with this id"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        serializer = InsuranceSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        insurance_id = request.POST.get('insurance_id',None)
        if insurance_id is None:
            data = {
                "status":"error",
                "message":"insurance_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Insurance.objects.get(id=insurance_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
if you go to the localhost:8000/drchronoinsurance/billing-summary
you can see that we want the get the current quater date
e.g
today is 16 May 2022
so it will return you
1 JAN 2022
'''
def getQuaterStartDate(date,quater):
    dtFirstDay = datetime(date.date().year, 3 * quater - 2, 1)

    return dtFirstDay

'''
if you go to the localhost:8000/drchronoinsurance/billing-summary
you can see that we want the get the current quater date
e.g
today is 16 May 2022
so it will return you
30 JUN 2022
'''
def getQuaterEndDate(date,quater):
    dtLastDay = datetime(date.year, 3 * quater + 1, 1) + timedelta(days=-1)
    return dtLastDay


'''
if you go to the localhost:8000/drchronoinsurance/billing-summary
you can see that we want the get the previous month date
e.g
today is 16 May 2022
so it will return you
1 April 2022 30 April 2022
'''
def getPreviousMonthDate():
    last_day_of_prev_month = datetime.today().replace(day=1) - timedelta(days=1)

    start_day_of_prev_month = datetime.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

    return start_day_of_prev_month,last_day_of_prev_month

'''
if you go to the localhost:8000/drchronoinsurance/billing-summary
you can see that we want the get the previous quater date
e.g
today is 16 May 2022
so it will return you
1 July 2021
'''

def previous_quarter(ref):
    first_month_of_quarter = ((ref.month - 1) // 3) * 3 + 1
    return ref.replace(month=first_month_of_quarter, day=1) - relativedelta(days=1)



'''
if you go to the localhost:8000/drchronoinsurance/billing-summary
you can see that we want the get the previous quater start and end date
e.g
today is 16 May 2022
so it will return you
1 July 2021 31 dec 2021
'''
def getPreviousQuaterStartEndDate():
    previous_quater_end_date = previous_quarter(datetime.today().date())

    quater = int((previous_quater_end_date.month - 1) / 3 + 1)

    previous_quarter_start_date =  datetime(previous_quater_end_date.year, 3 * quater - 2, 1).date()

    return previous_quarter_start_date,previous_quater_end_date


'''
this is will give you all the details of the patient payment that was made in the current quater
previous quater
'''
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def billingSummary(request):
    current_date=datetime.today()

    month_to_date = current_date.replace(day=1)
    previousMonthStartDate,previousMonthEndDate = getPreviousMonthDate()


    year_to_date = current_date.replace(day=1,month=1)

    currQuarter = int((current_date.month - 1) / 3 + 1)
    currentQuaterStartDate = getQuaterStartDate(current_date,currQuarter)

    previousQuaterStartDate,previousQuaterEndDate = getPreviousQuaterStartEndDate()


    data = {}

    month_to_date_billing = Payment.objects.filter(payment_date__range=[month_to_date.date(),current_date.date()])
    sum = 0
    for payment in month_to_date_billing:
        sum+=payment.amount

    data['month-to-date']={
        "start-date":month_to_date.strftime('%Y-%m-%d'),
        "end-date":current_date.strftime('%Y-%m-%d'),
        "total-income": sum
    }

    previous_month_billing = Payment.objects.filter(payment_date__range=[previousMonthStartDate.strftime('%Y-%m-%d'),previousMonthEndDate.strftime('%Y-%m-%d')])
    sum = 0
    for payment in previous_month_billing:
        sum+=payment.amount

    data['previous-month']={
        "start-date":previousMonthStartDate.strftime('%Y-%m-%d'),
        "end-date":previousMonthEndDate.strftime('%Y-%m-%d'),
        "total-income": sum
    }

    year_to_date_billing = Payment.objects.filter(payment_date__range=[year_to_date.strftime('%Y-%m-%d'),current_date.strftime('%Y-%m-%d')])
    sum = 0
    for payment in year_to_date_billing:
        sum+=payment.amount

    data['year-to-date'] = {
        "start-date":year_to_date.strftime('%Y-%m-%d'),
        "end-date":current_date.strftime('%Y-%m-%d'),
        "total-income": sum
    }

    previous_month_billing = Payment.objects.filter(payment_date__range=[year_to_date.strftime('%Y-%m-%d'),current_date.strftime('%Y-%m-%d')])
    sum = 0
    for payment in previous_month_billing:
        sum+=payment.amount

    data['year-to-date'] = {
        "start-date":year_to_date.strftime('%Y-%m-%d'),
        "end-date":current_date.strftime('%Y-%m-%d'),
        "total-income": sum
    }

    current_quater_billing = Payment.objects.filter(payment_date__range=[currentQuaterStartDate.strftime('%Y-%m-%d'),current_date.strftime('%Y-%m-%d')])
    sum = 0
    for payment in current_quater_billing:
        sum+=payment.amount


    data['current-quater']= {
        "start-date":currentQuaterStartDate.strftime('%Y-%m-%d'),
        "end-date":current_date.strftime('%Y-%m-%d'),
        "total-income": sum
    }

    previous_quater_billing = Payment.objects.filter(payment_date__range=[previousQuaterStartDate.strftime('%Y-%m-%d'),previousQuaterEndDate.strftime('%Y-%m-%d')])
    sum = 0
    for payment in previous_quater_billing:
        sum+=payment.amount

    data["previous-quater"] = {
            "start-date":previousQuaterStartDate.strftime('%Y-%m-%d'),
            "end-date":previousQuaterEndDate.strftime('%Y-%m-%d'),
            "total-income": sum
        }

    return Response(data=data,status=status.HTTP_200_OK)



'''
localhost:8000/drchronoinsurance/live-claim-fields
you need to get the live claim
live claims will be only get if user has see line 567 where quering different status
we can also change the status of it by using put request
'''
@api_view(['GET',"PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def live_claim_fields(request):
    if request.method == 'GET':
        method = request.GET.get('method',None)
        from_date = request.GET.get('from-date',None)
        to_date = request.GET.get('to-date',None)

        if method is None or from_date is None or to_date is None:
            objs = Billing.objects.filter(Q(status='Settled')|Q(status='Internal Review')|Q(status='Bill Insurance')|Q(status='Bill Secondary Insurance')|Q(status="Worker's Comp Claim")|Q(status="Auto Accident Claim")|Q(status="Durable Medical Equipment Claim"))

            serializer = BillingSerializer(objs,many=True)

            data={
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_200_OK)
        else:
            from_date = datetime.strptime(from_date,'%d/%m/%Y')-timedelta(days=1)
            to_date = datetime.strptime(to_date,'%d/%m/%Y')+timedelta(days=1)

            objs = Billing.objects.filter(creation_date__range=[from_date,to_date])
            obj_list = []

            for obj in objs:
                sum=0
                for i in obj.payment.all():
                    sum+=i.amount
                obj_list.append(
                    {
                    "billing_info":BillingSerializer(obj).data,
                    "billed": sum
                    }
                )

            data={
                "status":"ok",
                "message":"successfull",
                "data":obj_list
            }
            return Response(data=data,status=status.HTTP_200_OK)


# if the user needs to change the multiple status at the same time

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def batchStatusChange(request):
    data = json.loads(request.body)

    claim_list = data.get('claim-list',None)
    claim_status = data.get('claim-status',None)

    if claim_list is None:
        data={
            "status":"error",
            "message":"Empty List"
            }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)

    claim_list = list(claim_list)
    claim_status = int(claim_status)


    objs = Billing.objects.filter(fhir_claim_id__in=claim_list)
    claim_obj = FHIRClaim()
    for obj in objs:
        if claim_status == 1:
            obj.status = 'Paid In Full'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 2:
            obj.status = 'Balance Due'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 3:
            obj.status = 'Settled'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 4:
            obj.status = 'Internal Review'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 5:
            obj.status = 'Bill Insurance'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 6:
            obj.status = 'Bill Secondary Insurance'
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 7:
            obj.status = "Worker's Comp Claim"
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 8:
            obj.status = "Auto Accident Claim"
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        if claim_status == 9:
            obj.status = "Durable Medical Equipment Claim"
            loop.run_until_complete(claim_obj.updateClaimStatus(obj.fhir_claim_id,"entered-in-error"))
        loop.close()
        obj.save()
    print(objs[0].status)
    data={
        "status":"ok",
        "message":"Successfull",
        "status":objs[0].status
        }
    return Response(data=data,status=status.HTTP_200_OK)


'''
to get all the patient payment and update the patient patients
'''
@api_view(['GET',"PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patient_payments(request):
    if request.method == 'GET':

        from_date = request.GET.get('from_date',None)
        to_date = request.GET.get('to_date',None)
        from_range = request.GET.get('from_range',None)
        to_range = request.GET.get('to_range',None)


        if from_date is not None and to_date is not None:
            print('this is running')
            from_date = datetime.strptime(from_date,'%d/%m/%Y')-timedelta(days=1)
            to_date = datetime.strptime(to_date,'%d/%m/%Y')-timedelta(days=1)
            objs = Billing.objects.filter(Q(status='Balance Due')&Q(creation_date__range=[from_date,to_date])|Q(status='Paid In Full')&Q(creation_date__range=[from_date,to_date]))
        else:
            objs = Billing.objects.filter(Q(status='Paid In Full')|Q(status='Balance Due'))

        appointment_balance = 0
        total_bill = 0
        unallocated_balance = 0
        current_patient_response = 0

        obj_list = []

        for obj in objs:
            for payment in obj.payment.all():
                if payment.type.id == 1:
                    appointment_balance+=payment.amount
            for cpt_code in obj.cpt_code.all():
                total_bill += cpt_code.price * cpt_code.quantity
            for hcpcs_code in obj.hcpcs_code.all():
                total_bill += hcpcs_code.price * hcpcs_code.quantity
            current_patient_response = appointment_balance - total_bill
            if current_patient_response > 0:
                current_patient_response=0
            serializer_obj = BillingSerializer(obj)
            if from_range is not None and to_range is not None:
                if float(total_bill)>= float(from_range) and float(total_bill)<=float(to_range):
                    obj_list.append(
                        {
                            "data":serializer_obj.data,
                            "appointment_balance":appointment_balance,
                            "total_bill":total_bill,
                            "unallocated_balance":unallocated_balance,
                            "current_patient_response":current_patient_response
                        }
                    )
                else:
                    pass
            else:
                obj_list.append(
                {
                    "data":serializer_obj.data,
                    "appointment_balance":appointment_balance,
                    "total_bill":total_bill,
                    "unallocated_balance":unallocated_balance,
                    "current_patient_response":current_patient_response
                }
            )
        data={
            "status":"ok",
            "message":"successfull",
            "data":obj_list
        }
        return Response(data=data,status=status.HTTP_200_OK)


'''
patient payments sub data
'''
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patient_payments_sub_data(request):
    id = request.GET.get('id',None)
    if id is None:
        data = {
            "status":"error",
            "message":"Invalid Id"
        }
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)
    billing_obj = Billing.objects.get(id=id)
    payments = billing_obj.payment.all()
    serializers = PaymentSerializer(payments,many=True)
    data = {
            "status":"ok",
            "message":"successfull",
            "patient": {
                "id":billing_obj.id,
                "first_name":billing_obj.patient.first_name,
                "second_name":billing_obj.patient.second_name,
                "third_name":billing_obj.patient.third_name,
            },
            "data":serializers.data
    }
    return Response(data=data,status=status.HTTP_200_OK)


# export the patient payment as csv

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def exportPatientPaymentToCsv(request):
    payment_id = request.GET.get('payment-id')
    billing_id = request.GET.get('billing-id')
    payment_list = payment_id.split(',')
    payment_obj = Payment.objects.filter(id__in=payment_list)
    file_name = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
    header = ['patient', 'Amount Paid', 'Payment Type', 'Payment Date','Appointment']
    url = f'media/csv_file/patient_payments/{file_name}.csv'

    billing_obj = Billing.objects.get(id=billing_id)


    f = open(url, 'w',encoding='UTF8')
    writer = csv.writer(f)
    writer.writerow(header)
    for item in payment_obj:
        row = []
        row.append(f'{billing_obj.patient.first_name} {billing_obj.patient.third_name}')
        row.append(item.amount)
        row.append(item.type.name)
        row.append(item.payment_date.strftime('%Y:%m:%d %H:%M:%S'))
        row.append(item.appointment.slot.start_time.strftime('%Y:%m:%d %H:%M:%S'))
        writer.writerow(row)
    f.close()
    data = {
        "status":"ok",
        "message":"successfull",
        "url":url,
        "file_name":file_name
    }
    return Response(data=data,status=status.HTTP_200_OK)


'''
check the eligibility of the patient insurance claim wheather the patient is eligible or not
this is implemented by the FHIR so once we will get the request from the frontend it will pass the request
to the FHIR server on the patient id if there is any eligiblity for the patient we will get the response

'''


# to update the eligibility
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateEligibility(request):
    if request.method == 'GET':
        coverage_id = request.GET.get('coverage_id',None)
        if coverage_id is None or len(coverage_id) == 0:
            data = {
                "status":"error",
                "message":"coverage_id is required!!!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        fhir_coverage = FHIRCoverage()
        response = fhir_coverage.updateCoverage(coverage_id=coverage_id)

        data= {
            "status":"ok",
            "message":"successfull",
            "data":response
        }
        return Response(data=data,status=status.HTTP_200_OK)
