from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.ward_management.models import *
from rest_framework import status
from .serializers import *
import nest_asyncio
import asyncio
from FHIR.NAPHIES_FHIR_REQUEST.FHIRLocation import FHIRLocation
from django.conf import settings

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
def room(request):
    if request.method == 'GET':
        room = Room.objects.all()
        serializer = RoomSerializer(room,many=True)

        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
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


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ward(request):
    if request.method == 'GET':
        hospital = request.GET.get('hospital',None)
        if hospital is None:
            locations = Ward.objects.all()
        else:
            locations = Ward.objects.filter(hospital__pk=hospital)
        serializer = WardSerializer(locations,many=True)
        data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = WardSerializer(data=request.data)
        
        if serializer.is_valid():
            fhir_location  = FHIRLocation()
            response = loop.run_until_complete(fhir_location.createLocation(organization_id=settings.NPHIES_ORGANIZATION_ID))
            serializer.save(fhir_location_id=response['id'])
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data,
            "fhir_response":response
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
def hospital(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals,many=True)
        data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HospitalSerializer(data=request.data)
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
