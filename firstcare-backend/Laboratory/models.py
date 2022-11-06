from django.db import models
from firstcare.settings import AUTH_USER_MODEL
from Patient.models import Patient
from management.doctor_management.models import Department, Doctor
from management.ward_management.models import Ward

'''
the commented models are the old implementation i have not completely delete this code because maybe
in future you need this but that's totaly depend on you wheather you keep it or delete it
'''
# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class TestResult(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)
#     specimen = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="specimen")
#     test_status = models.CharField(max_length=500,null=True,blank=True)
#     timestamp = models.DateTimeField(null=True,blank=True)
#     category_service = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE,null=True,blank=True)
#     clinical_information_provided = models.CharField(max_length=1000,null=True,blank=True)
#     result = models.CharField(max_length=1000,null=True,blank=True)
#     conclusion = models.CharField(max_length=500,null=True,blank=True)
#     test_diagnosis = models.CharField(max_length=100,null=True,blank=True)
#     structured_test_diagnosis = models.CharField(max_length=100,null=True,blank=True)
#     multimedia_representation = models.FileField(null=True,blank=True)
#     comment = models.CharField(max_length=500,null=True,blank=True)
#     requested_name = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="requested")
#     requestor = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="requestor")
#     reciever = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="reciever")
#     distribution_list = models.CharField(max_length=100,null=True,blank=True)


SAMPLE_TYPE = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
)

'''
unit of measure is the measurement unit
e.g
sec/min/milimeter/litre
'''
class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


'''
what type of sample has been collected by labortory
'''
class SampleType(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    domain = models.CharField(max_length=500,null=True,blank=True)
    local_abbrevation = models.CharField(max_length=500,null=True,blank=True)
    active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0,null=True,blank=True)

'''
which test are available that this laboratory can do.
'''
class AvailableTests(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    sampleType = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=False)
    active = models.BooleanField(default=True)
    measure_unit = models.ForeignKey(UnitOfMeasure,on_delete=models.CASCADE,null=True,blank=True)
    referred_out = models.BooleanField(default=True)

'''
which samples are collected for a specific patient

'''
class Sample(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    requestor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    recieved_date = models.DateField(null=True,blank=True)
    source_location = models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,blank=True)
    accession_number = models.CharField(max_length=50,null=True,blank=True,unique=True)
    tests = models.ManyToManyField(AvailableTests,related_name="tests")


'''
refusalReason if the sample is refused
'''
class refusalReason(models.Model):
    sample_type = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=True,blank=True)
    departmet = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    biologist = models.CharField(max_length=500,null=True,blank=True)
    note = models.CharField(max_length=500,null=True,blank=True)
    reason = models.CharField(max_length=100,null=True)

'''
Non Conformity
'''
class NonConformity(models.Model):
    sample = models.ForeignKey(Sample,on_delete=models.CASCADE,null=False)
    reason = models.ManyToManyField(refusalReason,related_name="resusal_reasons")
    comments = models.CharField(max_length=1000,null=True)