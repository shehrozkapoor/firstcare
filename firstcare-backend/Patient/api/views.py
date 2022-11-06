import json
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import asyncio
import nest_asyncio
from drchrono_insurance.models import Insurance,InsuranceCompany

try:
    nest_asyncio.apply()
except:
    pass

try:
    loop = asyncio.get_event_loop()
except:
    loop = asyncio.new_event_loop()

'''
GET AND POST operation on the contact information
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contactInformation(request):
    if request.method == 'GET':
        instance = ContactInformation.objects.all()
        serializer = ContactInformationSerializer(instance,many=True)
        data = {}
        data['status'] = 'ok'
        data['message'] = 'successfull'
        data['data']=serializer.data
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ContactInformationSerializer(data=request.data)
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


'''
GET and POST request on the Patient
Note:
the post request is different because FHIR implementation in done this
see line 66 and 67
first we are creating the patient object in main database and once it will be stored their then
we are creating a patient in FHIR server
'''
@api_view(['GET','POST','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patient(request):
    if request.method == 'GET':
        document_id = request.GET.get('document_id',None)
        if document_id is not None:
            patients = Patient.objects.filter(document_id=document_id)
        else:
            patients = Patient.objects.all()
        serializer = PatientSerializer(patients,many=True)
        data = {}
        data['status'] = 'ok'
        data['message'] = 'successfull'
        data['data']=serializer.data
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            document_id = serializer.validated_data.pop('document_id')
            try:
                patient = Patient.objects.get(pk=document_id)
            except:
                serializer.save()
                patient = Patient.objects.get(pk=document_id)
                fhir_patient = FHIRPatient()
                response = loop.run_until_complete(fhir_patient.createPatient(data=patient))
                patient.fhir_id = response['id']
                patient.save()
                data  = {
                "status":"ok",
                "message":"successfull",
                "data":response
                }
                return Response(data=data,status=status.HTTP_201_CREATED)
            data  = {
            "status":"error",
            "message":"Patient Already Exist with this ID!!",
            }
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        document_id = request.GET.get('document_id',None)
        if document_id is None:
            data = {
                "status":"error",
                "message":"document_id is required for delete request!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        patient = Patient.objects.all()
        patient.delete()
        data  = {
            "status":"ok",
            "message":"successfull",
            }
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patientInsurance(request):
    if request.method == 'POST':
        serializer = PatientSerializerForInsurance(data=request.data)
        if serializer.is_valid():
            document_id = request.POST.get('document_id')
            try:
                patient = Patient.objects.get(pk=document_id)
            except:
                patient = serializer.save()
                fhir_patient = FHIRPatient()
                response = loop.run_until_complete(fhir_patient.createPatient(data=patient))
                patient.fhir_id = response['id']
                patient.save()
                data  = {
                "status":"ok",
                "message":"successfull",
                "data":serializer.data
                }
                return Response(data=data,status=status.HTTP_201_CREATED)
            data  = {
            "status":"error",
            "message":"Patient Already Exist with this ID!!",
            }
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        document_id = request.data.get('document_id',None)
        if document_id is None:
            data = {
                "status":"error",
                "message":"document_id is required for put request!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        patient = Patient.objects.get(pk=document_id)
        serializer = PatientSerializerForInsurance(patient,request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            data  = {
            "status":"error",
            "message":serializer.errors,
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_201_CREATED)





'''
get the specific pateint
'''


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getSpecificPatient(request):
    document_id = request.GET.get('document_id',None)
    first_name = request.GET.get('first_name',None)
    second_name = request.GET.get('second_name',None)
    file_id = request.GET.get('file_id',None)
    number = request.GET.get('number',None)
    start_date = request.GET.get('start_date',None)
    end_date = request.GET.get('end_date',None)
    insurance_plan = request.GET.get('insurance_plan',None)
    gender = request.GET.get('gender',None)
    data = {}
    patients = Patient.objects.filter(document_id=document_id)| Patient.objects.filter(file_id=file_id)| Patient.objects.filter(first_name=first_name)| Patient.objects.filter(second_name=second_name)| Patient.objects.filter(contact_info__phone_number=number)| Patient.objects.filter(DOB__gte=start_date)| Patient.objects.filter(DOB__lte=end_date)| Patient.objects.filter(insurance_plan=insurance_plan)| Patient.objects.filter(gender=gender)
    if len(patients)!=0:
        serializer = PatientSerializer(patients,many=True)
        data['status'] = 'ok'
        data['message'] = 'successfull'
        data['data']=serializer.data
        return Response(data=data,status=status.HTTP_200_OK)
    else:
        data['status'] = 'error'
        data['message'] = 'No Patient Found'
    return Response(data=data,status=status.HTTP_204_NO_CONTENT)


'''
patient list
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def patient_list(request):
    if request.method == 'GET':
        patient_lists = PatientList.objects.filter(user=request.user)
        serializer = PatientListSerializer(patient_lists,many=True)
        data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PatientListSerializer(data=request.data)
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

'''
search patient if you need any specific pateint
'''

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def searchPatient(request):
    if request.method == 'GET':
        document_id = request.GET.get('document_id','')
        if len(document_id) == 0:
            data ={
                "status":"error",
                "message":"document_id is required!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        patients = Patient.objects.filter(pk__startswith=document_id)
        serializer = PatientSerializer(patients,many=True)
        data = {}
        data['status'] = 'ok'
        data['message'] = 'successfull'
        data['data']=serializer.data
        return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getSearchInsurancePatient(request):
    if request.method == 'GET':
        patient_key = request.GET.get('PatientKey','')
        print(patient_key)
        if len(patient_key) < 10:
            data ={
                "TransactionName": "18f735cc-bb43-496e-9236-ef28951b31ae", 
                "ApiStatus": "Fail",
                "ErrorCode": "102",
                "ErrorDescription": "Identity number should be 10 digits", 
                "Insurance": None
                }
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
        data = {
            "TransactionName": "3ed3b0ef-e2f8-4de3-ad2c-6eb470c16fa2", 
            "ApiStatus": "Success",
            "ErrorCode": None,
            "ErrorDescription": None,
            "Insurance": [
                {
                "PolicyNumber": "19123472", 
                "InsuranceCompanyName": "Saudi National Insurance ", 
                "InsuranceCompanyNameAr":"ال رشكة للتأمي",
                "ClassName": "VVIP",
                "Gender": "Male",
                "DeductibleRate": "0",
                "MaxLimit": "100",
                "BeneficiaryType": "Dependent",
                "BeneficiaryTypeId": "2",
                "BeneficiaryNumber": "001066509223000",
                "IdentityNumber": "5555500005",
                "BeneficiaryName": "Test - Iliyas Pasha", 
                "InceptionDate": "07-01-2021",
                "PolicyHolder": "Saudi Tadawul Group", 
                "InsurancePolicyExpiryDate": "2022-08-09",
                }, 
                {
                "PolicyNumber": "19541234", 
                "InsuranceCompanyName": "Saudi National Insurance ", 
                "InsuranceCompanyNameAr":"ال رشكة للتأمي",
                "ClassName": "BC/A",
                "Gender": "Male",
                "DeductibleRate": "20",
                "MaxLimit": "0",
                "BeneficiaryType": "Dependent", 
                "BeneficiaryTypeId": "2",
                "BeneficiaryNumber": "001066509132101", 
                "IdentityNumber": "1110101111", 
                "BeneficiaryName": "Test - Iliyas Pasha", 
                "InceptionDate": "01-03-2020",
                "PolicyHolder": "State Properties General Authority", 
                "InsurancePolicyExpiryDate": "2022-09-28"
                } 
            ]
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == "POST":
        insurance_payload = request.data.get('insurance_payload','')
        patient_document_id = request.data.get('document_id','')
        
        if len(insurance_payload) == 0 or len(patient_document_id) == 0:
            data ={
                "status":"error",
                "message":"insurance_payload and document_id is required!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        patient = Patient.objects.get(document_id=patient_document_id)
        insurance_payload = json.loads(insurance_payload)
        
        insurance_exist_data = []
        count=0
        for obj in insurance_payload['Insurance']:
            try:
                Insurance.objects.get(patient=patient,policy_number=obj['PolicyNumber'])
                insurance_exist_data.append(count)
            except:
                insurance_obj = Insurance(patient=patient,policy_number=obj['PolicyNumber'],classname=obj['ClassName'],gender=obj['Gender'],DeductibleRate=obj['DeductibleRate'],MaxLimit=obj['MaxLimit'],BeneficiaryType=obj['BeneficiaryType'],BeneficiaryTypeId=obj['BeneficiaryTypeId'],BeneficiaryNumber=obj['BeneficiaryNumber'],IdentityNumber=obj['IdentityNumber'],BeneficiaryName=obj['BeneficiaryName'],InceptionDate=obj['InceptionDate'],PolicyHolder=obj['PolicyHolder'],InsurancePolicyExpiryDate=obj['InsurancePolicyExpiryDate'])
                try:
                    company = InsuranceCompany.objects.get(name=obj['InsuranceCompanyName'])
                except:
                    company = InsuranceCompany(name=obj['InsuranceCompanyName'],nameAr=obj['InsuranceCompanyNameAr'])
                    company.save()
                insurance_obj.company=company
                insurance_obj.save()
            count+=1
        print(insurance_exist_data)
        if len(insurance_exist_data) != 0:
            data ={
            "status":"error",
            "message":"\n".join(f"{insurance_payload['Insurance'][i]['PolicyNumber']} Policy Already Exist \n" for i in insurance_exist_data)
            }    
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
        data ={
            "status":"ok",
            "message":"successfull!"
        }
        return Response(data=data,status=status.HTTP_200_OK)