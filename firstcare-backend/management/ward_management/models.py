from django.db import models
from management.bed_management.models import *


'''
each ward will have many rooms
'''
class Room(models.Model):
    name = models.CharField(max_length=200,null=False)
    layout = models.ForeignKey(BedLayout,on_delete=models.CASCADE,null=False,db_constraint=False)

    def __str__(self):
        return self.name

'''
hospitals
'''

class Hospital(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True,unique=True)

'''
each hospital will have multiple wards
'''
class Ward(models.Model):
    name = models.CharField(max_length=200,null=False)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=False,db_constraint=False)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,null=False,db_constraint=False)
    fhir_location_id = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
