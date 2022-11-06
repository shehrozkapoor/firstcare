from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from rest_framework import status


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def insurance_user_permissions(request):
    if request.method == 'GET':
        user = InsuranceUserPermision.objects.all()
        serializer = InsuranceUserPermisionSerializer(user,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceUserPermisionSerializer(data=request.data)
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
def insurance_user_roles(request):
    if request.method == 'GET':
        user = InsuranceUserRoles.objects.all()
        serializer = InsuranceUserRolesSerializer(user,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceUserRolesSerializer(data=request.data)
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
def insurance_user(request):
    if request.method == 'GET':
        user = InsuranceUser.objects.all()
        serializer = InsuranceUserSerializer(user,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceUserSerializer(data=request.data)
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
def family_type(request):
    if request.method == 'GET':
        family = FamilyType.objects.all()
        serializer = FamilyTypeSerializer(family,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = FamilyTypeSerializer(data=request.data)
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
def confirmation_type(request):
    if request.method == 'GET':
        type = ConfirmationType.objects.all()
        serializer = ConfirmationTypeSerializer(type,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ConfirmationTypeSerializer(data=request.data)
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
def family(request):
    if request.method == 'GET':
        family = Family.objects.all()
        serializer = FamilySerializer(family,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = FamilySerializer(data=request.data)
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
def relation_ship(request):
    if request.method == 'GET':
        relatioship = RelationShip.objects.all()
        serializer = RelationShipSerializer(relatioship,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RelationShipSerializer(data=request.data)
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
def profession(request):
    if request.method == 'GET':
        profession = Profession.objects.all()
        serializer = ProfessionSerializer(profession,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProfessionSerializer(data=request.data)
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
def education(request):
    if request.method == 'GET':
        education = Education.objects.all()
        serializer = EducationSerializer(education,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = EducationSerializer(data=request.data)
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
def id_type(request):
    if request.method == 'GET':
        id_type = IdType.objects.all()
        serializer = IdTypeSerializer(id_type,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = IdTypeSerializer(data=request.data)
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
def head_insuree(request):
    if request.method == 'GET':
        insurance = HeadInsuree.objects.all()
        serializer = HeadInsureeSerializer(insurance,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HeadInsureeSerializer(data=request.data)
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
def health_facility_level(request):
    if request.method == 'GET':
        level = HealthFacilityLevel.objects.all()
        serializer = HealthFacilityLevelSerializer(level,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HealthFacilityLevelSerializer(data=request.data)
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
def health_facility(request):
    if request.method == 'GET':
        samp = HealthFacility.objects.all()
        serializer = HealthFacilitySerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HealthFacilitySerializer(data=request.data)
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
def first_service_point(request):
    if request.method == 'GET':
        samp = FirstServicePoint.objects.all()
        serializer = FirstServicePointSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = FirstServicePointSerializer(data=request.data)
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
def insurance(request):
    if request.method == 'GET':
        samp = Insurance.objects.all()
        serializer = InsuranceSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = InsuranceSerializer(data=request.data)
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
def insuree(request):
    if request.method == 'GET':
        samp = Insuree.objects.all()
        serializer = InsureeSerializer(samp,many=True)
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

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def products(request):
    if request.method == 'GET':
        samp = Products.objects.all()
        serializer = ProductsSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
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
def policy_details(request):
    if request.method == 'GET':
        samp = PolicyDetails.objects.all()
        serializer = PolicyDetailsSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PolicyDetailsSerializer(data=request.data)
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
def deductable(request):
    if request.method == 'GET':
        samp = Deductable.objects.all()
        serializer = DeductableSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DeductableSerializer(data=request.data)
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
def remunerated(request):
    if request.method == 'GET':
        samp = Remunerated.objects.all()
        serializer = RemuneratedSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RemuneratedSerializer(data=request.data)
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
def policies(request):
    if request.method == 'GET':
        samp = Policies.objects.all()
        serializer = PoliciesSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PoliciesSerializer(data=request.data)
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
def policies_values(request):
    if request.method == 'GET':
        samp = PoliciesValues.objects.all()
        serializer = PoliciesValuesSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PoliciesValuesSerializer(data=request.data)
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
def payment_type(request):
    if request.method == 'GET':
        samp = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(samp,many=True)
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

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contribution_category(request):
    if request.method == 'GET':
        samp = ContributionCategory.objects.all()
        serializer = ContributionCategorySerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ContributionCategorySerializer(data=request.data)
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

@api_view(['GET','POST','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contribution(request):
    if request.method == 'GET':
        samp = Contribution.objects.all()
        serializer = ContributionSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ContributionSerializer(data=request.data)
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
        contribution_id = request.POST.get('contribution_id',None)
        if contribution_id is None:
            data  = {
            "status":"error",
            "message":"contribution_id is required!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        contribution = Contribution.objects.get(pk=contribution_id)
        contribution.delete()
        data  = {
            "status":"ok",
            "message":"successfully deleted!"
            }
        return Response(data=data,status=status.HTTP_200_OK)



@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def legal_form(request):
    if request.method == 'GET':
        samp = LegalForm.objects.all()
        serializer = LegalFormSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = LegalFormSerializer(data=request.data)
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
def activity_code(request):
    if request.method == 'GET':
        samp = ActivityCode.objects.all()
        serializer = ActivityCodeSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ActivityCodeSerializer(data=request.data)
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
def policy_holders(request):
    if request.method == 'GET':
        samp = PolicyHolders.objects.all()
        serializer = PolicyHoldersSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PolicyHoldersSerializer(data=request.data)
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
def contract(request):
    if request.method == 'GET':
        samp = Contract.objects.all()
        serializer = ContractSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ContractSerializer(data=request.data)
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
def diagnosis(request):
    if request.method == 'GET':
        samp = Diagnosis.objects.all()
        serializer = DiagnosisSerializer(samp,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DiagnosisSerializer(data=request.data)
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