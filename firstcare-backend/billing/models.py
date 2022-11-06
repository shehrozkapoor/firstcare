from django.db import models
from Patient.models import Patient
from accounts.models import CustomUser
from management.schedule_management.models import Appointment
from FHIR.models import TaskBundle, CoverageEligibilityBundle,ClaimBundle, PaymentNoticeBundle, PaymentReconciliationBundle, PaymentReconciliationBundle,PreAuthBundle,CommunicationBundle



# ICD version
ICD_VERSION = (
    ('AUTO','AUTO'),
    ('ICD-10','ICD-10'),
    ('ICD-9','ICD-9'),
)

# Billing status
BILLING_STATUS = (
    ("Paid In Full","Paid In Full"),
    ("Balance Due","Balance Due"),
    ("Settled","Settled"),
    ("Internal Review","Internal Review"),
    ("Bill Insurance","Bill Insurance"),
    ("Bill Secondary Insurance","Bill Secondary Insurance"),
    ("Worker's Comp Claim","Worker's Comp Claim"),
    ("Auto Accident Claim","Auto Accident Claim"),
    ("Durable Medical Equipment Claim","Durable Medical Equipment Claim"),

)
# payment type we will have in the database
class PaymentType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

# payment methods we have in the database
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


'''
payment will be based on the payment_date on which date and time payment was made
payment can be only made for a specific appointment that patient has booked
Provider payment will also keep track that who has made the payment or who has served the patient to take the payment
type which payment type is used for the payment
method which payment method is used for the payment
note any note the provider want to set in the payment
amount how much amount is made.
'''

class Payment(models.Model):
    payment_date = models.DateTimeField(null=True)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)
    provider = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    type = models.ForeignKey(PaymentType,on_delete=models.CASCADE,null=True,blank=True)
    method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE,null=True,blank=True)
    note = models.CharField(max_length=1000,null=True,blank=True)
    amount = models.FloatField(null=False,default=0.00)

    def __str__(self):
        return str(self.id)



'''
there can be different type of payment profile that will be saved
because the provider don't need to set everything again and again
so he will just select the payment profile and all the cost will be calculated automatically
right now this is not implemented in the system but in future it has to be in the billing.
'''
class PaymentProfile(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

'''
you can see the drchrono there is workflow of everything
'''

class OnsetDataType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

'''
you can see the drchrono there is workflow of everything
'''

class OtherDateType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

'''
you can see the drchrono there is workflow of everything
'''
class HcfaBOX(models.Model):
    employement = models.BooleanField(default=False)
    auto_accident = models.BooleanField(default=False)
    other_accident = models.BooleanField(default=False)
    one_set_data_type = models.ForeignKey(OnsetDataType,on_delete=models.CASCADE,null=True,blank=True)
    onset_date = models.DateField(null=True,blank=True)
    other_date_type = models.ForeignKey(OtherDateType,on_delete=models.CASCADE,null=True,blank=True)
    other_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.id)

'''
ICD 10 code and each code will also a fixed amount so once user select the ICD codes it will calculate the complete cost
'''
class ICD10(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True,unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

'''
ICD 9 code and each code will also a fixed amount so once user select the ICD codes it will calculate the complete cost
'''
class ICD9(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True,unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

'''
CPTITEM  and each code will also a fixed amount so once user select the CPT ITEM codes it will calculate the complete cost
'''
class CPTITEM(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True,unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

'''
CPTCODE will contain the CPT ITEM and it will calculate all the cost
'''
class CPTCODE(models.Model):
    cpt_item = models.ForeignKey(CPTITEM,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.cpt_item.name

'''
same like ICD-10,ICD-9 and CPTCODE
'''

class HCPCS(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

'''
same like ICD-10,ICD-9 and CPTCODE
'''
class HCPCSCODE(models.Model):
    hcpcs_item = models.ForeignKey(HCPCS,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True)


    def __str__(self):
        return self.hcpcs_item.name



'''
this will be the final billing for a appointment.
for which pateint billing is done
icd_version
paymet that are done for a specific patient
and soo on...
'''
class Billing(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    icd_version = models.CharField(choices=ICD_VERSION,default='AUTO',max_length=10)
    pre_authorization_approval = models.CharField(max_length=100,null=True,blank=True)
    refferal_num = models.CharField(max_length=100,null=True,blank=True)
    payment_profile = models.ManyToManyField(PaymentProfile,related_name="payment_profile",blank=True)
    hcfa_box = models.ForeignKey(HcfaBOX,on_delete=models.CASCADE,null=True,blank=True)
    icd_10 = models.ManyToManyField(ICD10,related_name="icd_10")
    cpt_code = models.ManyToManyField(CPTCODE,related_name="cpt_codes")
    hcpcs_code = models.ManyToManyField(HCPCSCODE,related_name="hcpcs_codes")
    status = models.CharField(max_length=50,choices=BILLING_STATUS,null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    billing_note = models.CharField(max_length=1000,null=True,blank=True)
    service_note = models.CharField(max_length=1000,null=True,blank=True)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)
    fhir_claim_id = models.CharField(max_length=100,null=True,blank=True)
    claim_amount = models.FloatField(null=True,blank=True)
    unit_amount = models.FloatField(null=True,blank=True)
    paid_amount = models.FloatField(null=True,blank=True)
    total_amount = models.FloatField(null=True,blank=True)
    eligibility_bundle = models.ForeignKey(CoverageEligibilityBundle,on_delete=models.CASCADE,null=True,blank=True)
    pre_auth_bundle = models.ForeignKey(PreAuthBundle,on_delete=models.CASCADE,null=True,blank=True)
    claim_bundle = models.ForeignKey(ClaimBundle,on_delete=models.CASCADE,null=True,blank=True)
    communication_bundle = models.ForeignKey(CommunicationBundle,on_delete=models.CASCADE,null=True,blank=True)
    payment_reconciliation_bundle = models.ForeignKey(PaymentReconciliationBundle,on_delete=models.CASCADE,null=True,blank=True)
    payment_notice_bundle = models.ForeignKey(PaymentNoticeBundle,on_delete=models.CASCADE,null=True,blank=True)
    payment_cancel_bundle = models.ForeignKey(TaskBundle,on_delete=models.CASCADE,null=True,blank=True,related_name="cancel_bundle")
    payment_status_bundle = models.ForeignKey(TaskBundle,on_delete=models.CASCADE,null=True,blank=True,related_name="status_bundle")
    payment_poll_bundle = models.ForeignKey(TaskBundle,on_delete=models.CASCADE,null=True,blank=True,related_name="poll_bundle")
    
    
    
    def __str__(self):
        return f"this billing with id {str(self.id)}"





