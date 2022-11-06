import imp
from re import I
from django.db import models
from firstcare.settings import AUTH_USER_MODEL
from management.ward_management.models import Ward


'''
there are different department in hospital
e.g
emergency,ICU,inpatient,outpatient,Dermatology e.t.c
'''
class Department(models.Model):
    fhir_id = models.CharField(unique=True,null=False,max_length=200)
    name= models.CharField(max_length=500,null=True,blank=True)


'''
each doctor will have a different department and doctor will be a user which will have roles and permissions
'''

class Doctor(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=False,db_constraint=False)
    name = models.CharField(max_length=500,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=False)
    specialization = models.CharField(max_length=500,null=True,blank=True)
    location = models.ManyToManyField(Ward,related_name="doctor_location",blank=True)
    practice_code = models.CharField(max_length=100,null=True,blank=True)
    fhir_practitioner_id = models.CharField(max_length=200,null=True,blank=True)