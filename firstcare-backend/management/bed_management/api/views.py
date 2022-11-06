from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.bed_management.models import *
from rest_framework import status
from .serializers import *


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bed_tags(request):
    if request.method == "GET":
        tags = bedTags.objects.all()
        serializer = bedTagsSerializer(tags,many=True)

        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = bedTagsSerializer(data=request.data)
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
def bed_type(request):
    if request.method == "GET":
        type = bedType.objects.all()
        serializer = bedTypeSerializer(type,many=True)

        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = bedTypeSerializer(data=request.data)
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
def bed_layout(request):
    if request.method == 'GET':
        layout = BedLayout.objects.all()
        serializer = BedLayoutSerializer(layout,many=True)

        data = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = BedLayoutSerializer(data=request.data)
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