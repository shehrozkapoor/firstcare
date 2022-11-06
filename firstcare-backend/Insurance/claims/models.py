from django.db import models
from Insurance.insurance_administration.models import HealthFacilities,MedicalServices,MedicalItem,HeadInsuree,Diagnosis
from Insurance.models import InsuranceUser


CLAIM_STATUS = (
    ('ANY','ANY'),
    ('ENTERED','ENTERED'),
    ('REJECTED','REJECTED'),
    ('CHECKED','CHECKED'),
    ('PROCESSED','PROCESSED'),
    ('VALUATED','VALUATED'),
)

REVIEW_STATUS = (
    ('NOT SELECTED','NOT SELECTED'),
    ('SELECTED','SELECTED'),
    ('BYPASSED','BYPASSED'),
)
FEEDBACK_STATUS = (
    ('NOT SELECTED','NOT SELECTED'),
    ('SELECTED','SELECTED'),
    ('DELIVERED','DELIVERED'),
    ('BYPASSED','BYPASSED'),
)

VISIT_TYPE = (
    ('ANY','ANY'),
    ('EMERGENCY','EMERGENCY'),
    ('OTHER','OTHER'),
    ('REFERAL','REFERAL'),
)

class ClaimServices(models.Model):
    medical_service = models.ForeignKey(MedicalServices,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    explaination = models.CharField(max_length=1000,null=True,blank=True)

class ClaimItems(models.Model):
    medical_items = models.ForeignKey(MedicalItem,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    explaination = models.CharField(max_length=1000,null=True,blank=True)

class Claims(models.Model):
    health_facility = models.ForeignKey(HealthFacilities,on_delete=models.CASCADE,null=True,blank=True)
    insurance = models.ForeignKey(HeadInsuree,on_delete=models.CASCADE,null=True,blank=True)
    visit_date_from = models.DateField(null=True,blank=True)
    visit_date_to = models.DateField(null=True,blank=True)
    claimed_date = models.DateField(null=True,blank=True)
    visit_type = models.CharField(max_length=20,default='ANY',choices=VISIT_TYPE)
    main_diagnosis = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,null=True,blank=True,related_name="main_diagnosis")
    claim_num = models.CharField(max_length=100,null=True,blank=True)
    guarantee_num = models.CharField(max_length=100,null=True,blank=True)
    claimed_amount = models.IntegerField(null=True,blank=True)
    seg_dg_1 = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,null=True,blank=True,related_name="seg_dg_1")
    seg_dg_2 = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,null=True,blank=True,related_name="seg_dg_2")
    seg_dg_3 = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,null=True,blank=True,related_name="seg_dg_3")
    seg_dg_4 = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,null=True,blank=True,related_name="seg_dg_4")
    claim_administrator = models.ForeignKey(InsuranceUser,on_delete=models.CASCADE,null=True,blank=True)
    explaination = models.CharField(max_length=1000,null=True,blank=True)
    claim_status = models.CharField(max_length=20,default='ANY',choices=CLAIM_STATUS)
    feedback_status = models.CharField(max_length=20,default='SELECTED',choices=FEEDBACK_STATUS)
    review_status = models.CharField(max_length=20,default='SELECTED',choices=REVIEW_STATUS)
    medical_services = models.ManyToManyField(ClaimServices,related_name="claims_medical_services")
    medical_items = models.ManyToManyField(ClaimItems,related_name="claims_medical_items")
    submitted = models.BooleanField(default=False)