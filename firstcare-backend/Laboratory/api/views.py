from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from management.schedule_management.views import *
from rest_framework import status
import random
from Laboratory.models import *



'''
every laboratory sample will have a accession number and this will generate a random number
'''
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generateAccessionNumber(request):
    range_start = 10**(8-1)
    range_end = (10**8)-1
    data = {
        "satus":"ok",
        "message":"successfull",
        "accession_number": f"{random.randint(range_start, range_end)}-{random.randint(100, 999)}"
    }
    return Response(data=data,status=status.HTTP_200_OK)

'''
to perform the GET AND POST for the sample
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sample(request):
    if request.method == 'GET':
        samp = Sample.objects.all()
        serializer = SampleSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SampleSerializer(data=request.data)
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
perform the operation on the  sample type
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sample_type(request):
    if request.method == 'GET':
        samp_type = SampleType.objects.all()
        serializer = SampleTypeSerializer(samp_type,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SampleTypeSerializer(data=request.data)
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
top perform the operation on the GET and POST request of the user on unit of measure
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def unit_of_measure(request):
    if request.method == 'GET':
        samp_type = UnitOfMeasure.objects.all()
        serializer = UnitOfMeasureSerializer(samp_type,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = UnitOfMeasureSerializer(data=request.data)
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
GET all the available test that laboratory can perform
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def available_tests(request):
    if request.method == 'GET':
        type_id = request.GET.get('type_id',None)
        if type_id is None:
            data  = {
            "status":"error",
            "message":"type_id is required!",
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        tests = AvailableTests.objects.filter(sampleType__pk=type_id)
        serializer = SampleTypeSerializer(tests,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = AvailableTestsSerializer(data=request.data)
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
refusal reason request
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def refusal_reason(request):
    if request.method == 'GET':
        obj = refusalReason.objects.all()
        serializer = refusalReasonSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = refusalReasonSerializer(data=request.data)
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
non_confirmity actions
'''
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def non_conformity(request):
    if request.method == 'GET':
        obj = NonConformity.objects.all()
        serializer = NonConformitySerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = NonConformitySerializer(data=request.data)
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
