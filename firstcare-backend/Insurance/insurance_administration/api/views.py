from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from Insurance.insurance_administration.models import *


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def region(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RegionSerializer(data=request.data)
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
        region_id = request.POST.get('region_id',None)
        if region_id is None:
            data = {
                "status":"error",
                "message":"region_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        region = Region.objects.get(id=region_id)
        serializer = RegionSerializer(region,data=request.data)
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
        region_id = request.POST.get('region_id',None)
        if region_id is None:
            data = {
                "status":"error",
                "message":"region_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        region = Region.objects.get(id=region_id)
        region.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def district(request):
    if request.method == 'GET':
        dist = District.objects.all()
        serializer = DistrictSerializer(dist,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DistrictSerializer(data=request.data)
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
        district_id = request.POST.get('district_id',None)
        if district_id is None:
            data = {
                "status":"error",
                "message":"district_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        dist = District.objects.get(id=district_id)
        serializer = DistrictSerializer(dist,data=request.data)
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
        district_id = request.POST.get('district_id',None)
        if district_id is None:
            data = {
                "status":"error",
                "message":"district_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        dist = District.objects.get(id=district_id)
        dist.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def conversion(request):
    if request.method == 'GET':
        con = Conversion.objects.all()
        serializer = ConversionSerializer(con,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ConversionSerializer(data=request.data)
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
        conversion_id = request.POST.get('conversion_id',None)
        if conversion_id is None:
            data = {
                "status":"error",
                "message":"conversion_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        con = Conversion.objects.get(id=conversion_id)
        serializer = ConversionSerializer(con,data=request.data)
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
        conversion_id = request.POST.get('conversion_id',None)
        if conversion_id is None:
            data = {
                "status":"error",
                "message":"conversion_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        dist = District.objects.get(id=conversion_id)
        dist.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def treatment(request):
    if request.method == 'GET':
        treat = Treatment.objects.all()
        serializer = TreatmentSerializer(treat,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = TreatmentSerializer(data=request.data)
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
        treatment_id = request.POST.get('treatment_id',None)
        if treatment_id is None:
            data = {
                "status":"error",
                "message":"treatment_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        treat = Treatment.objects.get(id=treatment_id)
        serializer = TreatmentSerializer(treat,data=request.data)
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
        treatment_id = request.POST.get('treatment_id',None)
        if treatment_id is None:
            data = {
                "status":"error",
                "message":"treatment_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        treat = Treatment.objects.get(id=treatment_id)
        treat.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def insuree(request):
    if request.method == 'GET':
        obj = Insuree.objects.all()
        serializer = InsureeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsureeSerializer(data=request.data)
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
        insuree_id = request.POST.get('insuree_id',None)
        if insuree_id is None:
            data = {
                "status":"error",
                "message":"insuree_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Insuree.objects.get(id=insuree_id)
        serializer = InsureeSerializer(obj,data=request.data)
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
        insuree_id = request.POST.get('insuree_id',None)
        if insuree_id is None:
            data = {
                "status":"error",
                "message":"insuree_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Insuree.objects.get(id=insuree_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def policy(request):
    if request.method == 'GET':
        obj = Policy.objects.all()
        serializer = PolicySerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PolicySerializer(data=request.data)
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
        policy_id = request.POST.get('policy_id',None)
        if policy_id is None:
            data = {
                "status":"error",
                "message":"policy_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Policy.objects.get(id=policy_id)
        serializer = PolicySerializer(obj,data=request.data)
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
        policy_id = request.POST.get('policy_id',None)
        if policy_id is None:
            data = {
                "status":"error",
                "message":"policy_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Policy.objects.get(id=policy_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def extra_member_ceiling(request):
    if request.method == 'GET':
        obj = ExtraMemberCeiling.objects.all()
        serializer = ExtraMemberCeilingSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ExtraMemberCeilingSerializer(data=request.data)
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
        extra_member_ceiling_id = request.POST.get('extra_member_ceiling_id',None)
        if extra_member_ceiling_id is None:
            data = {
                "status":"error",
                "message":"extra_member_ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ExtraMemberCeiling.objects.get(id=extra_member_ceiling_id)
        serializer = ExtraMemberCeilingSerializer(obj,data=request.data)
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
        extra_member_ceiling_id = request.POST.get('extra_member_ceiling_id',None)
        if extra_member_ceiling_id is None:
            data = {
                "status":"error",
                "message":"extra_member_ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ExtraMemberCeiling.objects.get(id=extra_member_ceiling_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def maximum_ceiling(request):
    if request.method == 'GET':
        obj = MaximumCeiling.objects.all()
        serializer = MaximumCeilingSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MaximumCeilingSerializer(data=request.data)
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
        maximum_ceiling_id = request.POST.get('maximum_ceiling_id',None)
        if maximum_ceiling_id is None:
            data = {
                "status":"error",
                "message":"maximum_ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MaximumCeiling.objects.get(id=maximum_ceiling_id)
        serializer = MaximumCeilingSerializer(obj,data=request.data)
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
        maximum_ceiling_id = request.POST.get('maximum_ceiling_id',None)
        if maximum_ceiling_id is None:
            data = {
                "status":"error",
                "message":"maximum_ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MaximumCeiling.objects.get(id=maximum_ceiling_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def number(request):
    if request.method == 'GET':
        obj = Number.objects.all()
        serializer = NumberSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = NumberSerializer(data=request.data)
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
        number_id = request.POST.get('number_id',None)
        if number_id is None:
            data = {
                "status":"error",
                "message":"number_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Number.objects.get(id=number_id)
        serializer = NumberSerializer(obj,data=request.data)
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
        number_id = request.POST.get('number_id',None)
        if number_id is None:
            data = {
                "status":"error",
                "message":"number_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Number.objects.get(id=number_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ceiling(request):
    if request.method == 'GET':
        obj = Ceiling.objects.all()
        serializer = CeilingSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CeilingSerializer(data=request.data)
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
        ceiling_id = request.POST.get('ceiling_id',None)
        if ceiling_id is None:
            data = {
                "status":"error",
                "message":"ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Ceiling.objects.get(id=ceiling_id)
        serializer = CeilingSerializer(obj,data=request.data)
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
        ceiling_id = request.POST.get('ceiling_id',None)
        if ceiling_id is None:
            data = {
                "status":"error",
                "message":"ceiling_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Ceiling.objects.get(id=ceiling_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def distribution(request):
    if request.method == 'GET':
        obj = Distribution.objects.all()
        serializer = DistributionSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DistributionSerializer(data=request.data)
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
        distribution_id = request.POST.get('distribution_id',None)
        if distribution_id is None:
            data = {
                "status":"error",
                "message":"distribution_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Distribution.objects.get(id=distribution_id)
        serializer = DistributionSerializer(obj,data=request.data)
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
        distribution_id = request.POST.get('distribution_id',None)
        if distribution_id is None:
            data = {
                "status":"error",
                "message":"distribution_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Distribution.objects.get(id=distribution_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def level(request):
    if request.method == 'GET':
        obj = Level.objects.all()
        serializer = LevelSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = LevelSerializer(data=request.data)
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
        level_id = request.POST.get('level_id',None)
        if level_id is None:
            data = {
                "status":"error",
                "message":"level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Level.objects.get(id=level_id)
        serializer = LevelSerializer(obj,data=request.data)
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
        level_id = request.POST.get('level_id',None)
        if level_id is None:
            data = {
                "status":"error",
                "message":"level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Level.objects.get(id=level_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sub_level(request):
    if request.method == 'GET':
        obj = SubLevel.objects.all()
        serializer = SubLevelSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SubLevelSerializer(data=request.data)
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
        sub_level_id = request.POST.get('sub_level_id',None)
        if sub_level_id is None:
            data = {
                "status":"error",
                "message":"sub_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = SubLevel.objects.get(id=sub_level_id)
        serializer = SubLevelSerializer(obj,data=request.data)
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
        sub_level_id = request.POST.get('sub_level_id',None)
        if sub_level_id is None:
            data = {
                "status":"error",
                "message":"sub_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = SubLevel.objects.get(id=sub_level_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def capitation_payment(request):
    if request.method == 'GET':
        obj = CapitationPayment.objects.all()
        serializer = CapitationPaymentSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CapitationPaymentSerializer(data=request.data)
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
        capitation_id = request.POST.get('capitation_id',None)
        if capitation_id is None:
            data = {
                "status":"error",
                "message":"capitation_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CapitationPayment.objects.get(id=capitation_id)
        serializer = CapitationPaymentSerializer(obj,data=request.data)
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
        capitation_id = request.POST.get('capitation_id',None)
        if capitation_id is None:
            data = {
                "status":"error",
                "message":"capitation_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CapitationPayment.objects.get(id=capitation_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
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
        product_id = request.POST.get('product_id',None)
        if product_id is None:
            data = {
                "status":"error",
                "message":"product_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Product.objects.get(id=product_id)
        serializer = ProductSerializer(obj,data=request.data)
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
        product_id = request.POST.get('product_id',None)
        if product_id is None:
            data = {
                "status":"error",
                "message":"product_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Product.objects.get(id=product_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def health_facility_legal_form(request):
    if request.method == 'GET':
        obj = HealthFacilityLegalForm.objects.all()
        serializer = HealthFacilityLegalFormSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HealthFacilityLegalFormSerializer(data=request.data)
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
        health_facility_legal_form_id = request.POST.get('health_facility_legal_form_id',None)
        if health_facility_legal_form_id is None:
            data = {
                "status":"error",
                "message":"health_facility_legal_form_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilityLegalForm.objects.get(id=health_facility_legal_form_id)
        serializer = HealthFacilityLegalFormSerializer(obj,data=request.data)
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
        health_facility_legal_form_id = request.POST.get('health_facility_legal_form_id',None)
        if health_facility_legal_form_id is None:
            data = {
                "status":"error",
                "message":"health_facility_legal_form_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilityLegalForm.objects.get(id=health_facility_legal_form_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def health_facility_sub_level(request):
    if request.method == 'GET':
        obj = HealthFacilitySubLevel.objects.all()
        serializer = HealthFacilitySubLevelSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HealthFacilitySubLevelSerializer(data=request.data)
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
        health_facility_sub_level_id = request.POST.get('health_facility_sub_level_id',None)
        if health_facility_sub_level_id is None:
            data = {
                "status":"error",
                "message":"health_facility_sub_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilitySubLevel.objects.get(id=health_facility_sub_level_id)
        serializer = HealthFacilitySubLevelSerializer(obj,data=request.data)
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
        health_facility_sub_level_id = request.POST.get('health_facility_sub_level_id',None)
        if health_facility_sub_level_id is None:
            data = {
                "status":"error",
                "message":"health_facility_sub_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilitySubLevel.objects.get(id=health_facility_sub_level_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def care_type(request):
    if request.method == 'GET':
        obj = CareType.objects.all()
        serializer = CareTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CareTypeSerializer(data=request.data)
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
        care_type_id = request.POST.get('care_type_id',None)
        if care_type_id is None:
            data = {
                "status":"error",
                "message":"care_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CareType.objects.get(id=care_type_id)
        serializer = CareTypeSerializer(obj,data=request.data)
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
        care_type_id = request.POST.get('care_type_id',None)
        if care_type_id is None:
            data = {
                "status":"error",
                "message":"care_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CareType.objects.get(id=care_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def services_price_list(request):
    if request.method == 'GET':
        obj = ServicesPriceList.objects.all()
        serializer = ServicesPriceListSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ServicesPriceListSerializer(data=request.data)
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
        services_price_list_id = request.POST.get('services_price_list_id',None)
        if services_price_list_id is None:
            data = {
                "status":"error",
                "message":"services_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServicesPriceList.objects.get(id=services_price_list_id)
        serializer = ServicesPriceListSerializer(obj,data=request.data)
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
        services_price_list_id = request.POST.get('services_price_list_id',None)
        if services_price_list_id is None:
            data = {
                "status":"error",
                "message":"services_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServicesPriceList.objects.get(id=services_price_list_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def item_price_list(request):
    if request.method == 'GET':
        obj = ItemPriceList.objects.all()
        serializer = ItemPriceListSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ItemPriceListSerializer(data=request.data)
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
        item_price_list_id = request.POST.get('item_price_list_id',None)
        if item_price_list_id is None:
            data = {
                "status":"error",
                "message":"item_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ItemPriceList.objects.get(id=item_price_list_id)
        serializer = ItemPriceListSerializer(obj,data=request.data)
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
        item_price_list_id = request.POST.get('item_price_list_id',None)
        if item_price_list_id is None:
            data = {
                "status":"error",
                "message":"item_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ItemPriceList.objects.get(id=item_price_list_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def health_facilities(request):
    if request.method == 'GET':
        obj = HealthFacilities.objects.all()
        serializer = HealthFacilitiesSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HealthFacilitiesSerializer(data=request.data)
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
        health_facilities_id = request.POST.get('health_facilities_id',None)
        if health_facilities_id is None:
            data = {
                "status":"error",
                "message":"health_facilities_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilities.objects.get(id=health_facilities_id)
        serializer = HealthFacilitiesSerializer(obj,data=request.data)
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
        health_facilities_id = request.POST.get('health_facilities_id',None)
        if health_facilities_id is None:
            data = {
                "status":"error",
                "message":"health_facilities_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = HealthFacilities.objects.get(id=health_facilities_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def service_type(request):
    if request.method == 'GET':
        obj = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ServiceTypeSerializer(data=request.data)
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
        service_type_id = request.POST.get('service_type_id',None)
        if service_type_id is None:
            data = {
                "status":"error",
                "message":"service_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceType.objects.get(id=service_type_id)
        serializer = ServiceTypeSerializer(obj,data=request.data)
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
        service_type_id = request.POST.get('service_type_id',None)
        if service_type_id is None:
            data = {
                "status":"error",
                "message":"service_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceType.objects.get(id=service_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def service_category(request):
    if request.method == 'GET':
        obj = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ServiceCategorySerializer(data=request.data)
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
        service_category_id = request.POST.get('service_category_id',None)
        if service_category_id is None:
            data = {
                "status":"error",
                "message":"service_category_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceCategory.objects.get(id=service_category_id)
        serializer = ServiceCategorySerializer(obj,data=request.data)
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
        service_category_id = request.POST.get('service_category_id',None)
        if service_category_id is None:
            data = {
                "status":"error",
                "message":"service_category_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceCategory.objects.get(id=service_category_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def service_level(request):
    if request.method == 'GET':
        obj = ServiceLevel.objects.all()
        serializer = ServiceLevelSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ServiceLevelSerializer(data=request.data)
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
        service_level_id = request.POST.get('service_level_id',None)
        if service_level_id is None:
            data = {
                "status":"error",
                "message":"service_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceLevel.objects.get(id=service_level_id)
        serializer = ServiceLevelSerializer(obj,data=request.data)
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
        service_level_id = request.POST.get('service_level_id',None)
        if service_level_id is None:
            data = {
                "status":"error",
                "message":"service_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ServiceLevel.objects.get(id=service_level_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def medical_services(request):
    if request.method == 'GET':
        obj = MedicalServices.objects.all()
        serializer = MedicalServicesSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MedicalServicesSerializer(data=request.data)
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
        service_level_id = request.POST.get('service_level_id',None)
        if service_level_id is None:
            data = {
                "status":"error",
                "message":"service_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalServices.objects.get(id=service_level_id)
        serializer = MedicalServicesSerializer(obj,data=request.data)
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
        service_level_id = request.POST.get('service_level_id',None)
        if service_level_id is None:
            data = {
                "status":"error",
                "message":"service_level_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalServices.objects.get(id=service_level_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def item_type(request):
    if request.method == 'GET':
        obj = ItemType.objects.all()
        serializer = ItemTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ItemTypeSerializer(data=request.data)
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
        item_type_id = request.POST.get('item_type_id',None)
        if item_type_id is None:
            data = {
                "status":"error",
                "message":"item_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ItemType.objects.get(id=item_type_id)
        serializer = ItemTypeSerializer(obj,data=request.data)
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
        item_type_id = request.POST.get('item_type_id',None)
        if item_type_id is None:
            data = {
                "status":"error",
                "message":"item_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ItemType.objects.get(id=item_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def medical_item(request):
    if request.method == 'GET':
        obj = MedicalItem.objects.all()
        serializer = MedicalItemSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MedicalItemSerializer(data=request.data)
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
        medical_item_id = request.POST.get('medical_item_id',None)
        if medical_item_id is None:
            data = {
                "status":"error",
                "message":"medical_item_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalItem.objects.get(id=medical_item_id)
        serializer = MedicalItemSerializer(obj,data=request.data)
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
        medical_item_id = request.POST.get('medical_item_id',None)
        if medical_item_id is None:
            data = {
                "status":"error",
                "message":"medical_item_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalItem.objects.get(id=medical_item_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def medical_services_price_list(request):
    if request.method == 'GET':
        obj = MedicalServicesPriceList.objects.all()
        serializer = MedicalServicesPriceListSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MedicalServicesPriceListSerializer(data=request.data)
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
        medical_service_price_list_id = request.POST.get('medical_service_price_list_id',None)
        if medical_service_price_list_id is None:
            data = {
                "status":"error",
                "message":"medical_service_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalServicesPriceList.objects.get(id=medical_service_price_list_id)
        serializer = MedicalServicesPriceListSerializer(obj,data=request.data)
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
        medical_service_price_list_id = request.POST.get('medical_service_price_list_id',None)
        if medical_service_price_list_id is None:
            data = {
                "status":"error",
                "message":"medical_service_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalServicesPriceList.objects.get(id=medical_service_price_list_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def medical_items_price_list(request):
    if request.method == 'GET':
        obj = MedicalItemsPriceList.objects.all()
        serializer = MedicalItemsPriceListSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MedicalItemsPriceListSerializer(data=request.data)
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
        medical_item_price_list_id = request.POST.get('medical_item_price_list_id',None)
        if medical_item_price_list_id is None:
            data = {
                "status":"error",
                "message":"medical_item_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalItemsPriceList.objects.get(id=medical_item_price_list_id)
        serializer = MedicalItemsPriceListSerializer(obj,data=request.data)
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
        medical_item_price_list_id = request.POST.get('medical_item_price_list_id',None)
        if medical_item_price_list_id is None:
            data = {
                "status":"error",
                "message":"medical_item_price_list_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = MedicalItemsPriceList.objects.get(id=medical_item_price_list_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payer_type(request):
    if request.method == 'GET':
        obj = PayerType.objects.all()
        serializer = PayerTypeSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PayerTypeSerializer(data=request.data)
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
        payer_type_id = request.POST.get('payer_type_id',None)
        if payer_type_id is None:
            data = {
                "status":"error",
                "message":"payer_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PayerType.objects.get(id=payer_type_id)
        serializer = PayerTypeSerializer(obj,data=request.data)
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
        payer_type_id = request.POST.get('payer_type_id',None)
        if payer_type_id is None:
            data = {
                "status":"error",
                "message":"payer_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = PayerType.objects.get(id=payer_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def payer(request):
    if request.method == 'GET':
        obj = Payer.objects.all()
        serializer = PayerSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PayerSerializer(data=request.data)
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
        payer_id = request.POST.get('payer_id',None)
        if payer_id is None:
            data = {
                "status":"error",
                "message":"payer_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Payer.objects.get(id=payer_id)
        serializer = PayerSerializer(obj,data=request.data)
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
        payer_id = request.POST.get('payer_id',None)
        if payer_id is None:
            data = {
                "status":"error",
                "message":"payer_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Payer.objects.get(id=payer_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contribution_rules(request):
    if request.method == 'GET':
        obj = CalculationRules.objects.all()
        serializer = CalculationRulesSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CalculationRulesSerializer(data=request.data)
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
        calculation_rules_id = request.POST.get('calculation_rules_id',None)
        if calculation_rules_id is None:
            data = {
                "status":"error",
                "message":"calculation_rules_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CalculationRules.objects.get(id=calculation_rules_id)
        serializer = CalculationRulesSerializer(obj,data=request.data)
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
        calculation_rules_id = request.POST.get('calculation_rules_id',None)
        if calculation_rules_id is None:
            data = {
                "status":"error",
                "message":"calculation_rules_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = CalculationRules.objects.get(id=calculation_rules_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contribution_plan(request):
    if request.method == 'GET':
        obj = ContributionPlan.objects.all()
        serializer = ContributionPlanSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ContributionPlanSerializer(data=request.data)
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
        contribution_plan_id = request.POST.get('contribution_plan_id',None)
        if contribution_plan_id is None:
            data = {
                "status":"error",
                "message":"contribution_plan_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ContributionPlan.objects.get(id=contribution_plan_id)
        serializer = ContributionPlanSerializer(obj,data=request.data)
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
        contribution_plan_id = request.POST.get('contribution_plan_id',None)
        if contribution_plan_id is None:
            data = {
                "status":"error",
                "message":"contribution_plan_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = ContributionPlan.objects.get(id=contribution_plan_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

