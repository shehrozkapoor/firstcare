from django.db import models
from management.doctor_management.models  import Doctor


'''
there will different clinics and each clinic will have different doctor
'''
class Clinic(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=False,related_name="clinic_doctor")