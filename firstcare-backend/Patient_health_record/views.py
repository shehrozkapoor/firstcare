from django.shortcuts import render




def index(request):
    return render(request,'patient_helath_care_record/homePage.html')