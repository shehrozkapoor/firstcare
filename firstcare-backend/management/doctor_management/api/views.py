from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.ward_management.models import *
from rest_framework import status
from .serializers import *
from FHIR.NAPHIES_FHIR_REQUEST.FHIRPractitioner import FHIRPractitioner
from FHIR.NAPHIES_FHIR_REQUEST.FHIRLocation import FHIRLocation
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

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def department(request):
    if request.method == 'GET':
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept,many=True)

        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            location = FHIRLocation()
            name = request.POST.get('name',None)
            print(name)
            response = loop.run_until_complete(location.createLocation(name))
            serializer.save(fhir_id=response.id)
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

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def doctor(request):
    if request.method == 'GET':
        doc = Doctor.objects.all()
        serializer = DoctorSerializer(doc,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            practititoner = FHIRPractitioner()
            name = serializer.validated_data.pop('name').split(' ')
            first_name = name[0]
            last_name = name[1]
            result = loop.run_until_complete(practititoner.createPractitioner(first_name=first_name,last_name=last_name,license_id='001NF'))
            serializer.save(fhir_practitioner_id=result['id'],name=name[0]+name[1])
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data,
            "fhir_response":result
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)