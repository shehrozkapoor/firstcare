import json
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from FHIR.NAPHIES_FHIR_REQUEST.constants import FHIR
from Patient_health_record.models import Encounter
from .serializers import *
from rest_framework import status
from billing.models import *
from FHIR.NAPHIES_FHIR_REQUEST.FHIRClaim import FHIRClaim
import asyncio
import nest_asyncio

try:
    nest_asyncio.apply()
except:
    pass

try:
    loop = asyncio.get_event_loop()
except:
    loop = asyncio.new_event_loop()


'''
CRUD operation on the payment type
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payment_type(request):
    if request.method == 'GET':

        obj = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PaymentTypeSerializer(data=request.data)
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
        payment_type_id = request.POST.get('payment_type_id',None)
        if payment_type_id is None:
            data = {
                "status":"error",
                "message":"payment_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentType.objects.get(id=payment_type_id)
        serializer = PaymentTypeSerializer(obj,data=request.data)
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
        payment_type_id = request.POST.get('payment_type_id',None)
        if payment_type_id is None:
            data = {
                "status":"error",
                "message":"payment_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentType.objects.get(id=payment_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the payment method
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payment_method(request):
    if request.method == 'GET':
        obj = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PaymentMethodSerializer(data=request.data)
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
        payment_method_id = request.POST.get('payment_method_id',None)
        if payment_method_id is None:
            data = {
                "status":"error",
                "message":"payment_method_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentMethod.objects.get(id=payment_method_id)
        serializer = PaymentMethodSerializer(obj,data=request.data)
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
        payment_method_id = request.POST.get('payment_method_id',None)
        if payment_method_id is None:
            data = {
                "status":"error",
                "message":"payment_method_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentMethod.objects.get(id=payment_method_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the payment
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payment(request):
    if request.method == 'GET':
        appointment_id = request.GET.get('appointment_id','')
        if len(appointment_id) == 0:
            obj = Payment.objects.all()
        else:
            obj = Payment.objects.filter(appointment__id=appointment_id)
        serializer = PaymentSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
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
        payment_id = request.POST.get('payment_id',None)
        if payment_id is None:
            data = {
                "status":"error",
                "message":"payment_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Payment.objects.get(id=payment_id)
        serializer = PaymentSerializer(obj,data=request.data)
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
        payment_id = request.POST.get('payment_id',None)
        if payment_id is None:
            data = {
                "status":"error",
                "message":"payment_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Payment.objects.get(id=payment_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

'''
CRUD operation on the payment profile
'''

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payment_profile(request):
    if request.method == 'GET':
        obj = PaymentProfile.objects.all()
        serializer = PaymentProfileSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PaymentProfileSerializer(data=request.data)
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
        payment_profile_id = request.POST.get('payment_profile_id',None)
        if payment_profile_id is None:
            data = {
                "status":"error",
                "message":"payment_profile_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentProfile.objects.get(id=payment_profile_id)
        serializer = PaymentProfileSerializer(obj,data=request.data)
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
        payment_profile_id = request.POST.get('payment_profile_id',None)
        if payment_profile_id is None:
            data = {
                "status":"error",
                "message":"payment_profile_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PaymentProfile.objects.get(id=payment_profile_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the onset datatype
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def onset_data_type(request):
    if request.method == 'GET':
        obj = OnsetDataType.objects.all()
        serializer = OnsetDataTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OnsetDataTypeSerializer(data=request.data)
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
        onset_data_type_id = request.POST.get('onset_data_type_id',None)
        if onset_data_type_id is None:
            data = {
                "status":"error",
                "message":"onset_data_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = OnsetDataType.objects.get(id=onset_data_type_id)
        serializer = OnsetDataTypeSerializer(obj,data=request.data)
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
        onset_data_type_id = request.POST.get('onset_data_type_id',None)
        if onset_data_type_id is None:
            data = {
                "status":"error",
                "message":"onset_data_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = OnsetDataType.objects.get(id=onset_data_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the otherdata type
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def other_data_type(request):
    if request.method == 'GET':
        obj = OtherDateType.objects.all()
        serializer = OtherDateTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OtherDateTypeSerializer(data=request.data)
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
        other_data_type_id = request.POST.get('other_data_type_id',None)
        if other_data_type_id is None:
            data = {
                "status":"error",
                "message":"other_data_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = OtherDateType.objects.get(id=other_data_type_id)
        serializer = OtherDateTypeSerializer(obj,data=request.data)
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
        other_data_type_id = request.POST.get('other_data_type_id',None)
        if other_data_type_id is None:
            data = {
                "status":"error",
                "message":"other_data_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = OtherDateType.objects.get(id=other_data_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the hcfa_box
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hcfa_box(request):
    if request.method == 'GET':
        obj = HcfaBOX.objects.all()
        serializer = HcfaBOXSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HcfaBOXSerializer(data=request.data)
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
        hcfa_box_id = request.POST.get('hcfa_box_id',None)
        if hcfa_box_id is None:
            data = {
                "status":"error",
                "message":"hcfa_box_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HcfaBOX.objects.get(id=hcfa_box_id)
        serializer = HcfaBOXSerializer(obj,data=request.data)
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
        hcfa_box_id = request.POST.get('hcfa_box_id',None)
        if hcfa_box_id is None:
            data = {
                "status":"error",
                "message":"hcfa_box_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HcfaBOX.objects.get(id=hcfa_box_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the ICD 10
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def icd_10(request):
    if request.method == 'GET':
        code = request.GET.get('code',None)
        if code is not None:
            obj = ICD10.objects.filter(code__icontains=code)
        else:
            obj = ICD10.objects.all()
        serializer = ICD10Serializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ICD10Serializer(data=request.data)
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
        icd_10_id = request.POST.get('icd_10_id',None)
        if icd_10_id is None:
            data = {
                "status":"error",
                "message":"icd_10_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ICD10.objects.get(id=icd_10_id)
        serializer = ICD10Serializer(obj,data=request.data)
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
        icd_10_id = request.POST.get('icd_10_id',None)
        if icd_10_id is None:
            data = {
                "status":"error",
                "message":"icd_10_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ICD10.objects.get(id=icd_10_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the ICD 9
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def icd_9(request):
    if request.method == 'GET':
        obj = ICD9.objects.all()
        serializer = ICD9Serializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ICD9Serializer(data=request.data)
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
        icd_9_id = request.POST.get('icd_9_id',None)
        if icd_9_id is None:
            data = {
                "status":"error",
                "message":"icd_9_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ICD9.objects.get(id=icd_9_id)
        serializer = ICD9Serializer(obj,data=request.data)
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
        icd_9_id = request.POST.get('icd_9_id',None)
        if icd_9_id is None:
            data = {
                "status":"error",
                "message":"icd_9_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ICD9.objects.get(id=icd_9_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)



'''
CRUD operation on the CPT ITEMS
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cpt_item(request):
    if request.method == 'GET':
        obj = CPTITEM.objects.all()
        serializer = CPTITEMSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CPTITEMSerializer(data=request.data)
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
        cpt_item_id = request.POST.get('cpt_item_id',None)
        if cpt_item_id is None:
            data = {
                "status":"error",
                "message":"cpt_item_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CPTITEM.objects.get(id=cpt_item_id)
        serializer = CPTITEMSerializer(obj,data=request.data)
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
        cpt_item_id = request.POST.get('cpt_item_id',None)
        if cpt_item_id is None:
            data = {
                "status":"error",
                "message":"cpt_item_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CPTITEM.objects.get(id=cpt_item_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)



'''
CRUD operation on the CPT CODES
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cpt_code(request):
    if request.method == 'GET':
        obj = CPTCODE.objects.all()
        serializer = CPTCODESerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CPTCODESerializer(data=request.data)
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
        cpt_code_id = request.POST.get('cpt_code_id',None)
        if cpt_code_id is None:
            data = {
                "status":"error",
                "message":"cpt_code_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CPTCODE.objects.get(id=cpt_code_id)
        serializer = CPTCODESerializer(obj,data=request.data)
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
        cpt_code_id = request.POST.get('cpt_code_id',None)
        if cpt_code_id is None:
            data = {
                "status":"error",
                "message":"cpt_code_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CPTCODE.objects.get(id=cpt_code_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

'''
CRUD operation on the HCPCS
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hcpcs(request):
    if request.method == 'GET':
        obj = HCPCS.objects.all()
        serializer = HCPCSSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HCPCSSerializer(data=request.data)
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
        hcpcs_id = request.POST.get('hcpcs_id',None)
        if hcpcs_id is None:
            data = {
                "status":"error",
                "message":"hcpcs_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCPCS.objects.get(id=hcpcs_id)
        serializer = HCPCSSerializer(obj,data=request.data)
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
        hcpcs_id = request.POST.get('hcpcs_id',None)
        if hcpcs_id is None:
            data = {
                "status":"error",
                "message":"hcpcs_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCPCS.objects.get(id=hcpcs_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the HCPCS CODES
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hcpcs_code(request):
    if request.method == 'GET':
        obj = HCPCSCODE.objects.all()
        serializer = HCPCSCODESerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HCPCSCODESerializer(data=request.data)
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
        hcpcs_code_id = request.POST.get('hcpcs_code_id',None)
        if hcpcs_code_id is None:
            data = {
                "status":"error",
                "message":"hcpcs_code_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCPCSCODE.objects.get(id=hcpcs_code_id)
        serializer = HCPCSCODESerializer(obj,data=request.data)
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
        hcpcs_code_id = request.POST.get('hcpcs_code_id',None)
        if hcpcs_code_id is None:
            data = {
                "status":"error",
                "message":"hcpcs_code_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HCPCSCODE.objects.get(id=hcpcs_code_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


'''
CRUD operation on the Billing
'''
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def billing(request):
    if request.method == 'GET':
        obj = Billing.objects.all()
        serializer = BillingSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        fhir_claim = FHIRClaim()
        response = ''
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid():
            appointment_id = serializer.validated_data.pop('appointment').id
            
            check_billing_present = Billing.objects.filter(appointment__id=appointment_id)
            
            
            encounter = Encounter.objects.get(appointment__id=appointment_id)
            
            payments = Payment.objects.filter(appointment__id=appointment_id)
            
            
            paid_ammount = 0
            for payment in payments:
                paid_ammount += float(payment.amount)
                
            icd_10 = serializer.validated_data.pop('icd_10_id')
            hcpcs = serializer.validated_data.pop('hcpcs_code_id')
            
            icd_10_list = []
            hcpcs_list = []
            
            unit_price = 0
            for id in list(icd_10[0].split(',')):
                obj = ICD10.objects.get(pk=id)
                icd_10_list.append(obj)
                unit_price+=obj.price
            
            for id in list(hcpcs[0].split(',')):
                print(id)
                obj = HCPCSCODE.objects.get(pk=id)
                hcpcs_list.append(obj)
                unit_price += obj.hcpcs_item.price*obj.quantity
            
            net_price=unit_price + ((15*unit_price)/100)
            
            if check_billing_present.count() > 0:
                data  = {
                "status":"error",
                "message":"Billing already present for this Appointment",
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                if serializer.validated_data['status'] == 'Bill Insurance':
                    fhir_claim = FHIRClaim()
                    fhir_constant = FHIR()
                    care_team = fhir_constant.createCareTeam(encounter.appointment.clinic.doctor)
                    diagnosis = fhir_constant.createDiagnosis(icd_10_list)
                    product_services = fhir_constant.createProductServices(hcpcs_list)
                    supporting_info = fhir_constant.createSupportingInfo(encounter.vital_sign.all())
                    
                    response = loop.run_until_complete(fhir_claim.sendClaim(patient_id=encounter.appointment.patient.document_id,net_price=net_price,unit_price=unit_price,claim_type="institutional-claim",sub_type="institutional",processPriority="normal",careTeams=care_team,supportingInfos=supporting_info,diagnosis=diagnosis,product_services=product_services,service_date=encounter.appointment.date_time.strftime('%Y-%m-%d')))

                    serializer.save(fhir_claim_id=response['id'],appointment=encounter.appointment,paid_amount=paid_ammount,total_amount=net_price,unit_amount=unit_price)
                    data  = {
                    "status":"ok",
                    "message":"successfull",
                    "data":serializer.data,
                    "fhir-response":response
                    }
                else:
                    serializer.save(paid_amount=paid_ammount,total_amount=net_price,unit_amount=unit_price)
                    data  = {
                    "status":"ok",
                    "message":"successfull",
                    "data":serializer.data,
                    }
                return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        billing_id = request.POST.get('billing_id',None)
        if billing_id is None:
            data = {
                "status":"error",
                "message":"billing_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Billing.objects.get(id=billing_id)
        serializer = BillingSerializer(obj,data=request.data)
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
        billing_id = request.POST.get('billing_id',None)
        if billing_id is None:
            data = {
                "status":"error",
                "message":"billing_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Billing.objects.get(id=billing_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

