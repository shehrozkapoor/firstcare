from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import *
from.serializers import *

# usertype view to get all the usertypes we have in the database

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userType(request):
    query = UserType.objects.all()
    serializer = UserTypeSerializer(query,many=True)
    data={}
    data["status"]="ok"
    data["message"]="success"
    data["data"] = serializer.data
    return Response(data, status=status.HTTP_200_OK)

#we have implemented the HttpCookie only which the mostt secure way to store the Auth Token into the system.this method will give you the token for the login user.
@api_view(['GET'])
def getToken(request):
    data={}
    data["status"]="ok"
    data["message"]="success"
    try:
        data["data"] = {'token':request.COOKIES['token']}
    except:
        data["status"]="error"
        data["message"]="no token found"
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    data["status"]="ok"
    data["message"]="success"
    return Response(data, status=status.HTTP_200_OK)
