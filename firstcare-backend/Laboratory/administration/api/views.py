
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.schedule_management.views import *
from rest_framework import status
from Laboratory.administration.models import *
from .serializers import *
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def testConnection(request):
#     data = {
#         "satus":"ok",
#         "message":"successfull",
#     }
#     return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category(request):
    if request.method == 'GET':
        cat = Category.objects.all()
        serializer = CategorySerializers(cat,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CategorySerializers(data=request.data)
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
def dictionary(request):
    if request.method == 'GET':
        obj = Dictionary.objects.all()
        serializer = DictionarySerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DictionarySerializers(data=request.data)
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
def organization_type(request):
    if request.method == 'GET':
        obj = OrganizationType.objects.all()
        serializer = OrganizationTypeSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OrganizationTypeSerializers(data=request.data)
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
def organization(request):
    if request.method == 'GET':
        obj = Organization.objects.all()
        serializer = OrganizationSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OrganizationSerializers(data=request.data)
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
def panel(request):
    if request.method == 'GET':
        obj = Panel.objects.all()
        serializer = PanelSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PanelSerializers(data=request.data)
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
def panel_item(request):
    if request.method == 'GET':
        obj = PanelItem.objects.all()
        serializer = PanelItemSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PanelItemSerializers(data=request.data)
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
def result_limit(request):
    if request.method == 'GET':
        obj = ResultLimit.objects.all()
        serializer = ResultLimitSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ResultLimitSerializers(data=request.data)
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
def site_information(request):
    if request.method == 'GET':
        obj = SiteInformation.objects.all()
        serializer = SiteInformationSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SiteInformationSerializers(data=request.data)
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
def sample_entry_config(request):
    if request.method == 'GET':
        obj = SampleEntryConfig.objects.all()
        serializer = SampleEntryConfigSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SampleEntryConfigSerializers(data=request.data)
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
def printed_reports_config(request):
    if request.method == 'GET':
        obj = PrintedReportsConfig.objects.all()
        serializer = PrintedReportsConfigSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PrintedReportsConfigSerializers(data=request.data)
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


@api_view(['GET','POST','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_result(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id',None)
        dept_id = request.GET.get('department_id',None)
        reffered_out = request.GET.get('referred_out',None)

        if patient_id is not None:
            obj = TestResult.objects.filter(patient__pk=patient_id)
        elif dept_id is not None:
            obj = TestResult.objects.filter(patient__department__pk=dept_id)
        elif reffered_out is not None:
            obj = TestResult.objects.filter(reffered_out=reffered_out)
        else:
           obj = TestResult.objects.all()
        serializer = TestResultSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = TestResultSerializers(data=request.data)
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
        test_result_id = request.POST.get('test_result_id',None)
        if test_result_id is None:
            data = {
                "status":"error",
                "message":"test_result_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        try:
            obj = TestResult.objects.get(pk=test_result_id)
        except:
            data = {
                "status":"error",
                "message":"test_result not found!"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        serializer = TestResultSerializers(obj,data=request.data)
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
def sample_type_panel(request):
    if request.method == 'GET':
        obj = SampleTypePanel.objects.all()
        serializer = SampleTypePanelSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SampleTypePanelSerializers(data=request.data)
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
def sample_type_test(request):
    if request.method == 'GET':
        obj = SampleTypeTest.objects.all()
        serializer = SampleTypeTestSerializers(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SampleTypeTestSerializers(data=request.data)
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
