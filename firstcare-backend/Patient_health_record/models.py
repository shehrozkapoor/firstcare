from django.db import models
from Laboratory.models import AvailableTests, UnitOfMeasure
from Laboratory.administration.models import TestResult
from firstcare.settings import AUTH_USER_MODEL
from Patient.models import Patient
from management.doctor_management.models import Doctor
from management.ward_management.models import Ward
from management.schedule_management.models import Appointment


'''
the commented part is the old implementation in the patient healthcare record but then we started implemented through the
FHIR and other stuff so i kept this commented not deleted because i think this can be useful for you in future
so that's totaly depend on you wheather you keep it or delete it.by deleting it it will not have any effect on any other module

'''
# class Dispense(models.Model):
#     repeat = models.IntegerField(null=True,blank=True)
#     quantity = models.ForeignKey(Quantity,on_delete=models.CASCADE,null=True)
#     dispenser = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="dispenser")


# class Ingredient(models.Model):
#     identification = models.TextField(max_length=1000,null=True,blank=True)

# class Medicine(models.Model):
#     identification = models.ForeignKey(Ingredient,on_delete=models.CASCADE,null=True,blank=True)


# class AdministrationRequest(models.Model):
#     description = models.TextField(max_length=1000,null=True,blank=True)
#     totalPeriodicDosis = models.CharField(max_length=100,null=True,blank=True)
#     start = models.DateTimeField(null=True,blank=True)
#     end = models.DateTimeField(null=True,blank=True)
#     duration = models.ForeignKey(Quantity,on_delete=models.CASCADE,null=True)
#     numberOfAdministrations = models.IntegerField(null=True,blank=True)



# class Prescription(models.Model):
#     identifier = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="identifier")
#     status = models.CharField(max_length=10,null=True,blank=True)
#     patient = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="patient")
#     prescriber = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="prescriber")
#     prescribed = models.DateTimeField(null=True,blank=True)
#     reason = models.TextField(max_length=1000,null=True,blank=True)
#     dispense =  models.ForeignKey(Dispense,on_delete=models.CASCADE,null=True)
#     medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
#     administration_request = models.ForeignKey(AdministrationRequest,on_delete=models.CASCADE,null=True)


# class Coding(models.Model):
#     system = models.CharField(max_length=100,null=True,blank=True)
#     code = models.CharField(max_length=100,null=True,blank=True)
#     display = models.CharField(max_length=100,null=True,blank=True)


# class Plan(models.Model):
#     title = models.CharField(max_length=500,null=True,blank=True)

#     def __str__(self):
#         self.title




# class Refferals(models.Model):
#     title = models.CharField(max_length=500,null=True,blank=True)
#     text = models.TextField(max_length=100,null=True,blank=True)
#     identifier = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="refferals_identifier")
#     definition = models.TextField(max_length=100,null=True,blank=True)
#     based_on = models.TextField(max_length=100,null=True,blank=True)
#     replaces = models.TextField(max_length=100,null=True,blank=True)
#     group_identifier = models.CharField(max_length=20,null=True,blank=True)
#     status = models.CharField(max_length=100,null=True,blank=True)
#     intent = models.CharField(max_length=100,null=True,blank=True)
#     type = models.ForeignKey(Coding,on_delete=models.CASCADE,null=True,blank=True,related_name="type")
#     priority = models.CharField(max_length=100,null=True,blank=True)
#     service_requested = models.ForeignKey(Coding,on_delete=models.CASCADE,null=True,blank=True,related_name="service_requested")
#     subject = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="referral_subject")
#     context = models.CharField(max_length=100,null=True,blank=True)
#     occurrence_period = models.DateTimeField(null=True,blank=True)
#     authored_on = models.DateTimeField(null=True,blank=True)
#     requester = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="referral_requestor")
#     specialty = models.ForeignKey(Coding,on_delete=models.CASCADE,null=True,blank=True,related_name="referral_speciality")
#     recipient = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="referral_recipient")
#     reason_code = models.CharField(max_length=100,null=True,blank=True)
#     description = models.TextField(max_length=100,null=True,blank=True)


# class Procedure(models.Model):
#     status = models.CharField(max_length=100,null=True,blank=True)
#     code = models.ForeignKey(Coding,on_delete=models.CASCADE,null=True,blank=True,related_name="procedure_code")
#     subject = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="procedure_subject")
#     performed = models.DateTimeField(null=True,blank=True)
#     recorder = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="procedure_recorder")
#     asserter = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="procedure_asserter")
#     performer = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="procedure_performer")
#     reason_code = models.CharField(max_length=100,null=True,blank=True)
#     follow_up = models.TextField(max_length=100,null=True,blank=True)
#     note = models.TextField(max_length=100,null=True,blank=True)


# class Problem_Diagnosis(models.Model):
#     name = models.CharField(max_length=100,null=True,blank=True)
#     clinical_description = models.TextField(max_length=1000,null=True,blank=True)
#     body_site = models.TextField(max_length=1000,null=True,blank=True)
#     stuctured_body_site = models.TextField(max_length=1000,null=True,blank=True)
#     cause = models.TextField(max_length=1000,null=True,blank=True)
#     onsetTime = models.DateTimeField(null=True,blank=True)
#     clinically_recognized = models.DateTimeField(null=True,blank=True)
#     severity = models.TextField(max_length=1000,null=True,blank=True)
#     specific_details = models.TextField(max_length=1000,null=True,blank=True)
#     course_description = models.TextField(max_length=1000,null=True,blank=True)
#     resolutionTime = models.DateTimeField(null=True,blank=True)
#     status = models.CharField(max_length=100,null=True,blank=True)
#     diagnostic_certainity = models.CharField(max_length=100,null=True,blank=True)
#     comments = models.CharField(max_length=100,null=True,blank=True)



# class Manufacturer(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class Components(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class Asset(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class Extension(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class Multimedia(models.Model):
    # name = models.CharField(max_length=500,null=True,blank=True)

# class Devices(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)
#     type = models.CharField(max_length=200,null=True,blank=True)
#     description = models.TextField(max_length=1000,null=True,blank=True)
#     properties = models.CharField(max_length=300,null=True,blank=True)
#     manufacture = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,null=True,blank=True)
#     # date of manufacture
#     DOM = models.DateTimeField(null=True,blank=True)
#     serial_number = models.CharField(max_length=100,null=True,blank=True,unique=True)
#     catalogue_number = models.CharField(max_length=100,null=True,blank=True)
#     model_number = models.CharField(max_length=100,null=True,blank=True)
#     lot_number = models.CharField(max_length=100,null=True,blank=True)
#     software_version = models.CharField(max_length=20,null=True,blank=True)
#     # date of expiry
#     DOE = models.DateTimeField(null=True,blank=True)
#     assets = models.ForeignKey(Asset,on_delete=models.CASCADE,null=True,blank=True)
#     components = models.ForeignKey(Components,on_delete=models.CASCADE,null=True,blank=True)
#     extension = models.ForeignKey(Extension,on_delete=models.CASCADE,null=True,blank=True)
#     multimedia = models.ForeignKey(Multimedia,on_delete=models.CASCADE,null=True,blank=True)
#     comment = models.CharField(max_length=500,null=True,blank=True)


# class Education(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class EducationSummary(models.Model):
#     description = models.TextField(max_length=1000,null=True,blank=True)
#     age_started = models.IntegerField(null=True,blank=True)
#     age_ended = models.IntegerField(null=True,blank=True)
#     higest_level_completed = models.CharField(max_length=100,null=True,blank=True)
#     education_record = models.ForeignKey(Education,on_delete=models.CASCADE,null=True,blank=True)
#     additional_details = models.TextField(max_length=1000,null=True,blank=True)
#     comment = models.CharField(max_length=500,null=True,blank=True)



# class ServiceType(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)

# class ScreeningActivity(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)
#     service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE,null=True,blank=True)
#     description = models.TextField(max_length=1000,null=True,blank=True)
#     reason = models.TextField(max_length=1000,null=True,blank=True)
#     comment = models.CharField(max_length=500,null=True,blank=True)


# class Target(models.Model):
    # name = models.CharField(max_length=500,null=True,blank=True)
    # description = models.TextField(max_length=1000,null=True,blank=True)
    # path = models.CharField(max_length=500,null=True,blank=True)
    # proposed_date = models.DateTimeField(null=True,blank=True)
    # end_date = models.DateTimeField(null=True,blank=True)
    # outcome = models.CharField(max_length=100,null=True,blank=True)
    # comment = models.CharField(max_length=500,null=True,blank=True)

# class Goal(models.Model):
#     name = models.CharField(max_length=500,null=True,blank=True)
#     description = models.TextField(max_length=1000,null=True,blank=True)
#     clinical_indication = models.TextField(max_length=1000,null=True,blank=True)
#     start_date = models.DateTimeField(null=True,blank=True)
#     proposed_date = models.DateTimeField(null=True,blank=True)
#     end_date = models.DateTimeField(null=True,blank=True)
#     outcome = models.CharField(max_length=100,null=True,blank=True)
#     comment = models.CharField(max_length=500,null=True,blank=True)
#     rediness_for_change = models.TextField(max_length=1000,null=True,blank=True)
#     target = models.ForeignKey(Target,on_delete=models.CASCADE,null=True,blank=True)

# # class Disease(models.Model):
# #     name = models.CharField(max_length=500,null=True,blank=True)

# # class Immunisation(models.Model):
# #     disease = models.ForeignKey(Disease,on_delete=models.CASCADE,null=True,blank=True)
# #     course_status = models.CharField(max_length=100,null=True,blank=True)
# #     primary_course_completed = models.DateTimeField(null=True,blank=True)
# #     last_booster = models.DateTimeField(null=True,blank=True)
# #     status = models.CharField(max_length=100,null=True,blank=True)
# #     comment = models.CharField(max_length=500,null=True,blank=True)


'''
when doctor providing the prescription he need to give the dosage instruction.
'''
class DosageInstruction(models.Model):
    precondition = models.TextField(max_length=1000,null=True,blank=True)
    prn = models.BooleanField(default=False)
    additional_instruction = models.TextField(max_length=1000,null=True,blank=True)
    route = models.TextField(max_length=1000,null=True,blank=True)
    dose = models.CharField(max_length=100,null=True)
    rate = models.CharField(max_length=100,null=True)
    schedule = models.CharField(max_length=100,null=True)

'''
relationship
'''
class RelationShip(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

'''
the type of the encounter
'''
class EncounterType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

'''
chiefcomplain see the powerchart to understand
'''
class ChiefComplain(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

'''
vitalsigns see the powerchart to understand
'''

class VitalSigns(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    unit_of_measure = models.ForeignKey(UnitOfMeasure,on_delete=models.CASCADE,null=True,blank=True)
    date_and_time = models.DateTimeField(null=True,blank=True)
    value = models.CharField(max_length=100,null=True,blank=True)


'''
problems or the illness the patient will have
'''
class Problems(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)


'''
there can be multiple problem saved in the problem list so the user doesnot need to add the similar problem
again and again he can just select the problem list and all the problem will be given
'''
class ProblemList(models.Model):
    problem = models.ManyToManyField(Problems,related_name="problem_lists_problems")
    this_visit = models.BooleanField(default=True)
    chronic = models.BooleanField(default=False)


'''
Hospital or doctor want to have a document
'''
class Document(models.Model):
    value = models.TextField(null=True,blank=True)
    subject = models.CharField(max_length=1000,null=True,blank=True)
    note = models.CharField(max_length=1000,null=True,blank=True)
    creation_time = models.DateTimeField(null=True,blank=True)
    attachment = models.FileField(null=True,blank=True)


'''
to save the historytype of the patient
'''
class HistoryType(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)


'''
to save the history of the patient
'''
class History(models.Model):
    type = models.ForeignKey(HistoryType,on_delete=models.CASCADE,null=True,blank=True)
    name = models.TextField(null=True,blank=True)


'''
review of the system
'''
class ReviewOfSystem(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    value = models.TextField(null=True,blank=True)


'''
physical exam
'''
class PhysicalExam(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    value = models.TextField(null=True,blank=True)


'''
order
'''
class Order(models.Model):
    test = models.ManyToManyField(AvailableTests,related_name="ordered_tests")
    quantity = models.IntegerField(null=True,blank=True)
    when_schedule = models.DateTimeField(null=True,blank=True)


'''
Assesment and plan
'''
class AssessmentAndPlan(models.Model):
    problem = models.ForeignKey(ProblemList,on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

'''
progress note if the user revisit the doctor for checkup so the doctor will write the progress note
'''
class ProgressNote(models.Model):
    description = models.TextField(null=True,blank=True)


'''
all the information for a specific patient encounter will be stored here
'''
class Encounter(models.Model):
    estimated_arrival_date = models.DateTimeField(null=True,blank=True)
    type = models.ForeignKey(EncounterType,on_delete=models.CASCADE,null=True,blank=True)
    registeration_date = models.DateTimeField(null=True,blank=True)
    discharge_date = models.DateTimeField(null=True,blank=True)
    attending_physician = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    chief_complain = models.ForeignKey(ChiefComplain,on_delete=models.CASCADE,null=True,blank=True)
    vital_sign = models.ManyToManyField(VitalSigns,blank=True)
    problem_list = models.ForeignKey(ProblemList,on_delete=models.CASCADE,null=True,blank=True)
    home_medication = models.ManyToManyField(DosageInstruction,related_name="Encounter_home_medication",blank=True)
    document = models.ManyToManyField(Document,related_name="Encounter_documents",blank=True)
    lab_result = models.ManyToManyField(TestResult,related_name="Encounter_tests",blank=True)
    history = models.ManyToManyField(History,related_name="Encounter_history",blank=True)
    review_of_system = models.ForeignKey(ReviewOfSystem,on_delete=models.CASCADE,null=True,blank=True)
    physical_exam = models.ForeignKey(PhysicalExam,on_delete=models.CASCADE,null=True,blank=True)
    orders = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    assessment_and_plan = models.ManyToManyField(AssessmentAndPlan,related_name="encounter_AssessmentAndPlan",blank=True)
    progress_note = models.ForeignKey(ProgressNote,on_delete=models.CASCADE,null=True,blank=True)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)