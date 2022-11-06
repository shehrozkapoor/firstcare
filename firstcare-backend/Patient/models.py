from django.db import models
from firstcare.settings import AUTH_USER_MODEL
from management.doctor_management.models import Department
from management.ward_management.models import Ward

IDENTIFICATION_TYPE = (
    ('NATIONAL-ID', 'NATIONAL-ID'),
    ('IQAMA', 'IQAMA'),
    ('NON ID', 'NON ID'),
)

RELATIONSHIP_TYPE = (
    ('1', '1'),
    ('2', '2')
)

REGISTRATION_TYPE = (
    ('1', '1'),
    ('2', '2')
)

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
    ('unknown', 'unknown')
)

MARITAL_STATUS = (
    ('MARRIED', 'MARRIED'),
    ('SINGLE', 'SINGLE')
)
CONTACT_INFORMATION_STATUS = (
    ('ACTIVE', 'ACTIVE'),
    ('CLOSED', 'CLOSED'),
    ('HOLD', 'HOLD')
)

DISCHARGE_CRITERIA = (
    ('N','NONE'),
    ('1','ONLY DISPLAY PATIENTS THAT ARE NOT DISCHARGE')
)

'''
contact information of the patient
'''
class ContactInformation(models.Model):
    email = models.EmailField(max_length=500, null=True, blank=True)
    phone_residence = models.CharField(max_length=500, null=False)
    off = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=False, blank=True)
    Int_Mob = models.BooleanField(default=False)
    Fax = models.CharField(max_length=500, null=True, blank=True)
    emergency_contact_name = models.CharField(
        max_length=100, null=True, blank=True)
    emergency_contact_number = models.CharField(
        max_length=13, null=True, blank=True)
    emergency_contact_gender = models.CharField(max_length=17, null=True, blank=False,choices=GENDER)
    emergency_contact_relationship = models.CharField(max_length=17, null=True, blank=False)
    send_email = models.BooleanField(default=False)
    send_sms = models.BooleanField(default=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    p_o_box = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    willing_to_donate_blood = models.BooleanField(default=False)
    emergency_patient = models.BooleanField(default=False)
    require_data_update = models.BooleanField(default=False)
    last_modification_date = models.DateTimeField(null=True, blank=True)
    modified_user_name = models.CharField(
        max_length=100, null=True, blank=True)
    status = models.CharField(
        max_length=6, choices=CONTACT_INFORMATION_STATUS, null=True, blank=True)
    stop_ivr = models.BooleanField(default=False)
    permanent_address = models.CharField(max_length=500, null=True, blank=True)
    temporary_address = models.CharField(max_length=500, null=True, blank=True)

'''
patient will be a user in the system so foreign key to a user model and some related information that a patient will have
'''
class Patient(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name='patient_profile')
    identification_type = models.CharField(
        max_length=14, choices=IDENTIFICATION_TYPE, null=True, blank=False)
    account_id = models.CharField(max_length=50, null=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    relationship_type = models.CharField(
        max_length=1, choices=RELATIONSHIP_TYPE, null=True, blank=False)
    id_number = models.IntegerField(null=True, blank=False)
    registration_type = models.CharField(
        max_length=1, choices=REGISTRATION_TYPE, null=True, blank=False)
    health_id = models.IntegerField(null=True, blank=False)
    id_expiry = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=17, null=False)
    first_name = models.CharField(max_length=50, null=False,default="")
    second_name = models.CharField(max_length=50, null=False,default="")
    third_name = models.CharField(max_length=50, null=True,blank=True)
    
    DOB_hijri = models.CharField(max_length=50, null=False, blank=False)
    e_health_id = models.CharField(max_length=50, null=True, blank=True)
    residency_type = models.CharField(max_length=100, null=False)
    document_id = models.CharField(max_length=50,primary_key=True,unique=True)
    maritail_status = models.CharField(max_length=10, null=True, blank=True,choices=MARITAL_STATUS)
    blood_group = models.CharField(max_length=3, null=True)
    insurance_plan = models.CharField(max_length=100, null=True,blank=True)
    file_id = models.CharField(max_length=100, null=True,blank=True)
    DOB = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, null=False, blank=True)
    document_type = models.CharField(max_length=100, null=True, blank=True)
    preffered_language = models.CharField(max_length=100, null=True, blank=True)
    
    fhir_id = models.CharField(max_length=100, null=True, blank=True)
    
    first_name_arabic = models.CharField(max_length=50, null=True, blank=True)
    second_name_arabic = models.CharField(max_length=50, null=True, blank=True)
    third_name_arabic = models.CharField(max_length=50, null=True, blank=True)
    last_name_arabic = models.CharField(max_length=50, null=True, blank=True)
    rh_facto = models.CharField(max_length=3, null=True)
    pregnant = models.BooleanField(default=False)
    privilege_member = models.BooleanField(default=False)
    membership_num = models.CharField(max_length=50, null=True, blank=True)
    file_type = models.FileField(null=True, blank=True)
    contact_info = models.ForeignKey(ContactInformation,on_delete=models.CASCADE,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    deceasedBoolean = models.BooleanField(default=False)
    deceasedDateTime = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(self.pk)


'''
patient list is available in powerchart for more understanding
of patient list you can search on youtube patientlist in powerchart
'''
class PatientList(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=200,null=False,unique=True)
    location = models.ManyToManyField(Ward,related_name="location")
    patient = models.ManyToManyField(Patient,related_name="patients")
    discharge_criteria = models.CharField(max_length=4,choices=DISCHARGE_CRITERIA,null=False)
    active = models.BooleanField(default=False)