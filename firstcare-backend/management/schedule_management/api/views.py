from datetime import timedelta
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.doctor_management.api.serializers import DoctorSerializer
from management.schedule_management.views import *
from rest_framework import status
from .serializers import *


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def appointmentType(request):
    if request.method == 'GET':
        type = AppointmentType.objects.all()
        serializer = AppointmentTypeSerializer(type,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = AppointmentTypeSerializer(data=request.data)
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
def providerAvail(request):
    if request.method == 'GET':
        type = ProviderAvail.objects.all()
        serializer = ProviderAvailSerializer(type,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProviderAvailSerializer(data=request.data)
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
def appointment(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id','')
        if len(patient_id) == 0:
            appoint = Appointment.objects.all()
        else:
            appoint = Appointment.objects.filter(patient__pk=patient_id)

        serializer = AppointmentSerializer(appoint,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
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
def findSlots(request):
    if request.method == 'GET':
        appointment_type = request.GET.get('appointment_type',None)
        if appointment_type is None:
            data  = {
                "status":"error",
                "message":"appointment_type is required",
                }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        type = AppointmentType.objects.get(pk=appointment_type)
        slots = Slot.objects.filter(provider__available_types__in=[type])
        filtered_slots= []
        for slot in slots:
            appointment = Appointment.objects.filter(slot__id=slot.id).count()
            if appointment < 3:
                filtered_slots.append(slot)
        serializer = SlotSerializer(filtered_slots,many=True)
        data={
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
