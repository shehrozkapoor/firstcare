from django.db import models
from Laboratory.models import AvailableTests, SampleType
from Patient.models import GENDER, Patient

class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class Dictionary(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    active = models.BooleanField(default=False)
    entry = models.TextField(max_length=1500,null=False)
    local_abbreviation = models.CharField(max_length=100,null=False)


class OrganizationType(models.Model):
    name = models.CharField(max_length=100,null=False)

class Organization(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    short_name = models.CharField(max_length=100,null=True,blank=True)
    active = models.BooleanField(default=True)
    street_address = models.CharField(max_length=1000,null=True,blank=True)
    internet_address = models.CharField(max_length=1000,null=True,blank=True)
    type = models.ForeignKey(OrganizationType,on_delete=models.CASCADE,null=True,blank=True)
    nphies_id = models.CharField(max_length=1000,null=True,blank=True,unique=True)
    

class Panel(models.Model):
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=False)

class PanelItem(models.Model):
    panel = models.ForeignKey(Panel,on_delete=models.CASCADE,null=False)
    method = models.CharField(max_length=100,null=False)
    test = models.CharField(max_length=1000,null=False)
    sort_order = models.CharField(max_length=1000,null=False)


LIMIT_TYPE = (
    ('0','-----'),
    ('1','NUMERIC')
)


class ResultLimit(models.Model):
    test = models.ForeignKey(AvailableTests,on_delete=models.CASCADE,null=False)
    type = models.CharField(max_length=1,choices=LIMIT_TYPE,default='1',null=False)
    gender = models.CharField(max_length=7,choices=GENDER,null=True)
    age_min = models.CharField(max_length=20,null=True,blank=True)
    age_max = models.CharField(max_length=20,null=True,blank=True)
    normal_range_low = models.CharField(max_length=20,null=True,blank=True)
    normal_range_high = models.CharField(max_length=20,null=True,blank=True)
    valid_range_low = models.CharField(max_length=20,null=True,blank=True)
    valid_range_high = models.CharField(max_length=20,null=True,blank=True)

class SiteInformation(models.Model):
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=False)
    value = models.CharField(max_length=100,null=False)

class SampleEntryConfig(models.Model):
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=False)
    value = models.CharField(max_length=100,null=False)

class PrintedReportsConfig(models.Model):
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=False)
    value = models.CharField(max_length=100,null=False)


class TestResult(models.Model):
    test = models.ForeignKey(AvailableTests,on_delete=models.CASCADE,null=False)
    group = models.CharField(max_length=100,null=False)
    flags = models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=100,null=False)
    value = models.CharField(max_length=100,null=False)
    significant_digit = models.CharField(max_length=100,null=False)
    quant_limit = models.CharField(max_length=100,null=False)
    count_level = models.CharField(max_length=100,null=False)
    scriptlet = models.CharField(max_length=100,null=False)
    abnormal = models.BooleanField(default=False)
    status = models.BooleanField(null=True,blank=True)
    reffered_out = models.BooleanField(null=True,blank=True)
    note = models.CharField(max_length=1000,null=True,blank=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)


class SampleTypePanel(models.Model):
    sampletype = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=True,blank=True)
    panel = models.ForeignKey(Panel,on_delete=models.CASCADE,null=True,blank=True)

class SampleTypeTest(models.Model):
    sampletype = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=True,blank=True)
    test = models.ForeignKey(AvailableTests,on_delete=models.CASCADE,null=True,blank=True)