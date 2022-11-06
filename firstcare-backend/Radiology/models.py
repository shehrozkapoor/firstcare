from django.db import models


# anatomical location
class AnatomicalLocation(models.Model):
    location = models.CharField(max_length=500,null=True,blank=True)

# examination details
class ExamiationDetails(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)

# imaging examination
class ImagingExamination(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    reason = models.CharField(max_length=500,null=True,blank=True)
    anatomical_location = models.ForeignKey(AnatomicalLocation,on_delete=models.CASCADE,null=True,blank=True)
    examiation_details = models.ForeignKey(ExamiationDetails,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=500,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)

