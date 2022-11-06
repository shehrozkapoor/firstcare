from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from management.schedule_management.views import *
from rest_framework import status
from .serializers import *
from Patient_health_record.models import *

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def dosage_instruction(request):
    if request.method == 'GET':
        instructions = DosageInstruction.objects.all()
        serializer = DosageInstructionSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DosageInstructionSerializer(data=request.data)
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
        instructions = RelationShip.objects.all()
        serializer = RelationShipSerializer(instructions,many=True)
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
def encounter_type(request):
    if request.method == 'GET':
        instructions = EncounterType.objects.all()
        serializer = EncounterTypeSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = EncounterTypeSerializer(data=request.data)
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
def chief_complain(request):
    if request.method == 'GET':
        instructions = ChiefComplain.objects.all()
        serializer = ChiefComplainSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ChiefComplainSerializer(data=request.data)
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
def vital_signs(request):
    if request.method == 'GET':
        instructions = VitalSigns.objects.all()
        serializer = VitalSignsSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = VitalSignsSerializer(data=request.data)
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
def problems(request):
    if request.method == 'GET':
        instructions = Problems.objects.all()
        serializer = ProblemsSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProblemsSerializer(data=request.data)
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
def problem_list(request):
    if request.method == 'GET':
        instructions = ProblemList.objects.all()
        serializer = ProblemListSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProblemListSerializer(data=request.data)
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
def document(request):
    if request.method == 'GET':
        instructions = Document.objects.all()
        serializer = DocumentSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
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
def history_type(request):
    if request.method == 'GET':
        instructions = HistoryType.objects.all()
        serializer = HistoryTypeSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HistoryTypeSerializer(data=request.data)
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
def history(request):
    if request.method == 'GET':
        instructions = History.objects.all()
        serializer = HistorySerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = HistorySerializer(data=request.data)
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
def review_of_system(request):
    if request.method == 'GET':
        instructions = ReviewOfSystem.objects.all()
        serializer = ReviewOfSystemSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ReviewOfSystemSerializer(data=request.data)
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
def physical_exam(request):
    if request.method == 'GET':
        instructions = PhysicalExam.objects.all()
        serializer = PhysicalExamSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PhysicalExamSerializer(data=request.data)
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
def order(request):
    if request.method == 'GET':
        instructions = Order.objects.all()
        serializer = OrderSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
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
def assessment_and_plan(request):
    if request.method == 'GET':
        instructions = AssessmentAndPlan.objects.all()
        serializer = AssessmentAndPlanSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = AssessmentAndPlanSerializer(data=request.data)
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
def progress_note(request):
    if request.method == 'GET':
        instructions = ProgressNote.objects.all()
        serializer = ProgressNoteSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProgressNoteSerializer(data=request.data)
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
def encounter(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id',None)
        if patient_id is None:
            data={
                "status":"error",
                "message":"patient_id is required!"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        instructions = Encounter.objects.filter(patient__pk=patient_id)
        serializer = EncounterSerializer(instructions,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }  
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = EncounterSerializer(data=request.data)
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