from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from management.outpatient_management.clinic_management.models import Clinic
from .serializers import *

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def clinic(request):
    if request.method == 'GET':
        cli = Clinic.objects.all()
        serializer = ClinicSerializer(cli,many=True)
        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClinicSerializer(data=request.data)
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
