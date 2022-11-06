from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from Insurance.claims.models import *


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def claim_services(request):
    if request.method == 'GET':
        obj = ClaimServices.objects.all()
        serializer = ClaimServicesSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClaimServicesSerializer(data=request.data)
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
        claim_services_id = request.POST.get('claim_services_id',None)
        if claim_services_id is None:
            data = {
                "status":"error",
                "message":"claim_services_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ClaimServices.objects.get(id=claim_services_id)
        serializer = ClaimServicesSerializer(obj,data=request.data)
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
        claim_services_id = request.POST.get('claim_services_id',None)
        if claim_services_id is None:
            data = {
                "status":"error",
                "message":"claim_services_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ClaimServices.objects.get(id=claim_services_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def claim_items(request):
    if request.method == 'GET':
        obj = ClaimItems.objects.all()
        serializer = ClaimItemsSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClaimItemsSerializer(data=request.data)
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
        claim_items_id = request.POST.get('claim_items_id',None)
        if claim_items_id is None:
            data = {
                "status":"error",
                "message":"claim_items_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ClaimItems.objects.get(id=claim_items_id)
        serializer = ClaimItemsSerializer(obj,data=request.data)
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
        claim_items_id = request.POST.get('claim_items_id',None)
        if claim_items_id is None:
            data = {
                "status":"error",
                "message":"claim_items_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ClaimItems.objects.get(id=claim_items_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def claims(request):
    if request.method == 'GET':
        obj = Claims.objects.all()
        serializer = ClaimsSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClaimsSerializer(data=request.data)
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
        claim_items_id = request.POST.get('claim_items_id',None)
        if claim_items_id is None:
            data = {
                "status":"error",
                "message":"claim_items_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Claims.objects.get(id=claim_items_id)
        serializer = ClaimsSerializer(obj,data=request.data)
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
        claim_items_id = request.POST.get('claim_items_id',None)
        if claim_items_id is None:
            data = {
                "status":"error",
                "message":"claim_items_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Claims.objects.get(id=claim_items_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def review_claims(request):
    if request.method == 'GET':
        obj = Claims.objects.filter(submitted=True)
        serializer = ClaimsSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'PUT':
        claim_items_id = request.POST.get('claim_items_id',None)
        if claim_items_id is None:
            data = {
                "status":"error",
                "message":"claim_items_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Claims.objects.get(id=claim_items_id)
        serializer = ClaimsSerializer(obj,data=request.data)
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