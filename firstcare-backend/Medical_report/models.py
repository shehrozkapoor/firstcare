from tkinter import N
from django.db import models

# Create your models here.



'''
each medical summary will have Episodes
'''
class Episode(models.Model):
    onset_of_use = models.DateTimeField(null=True,blank=True)
    indication = models.CharField(max_length=100,null=True,blank=True)
    therapeutic_intent = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    details = models.TextField(max_length=1000,null=True,blank=True)
    cessation = models.DateTimeField(null=True,blank=True)
    reason_cessation = models.TextField(max_length=1000,null=True,blank=True)
    outcome = models.TextField(max_length=1000,null=True,blank=True)


'''
medical summary
'''
class MedicationSummary(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    clinical_indication = models.CharField(max_length=100,null=True,blank=True)
    onset_of_use = models.DateTimeField(null=True,blank=True)
    episode = models.ForeignKey(Episode,on_delete=models.CASCADE,null=True,blank=True)
    cumulative_dose = models.IntegerField(null=True,blank=True)
    cessation_use = models.DateTimeField(null=True,blank=True)
    cumulative_duration = models.IntegerField(null=True,blank=True)


