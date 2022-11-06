from django.db import models
from Patient.models import Patient
SEX = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER'),
    ('UNKNOWN','UNKNOWN'),
    ('DECLINE TO SPECIFY','DECLINE TO SPECIFY')
    )

RELATIONSHIP = (
    ('Spouse','Spouse'),
    ('Grandparent','Grandparent'),
    ('Grandchild','Grandchild'),
    ('Nephew or Niece','Nephew or Niece'),
    ('Foster Child','Foster Child'),
    ('Ward','Ward'),
    ('Stepson or Stepdaughter','Stepson or Stepdaughter'),
    ('Child','Child'),
    ('Employee','Employee'),
    ('Unknown','Unknown'),
    ('Handicapped Dependent','Handicapped Dependent'),
    ('Sponsored Dependent','Sponsored Dependent'),
    ('Dependent of a Minor Dependent','Dependent of a Minor Dependent'),
    ('Significant Other','Significant Other'),
    ('Mother','Mother'),
    ('Father','Father'),
    ('Emancipated Minor','Emancipated Minor'),
    ('Organ Donor','Organ Donor'),
    ('Cadaver Donor','Cadaver Donor'),
    ('Injured Plaintiff','Injured Plaintiff'),
    ('Child Where Insured Has No Financial Responsibility','Child Where Insured Has No Financial Responsibility'),
    ('Life Partner','Life Partner'),
    ('Dependent','Dependent'),
    ('Other Relationship','Other Relationship')
)

INSURANCE_TYPE = (
    ('PRIMARY INSURANCE','PRIMARY INSURANCE'),
    ('SECONDARY INSURANCE','SECONDARY INSURANCE'),
    ('TERTIARY INSURANCE','TERTIARY INSURANCE'),
    ('AUTO ACCIDENT INSURANCE','AUTO ACCIDENT INSURANCE'),
    ('WORKER COMP INSURANCE','WORKER COMP INSURANCE'),
    ('DURABLE MED EQPT INSURANCE','DURABLE MED EQPT INSURANCE'),
)


# insurance companies we will have in the system

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    nameAr = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.name

# insurance plans we will have in the system
class InsurancePlanType(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class HCFA(models.Model):
    onset_date = models.DateField(null=True,blank=True)
    initial_visit_date = models.DateField(null=True,blank=True)
    prepopulate_last_related_visit = models.BooleanField(default=False)



'''
if the patient is not there is someone else who want to use the Insurance
e.g
some relative of the patient has the insurance like brother,mother e.t.c
so we will save the subscriber information (you can also see the fhir implementation on the FHIR website)
'''
class Subscriber(models.Model):
    relationship = models.CharField(max_length=100,null=True,blank=True,choices=RELATIONSHIP)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    sex = models.CharField(max_length=20,null=True,blank=True,choices=SEX)
    suffix = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True)
    ssn = models.CharField(max_length=100,null=True,blank=True)
    phone_num = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    zip_code = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


'''
all the insurance information on patient will be saved here
there can be different types of insurance in the insurance and one patient can have multiple insurance but it cannot be of same type
'''
class Insurance(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    policy_number = models.CharField(max_length=100,null=True,blank=True)
    classname = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    DeductibleRate = models.CharField(max_length=100,null=True,blank=True)
    MaxLimit = models.CharField(max_length=100,null=True,blank=True)
    BeneficiaryType = models.CharField(max_length=100,null=True,blank=True)
    BeneficiaryTypeId = models.CharField(max_length=100,null=True,blank=True)
    BeneficiaryNumber = models.CharField(max_length=100,null=True,blank=True)
    IdentityNumber = models.CharField(max_length=100,null=True,blank=True)
    BeneficiaryName = models.CharField(max_length=100,null=True,blank=True)
    InceptionDate = models.CharField(max_length=100,null=True,blank=True)
    PolicyHolder = models.CharField(max_length=100,null=True,blank=True)
    InsurancePolicyExpiryDate = models.CharField(max_length=100,null=True,blank=True)
    
    company = models.ForeignKey(InsuranceCompany,on_delete=models.CASCADE,null=True,blank=True)
    player_id = models.CharField(max_length=100,null=True,blank=True)
    tpl_code = models.CharField(max_length=100,null=True,blank=True)
    id_num = models.CharField(max_length=100,null=True,blank=True)
    group_name = models.CharField(max_length=100,null=True,blank=True)
    group_num = models.CharField(max_length=100,null=True,blank=True)
    plan_name = models.CharField(max_length=100,null=True,blank=True)
    plan_type = models.ForeignKey(InsurancePlanType,on_delete=models.CASCADE,null=True,blank=True)
    claim_office_num = models.CharField(max_length=100,null=True,blank=True)
    allowed_visits_num = models.CharField(max_length=100,null=True,blank=True)
    card_issue_date = models.DateField(null=True,blank=True)
    note = models.CharField(max_length=100,null=True,blank=True)
    photo_front = models.FileField(null=True)
    photo_back = models.FileField(null=True)
    same_person = models.BooleanField(default=True)
    hcfa = models.ForeignKey(HCFA,on_delete=models.CASCADE,null=True,blank=True)
    subscriber = models.ForeignKey(Subscriber,on_delete=models.CASCADE,null=True,blank=True)
    insurance_type = models.CharField(max_length=100,choices=INSURANCE_TYPE,null=True,blank=True)


    def __Str__(self):
        return self.patient.patient_id
