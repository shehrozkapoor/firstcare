from django.db import models
from Patient.models import Patient
from management.doctor_management.models import Doctor

class CoverageEligibilityBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    eligibility_request_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle_status = models.BooleanField(default=False)
    response_bundle = models.JSONField(null=True,blank=True)
    eligibility_response_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_eligibility_status = models.CharField(max_length=100,default="Requested")
    response_eligibility_description = models.CharField(max_length=1000,null=True,blank=True)
    
    response_eligibility_error = models.BooleanField(default=False)
    response_eligibility_error_description = models.CharField(max_length=1000,null=True,blank=True,default='')
    
    response_site_eligibility_status = models.CharField(max_length=1000,null=True,blank=True,default='')
    
    response_site_eligibility_not_inforce = models.CharField(max_length=1000,null=True,blank=True,default='')
    
    createdOn = models.DateTimeField(auto_now_add=True)
    
    beneficiary_coverage_id = models.CharField(max_length=1000,null=True,blank=True)

class PreAuthBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    pre_auth_request_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_bundle_status = models.BooleanField(default=False)
    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle = models.JSONField(null=True,blank=True)
    claim_response_id = models.CharField(max_length=100,null=True,blank=True)
    
    claim = models.ForeignKey("Claim",on_delete=models.CASCADE,null=True,blank=True)

class ClaimBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    claim_request_id = models.CharField(max_length=100,null=True,blank=True)

    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle_status = models.BooleanField(default=False)
    response_bundle = models.JSONField(null=True,blank=True)
    claim_response_id = models.CharField(max_length=100,null=True,blank=True)
    
    preauth = models.ForeignKey(PreAuthBundle,on_delete=models.CASCADE,null=True,blank=True)

class CommunicationBundle(models.Model):
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    request_payload = models.JSONField(null=True,blank=True)
    communication_request_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle_status = models.BooleanField(default=False)
    response_bundle = models.JSONField(null=True,blank=True)
    response_payload = models.JSONField(null=True,blank=True)
    communication_response_id = models.CharField(max_length=100,null=True,blank=True)
    
    claim = models.ForeignKey(ClaimBundle,on_delete=models.CASCADE,null=True,blank=True)

class PaymentReconciliationBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    claim_request_id = models.CharField(max_length=100,null=True,blank=True)
    payment_reconciliation_id = models.CharField(max_length=100,null=True,blank=True)
    
    claim_response_id = models.CharField(max_length=100,null=True,blank=True)
    
    claim = models.ForeignKey(ClaimBundle,on_delete=models.CASCADE,null=True,blank=True)

class PaymentNoticeBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    payment_reconciliation_id = models.CharField(max_length=100,null=True,blank=True)
    

class TaskBundle(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    request_task_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle = models.JSONField(null=True,blank=True)
    response_task_id = models.CharField(max_length=100,null=True,blank=True)
    
    request_type = models.CharField(max_length=1000,default='cancel')
    
    claim = models.ForeignKey(ClaimBundle,on_delete=models.CASCADE,null=True,blank=True)

class BatchRequestBundle(models.Model):
    request_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    request_bundle = models.JSONField(null=True,blank=True)
    request_task_id = models.CharField(max_length=100,null=True,blank=True)
    
    response_bundle_id = models.CharField(max_length=100,null=True,blank=True)
    response_bundle = models.JSONField(null=True,blank=True)
    response_task_id = models.CharField(max_length=100,null=True,blank=True)
    
    claims = models.ManyToManyField(ClaimBundle,blank=True)
    
    
    
class DiagnosisInformation(models.Model):
    icd_10 = models.ForeignKey("billing.ICD10",on_delete=models.CASCADE,null=True,blank=True)
    type  = models.CharField(max_length=100,null=True,blank=True)
    on_admission = models.CharField(max_length=100,null=True,blank=True)


class SupportingInfo(models.Model):
    type  = models.CharField(max_length=1000,null=True,blank=True)
    reason  = models.CharField(max_length=1000,null=True,blank=True)
    category  = models.CharField(max_length=1000,null=True,blank=True)
    value  = models.CharField(max_length=1000,null=True,blank=True)
    code = models.CharField(max_length=1000,null=True,blank=True)

class CareTeam(models.Model):
    practitioner  = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    practitioner_role  = models.CharField(max_length=1000,null=True,blank=True)
    care_team_role  = models.CharField(max_length=1000,null=True,blank=True)
    specialty  = models.CharField(max_length=1000,null=True,blank=True)

class Items(models.Model):
    type  = models.CharField(max_length=1000,null=True,blank=True)
    code_description  = models.CharField(max_length=1000,null=True,blank=True)
    quantity  = models.CharField(max_length=1000,null=True,blank=True)
    unit_price  = models.CharField(max_length=1000,null=True,blank=True)
    factor  = models.CharField(max_length=1000,null=True,blank=True)
    tax  = models.CharField(max_length=1000,null=True,blank=True)
    patient_share_p  = models.CharField(max_length=1000,null=True,blank=True)
    vat  = models.CharField(max_length=1000,null=True,blank=True)
    net  = models.CharField(max_length=1000,null=True,blank=True)
    patient_share  = models.CharField(max_length=1000,null=True,blank=True)
    payer_share = models.CharField(max_length=1000,null=True,blank=True)
    start_DateTime = models.DateTimeField(null=True,blank=True)
    care_teams = models.ManyToManyField(CareTeam,blank=True)
    diagnoses = models.ManyToManyField(DiagnosisInformation,blank=True)
    support_info = models.ManyToManyField(SupportingInfo,blank=True)
    body_site = models.CharField(max_length=1000,null=True,blank=True)
    
    
class Claim(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    coverage_eligibility_request = models.ForeignKey(CoverageEligibilityBundle,on_delete=models.CASCADE,null=True,blank=True)
    diagnosis_information = models.ManyToManyField(DiagnosisInformation,blank=True)
    supporting_info = models.ManyToManyField(SupportingInfo,blank=True)
    care_team = models.ManyToManyField(CareTeam,blank=True)
    items = models.ManyToManyField(Items,blank=True)
    claim_type=models.CharField(max_length=1000,null=True,blank=True)
    claim_sub_type=models.CharField(max_length=1000,null=True,blank=True)
    
    