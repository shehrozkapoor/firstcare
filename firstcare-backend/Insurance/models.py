import code
from django.db import models
from Patient.models import GENDER, MARITAL_STATUS
from firstcare.settings import AUTH_USER_MODEL


# insurance user permissions
class InsuranceUserPermision(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# insurance user roles
class InsuranceUserRoles(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    blocked = models.BooleanField(default=False)
    permisions = models.ManyToManyField(InsuranceUserPermision,related_name="insurance_user_permissions")

# insurance users
class InsuranceUser(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    role = models.ManyToManyField(InsuranceUserRoles,related_name="insurance_user_roles")

# family type
class FamilyType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# confirmation type
class ConfirmationType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# family
class Family(models.Model):
    type = models.ForeignKey(FamilyType,on_delete=models.CASCADE,null=True,blank=True)
    confirmation_type = models.ForeignKey(ConfirmationType,on_delete=models.CASCADE,null=True,blank=True)
    confirmation_num = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    poverty_status = models.BooleanField(default=False)

# relationship
class RelationShip(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# profession
class Profession(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# education
class Education(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# id type
class IdType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


TYPE = (
    ('1','HEAD-INSURANCE'),
    ('2','INSURANCE'),
)
# head insuree ? who is the main insurance holder
class HeadInsuree(models.Model):
    insurance_num = models.CharField(max_length=100,null=True,blank=True)
    relationship_details = models.ForeignKey(RelationShip,on_delete=models.CASCADE,null=True,blank=True)
    given_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=7,choices=GENDER,null=True)
    maritial_status = models.CharField(max_length=10,choices=MARITAL_STATUS,null=True)
    beneficiary_card = models.BooleanField(default=False)
    phone = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE,null=True,blank=True)
    education = models.ForeignKey(Education,on_delete=models.CASCADE,null=True,blank=True)
    id_type = models.ForeignKey(IdType,on_delete=models.CASCADE,null=True,blank=True)
    id_num = models.CharField(max_length=100,null=True,blank=True)
    photo = models.FileField(null=True,blank=True)
    photo_date = models.DateField(null=True,blank=True)
    type = models.CharField(max_length=1,choices=TYPE,null=True,blank=True)

# health facility level
class HealthFacilityLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# health facility
class HealthFacility(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    level = models.ForeignKey(HealthFacilityLevel,on_delete=models.CASCADE,null=True,blank=True)


# firstservice point
class FirstServicePoint(models.Model):
    facility = models.ForeignKey(HealthFacility,on_delete=models.CASCADE,null=True,blank=True)



# insurance
class Insurance(models.Model):
    family = models.ForeignKey(Family,on_delete=models.CASCADE,null=True,blank=True)
    head_insurance = models.ForeignKey(HeadInsuree,on_delete=models.CASCADE,null=True,blank=True)
    first_service_point = models.ForeignKey(FirstServicePoint,on_delete=models.CASCADE,null=True,blank=True)


# who has insurance

class Insuree(models.Model):
    family = models.ForeignKey(Family,on_delete=models.CASCADE,null=True,blank=True)
    head_insurance = models.ForeignKey(HeadInsuree,on_delete=models.CASCADE,null=True,blank=True)
    first_service_point = models.ForeignKey(FirstServicePoint,on_delete=models.CASCADE,null=True,blank=True)

# which insurance
class Products(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)


# policy details
class PolicyDetails(models.Model):
    enrollment_date = models.DateField(null=True)
    effective_date = models.DateField(null=True)
    start_date =  models.DateField(null=True)
    end_date =  models.DateField(null=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
    officer = models.ForeignKey(InsuranceUser,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=100,null=True)


# deduction
class Deductable(models.Model):
    general = models.CharField(max_length=100,null=True,blank=True)
    in_patient = models.CharField(max_length=100,null=True,blank=True)
    out_patient = models.CharField(max_length=100,null=True,blank=True)


# remunerated
class Remunerated(models.Model):
    general = models.CharField(max_length=100,null=True,blank=True)
    in_patient = models.CharField(max_length=100,null=True,blank=True)
    out_patient = models.CharField(max_length=100,null=True,blank=True)

#policies values

class PoliciesValues(models.Model):
    value = models.CharField(max_length=100,null=True,blank=True)
    contribution_paid = models.CharField(max_length=100,null=True,blank=True)
    balance = models.CharField(max_length=100,null=True,blank=True)
    deductable = models.ForeignKey(Deductable,on_delete=models.CASCADE,null=True,blank=True)
    remunerated = models.ForeignKey(Remunerated,on_delete=models.CASCADE,null=True,blank=True)


# policies
class Policies(models.Model):
    family = models.ForeignKey(Family,on_delete=models.CASCADE,null=True,blank=True)
    policy_details = models.ForeignKey(PolicyDetails,on_delete=models.CASCADE,null=True,blank=True)
    policy_value = models.ForeignKey(PoliciesValues,on_delete=models.CASCADE,null=True,blank=True)

# payment type
class PaymentType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# contribution category
class ContributionCategory(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

# contribution
class Contribution(models.Model):
    policy = models.ForeignKey(Policies,on_delete=models.CASCADE,null=True,blank=True)
    payment_date = models.DateField(null=True)
    payer = models.ForeignKey(InsuranceUser,on_delete=models.CASCADE,null=True,blank=True)
    amount = models.CharField(max_length=100,null=True,blank=True)
    payment_type = models.ForeignKey(PaymentType,on_delete=models.CASCADE,null=True,blank=True)
    reciept_num = models.CharField(max_length=100,null=True,blank=True)
    category = models.ForeignKey(ContributionCategory,on_delete=models.CASCADE,null=True,blank=True)

# legal form
class LegalForm(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


# activity code
class ActivityCode(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


# policy holder
class PolicyHolders(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    trade_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    phone = models.CharField(max_length=1000,null=True,blank=True)
    fax = models.CharField(max_length=1000,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    contact_name = models.CharField(max_length=100,null=True,blank=True)
    leagal_form = models.ForeignKey(LegalForm,on_delete=models.CASCADE,null=True,blank=True)
    activity_code = models.ForeignKey(ActivityCode,on_delete=models.CASCADE,null=True,blank=True)
    accountancy_account = models.CharField(max_length=100,null=True,blank=True)
    bank_account = models.CharField(max_length=100,null=True,blank=True)
    payment_reference = models.CharField(max_length=100,null=True,blank=True)
    payment_date = models.DateField(null=True)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)

# contract
class Contract(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    policy_holder = models.ForeignKey(PolicyHolders,on_delete=models.CASCADE,null=True,blank=True)
    payment_reference = models.CharField(max_length=100,null=True,blank=True)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)

# diagnosis
class Diagnosis(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)