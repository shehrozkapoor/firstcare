from django.shortcuts import render
from rest_framework.authtoken.models import Token



def index(request):
    try:
        token = request.COOKIES['token']
    except:
        return render(request,'insurance/login.html')
        
    user = Token.objects.get(key=token).user
    return render(request,'insurance/base.html',{"user":user})

