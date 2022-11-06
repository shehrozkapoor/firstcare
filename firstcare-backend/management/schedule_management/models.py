from django.db import models
from management.outpatient_management.clinic_management.models import Clinic
from management.doctor_management.models import Doctor
from Patient.models import Patient

'''
Appointment type will have duration
e.g
60 minutes 30minutes e.t.c
'''

class AppointmentType(models.Model):
    type = models.CharField(max_length=100,null=True,blank=True)
    duration = models.CharField(max_length=10,null=True)
    description = models.CharField(max_length=1000,null=True,blank=True)


'''
doctor will have a different timing and according to the appointment type the doctor time will be divided into time slot

'''
class ProviderAvail(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=False,related_name="provider")
    start_date= models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    time_slot_length = models.CharField(max_length=100,null=True,blank=True)
    available_types = models.ManyToManyField(AppointmentType,related_name="available_types")



'''
slots that are available
'''
class Slot(models.Model):
    provider = models.ForeignKey(ProviderAvail,on_delete=models.CASCADE,null=True,related_name="doctor_avail")
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)


'''
appointment that will be schedule for a patient
'''
class Appointment(models.Model):
    date_time = models.DateTimeField(null=False)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE,null=True)
    type = models.ForeignKey(AppointmentType,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    checkin = models.DateTimeField(null=True,blank=True)
    checkout = models.DateTimeField(null=True,blank=True)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE,null=True,related_name="slot")
