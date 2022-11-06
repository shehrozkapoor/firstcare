from django.db import models
from Insurance.models import *



class Region(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class District(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class Conversion(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


class Treatment(models.Model):
    deductible = models.CharField(max_length=100,null=True,blank=True)
    ceiling = models.CharField(max_length=100,null=True,blank=True)
    hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)

class Insuree(models.Model):
    deductible = models.CharField(max_length=100,null=True,blank=True)
    ceiling = models.CharField(max_length=100,null=True,blank=True)
    hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)

class Policy(models.Model):
    deductible = models.CharField(max_length=100,null=True,blank=True)
    ceiling = models.CharField(max_length=100,null=True,blank=True)
    hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_deductible = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)

class ExtraMemberCeiling(models.Model):
    ceiling = models.CharField(max_length=100,null=True,blank=True)
    hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)

class MaximumCeiling(models.Model):
    ceiling = models.CharField(max_length=100,null=True,blank=True)
    hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)
    non_hospital_ceiling = models.CharField(max_length=100,null=True,blank=True)

class Number(models.Model):
    consultation = models.CharField(max_length=100,null=True,blank=True)
    surgeries = models.CharField(max_length=100,null=True,blank=True)
    deliveries = models.CharField(max_length=100,null=True,blank=True)
    hospitalization = models.CharField(max_length=100,null=True,blank=True)
    antenatal = models.CharField(max_length=100,null=True,blank=True)
    visits = models.CharField(max_length=100,null=True,blank=True)

class Ceiling(models.Model):
    consultation = models.CharField(max_length=100,null=True,blank=True)
    surgeries = models.CharField(max_length=100,null=True,blank=True)
    deliveries = models.CharField(max_length=100,null=True,blank=True)
    hospitalization = models.CharField(max_length=100,null=True,blank=True)
    antenatal = models.CharField(max_length=100,null=True,blank=True)

DISTRIBUTION_TYPE = (
    ('0','NONE'),
    ('1','MONTHLY'),
    ('2','QUATERLY'),
    ('3','YEARLY')
)
class Distribution(models.Model):
    type = models.CharField(max_length=1,choices=DISTRIBUTION_TYPE,default='0')
    month_1 = models.CharField(max_length=100,null=True,blank=True)
    month_2 = models.CharField(max_length=100,null=True,blank=True)
    month_3 = models.CharField(max_length=100,null=True,blank=True)
    month_4 = models.CharField(max_length=100,null=True,blank=True)
    month_5 = models.CharField(max_length=100,null=True,blank=True)
    month_6 = models.CharField(max_length=100,null=True,blank=True)
    month_7 = models.CharField(max_length=100,null=True,blank=True)
    month_8 = models.CharField(max_length=100,null=True,blank=True)
    month_9 = models.CharField(max_length=100,null=True,blank=True)
    month_10 = models.CharField(max_length=100,null=True,blank=True)
    month_11 = models.CharField(max_length=100,null=True,blank=True)
    month_12 = models.CharField(max_length=100,null=True,blank=True)
    quater_1 = models.CharField(max_length=100,null=True,blank=True)
    quater_2 = models.CharField(max_length=100,null=True,blank=True)
    quater_3 = models.CharField(max_length=100,null=True,blank=True)
    quater_4 = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=True,blank=True)

class Level(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class SubLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class CapitationPayment(models.Model):
    level_1 = models.ForeignKey(Level,on_delete=models.CASCADE,null=True,blank=True,related_name="level_1")
    sub_level_1 = models.ForeignKey(SubLevel,on_delete=models.CASCADE,null=True,blank=True,related_name="sub_level_1")
    level_2 = models.ForeignKey(Level,on_delete=models.CASCADE,null=True,blank=True,related_name="level_2")
    sub_level_2 = models.ForeignKey(SubLevel,on_delete=models.CASCADE,null=True,blank=True,related_name="sub_level_2")
    level_3 = models.ForeignKey(Level,on_delete=models.CASCADE,null=True,blank=True,related_name="level_3")
    sub_level_3 = models.ForeignKey(SubLevel,on_delete=models.CASCADE,null=True,blank=True,related_name="sub_level_3")
    level_4 = models.ForeignKey(Level,on_delete=models.CASCADE,null=True,blank=True,related_name="level_4")
    sub_level_4 = models.ForeignKey(SubLevel,on_delete=models.CASCADE,null=True,blank=True,related_name="sub_level_4")
    share_of_contribution = models.CharField(max_length=100,null=True,blank=True)
    weight_of_population = models.CharField(max_length=100,null=True,blank=True)
    weight_of_number_of_families = models.CharField(max_length=100,null=True,blank=True)
    weight_of_insured_population = models.CharField(max_length=100,null=True,blank=True)
    weight_of_insured_families = models.CharField(max_length=100,null=True,blank=True)
    weight_of_number_of_visits = models.CharField(max_length=100,null=True,blank=True)
    weight_of_adjusted_amount = models.CharField(max_length=100,null=True,blank=True)



class Product(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    conversion = models.ForeignKey(Conversion,on_delete=models.CASCADE,null=True,blank=True)
    lump_sum = models.BigIntegerField(null=True,blank=True)
    threshold_member = models.CharField(max_length=100,null=True,blank=True)
    maximum_memebers = models.BigIntegerField(null=True,blank=True)
    contribution_adult = models.CharField(max_length=100,null=True,blank=True)
    contribution_child = models.CharField(max_length=100,null=True,blank=True)
    insurance_period = models.IntegerField(null=True,blank=True)
    administration_period = models.IntegerField(null=True,blank=True)
    max_installments = models.IntegerField(null=True,blank=True)
    grace_period_payment = models.IntegerField(null=True,blank=True)
    grace_period_enrollment = models.IntegerField(null=True,blank=True)
    grace_period_renewal = models.IntegerField(null=True,blank=True)
    renewal_disc = models.IntegerField(null=True,blank=True)
    renewal_disc_period = models.IntegerField(null=True,blank=True)
    enrollment_disc = models.IntegerField(null=True,blank=True)
    enrollment_disc_period = models.IntegerField(null=True,blank=True)
    account_code_remuneration = models.CharField(max_length=100,null=True,blank=True)
    account_code_contribution = models.CharField(max_length=100,null=True,blank=True)
    registration_lump_sum = models.BigIntegerField(null=True,blank=True)
    assembly_lump_sum = models.BigIntegerField(null=True,blank=True)
    registration_fee = models.BigIntegerField(null=True,blank=True)
    assembly_fee = models.BigIntegerField(null=True,blank=True)
    start_cycle_1_day = models.IntegerField(null=True,blank=True)
    start_cycle_1_month = models.IntegerField(null=True,blank=True)
    start_cycle_2_day = models.IntegerField(null=True,blank=True)
    start_cycle_2_month = models.IntegerField(null=True,blank=True)
    start_cycle_3_day = models.IntegerField(null=True,blank=True)
    start_cycle_3_month = models.IntegerField(null=True,blank=True)
    start_cycle_4_day = models.IntegerField(null=True,blank=True)
    start_cycle_4_month = models.IntegerField(null=True,blank=True)
    treatment = models.ForeignKey(Treatment,on_delete=models.CASCADE,null=True,blank=True)
    insuree = models.ForeignKey(Insuree,on_delete=models.CASCADE,null=True,blank=True)
    policy = models.ForeignKey(Policy,on_delete=models.CASCADE,null=True,blank=True)
    extra_member_ceiling = models.ForeignKey(ExtraMemberCeiling,on_delete=models.CASCADE,null=True,blank=True)
    maximum_ceiling = models.ForeignKey(MaximumCeiling,on_delete=models.CASCADE,null=True,blank=True)
    distribution_deductable = models.ForeignKey(Distribution,on_delete=models.CASCADE,null=True,blank=True,related_name="deductable")
    distribution_deductable_hospital = models.ForeignKey(Distribution,on_delete=models.CASCADE,null=True,blank=True,related_name="deductablehospital")
    distribution_deductable_non_hospital = models.ForeignKey(Distribution,on_delete=models.CASCADE,null=True,blank=True,related_name="deductablenonhospital")
    capitation_payment = models.ForeignKey(CapitationPayment,on_delete=models.CASCADE,null=True,blank=True)


class HealthFacilityLegalForm(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class HealthFacilitySubLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class CareType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class ServicesPriceList(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class ItemPriceList(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class HealthFacilities(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    health_facility_legal_form = models.ForeignKey(HealthFacilityLegalForm,on_delete=models.CASCADE,null=True,blank=True)
    health_facility_level = models.ForeignKey(HealthFacilityLevel,on_delete=models.CASCADE,null=True,blank=True)
    health_facility_sub_level = models.ForeignKey(HealthFacilitySubLevel,on_delete=models.CASCADE,null=True,blank=True)
    care_type = models.ForeignKey(CareType,on_delete=models.CASCADE,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    accounting_code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    fax = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    services_price_list = models.ForeignKey(ServicesPriceList,on_delete=models.CASCADE,null=True,blank=True)
    item_price_list = models.ForeignKey(ItemPriceList,on_delete=models.CASCADE,null=True,blank=True)
    


class ServiceType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class ServiceLevel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


class MedicalServices(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE,null=True,blank=True)
    service_category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE,null=True,blank=True)
    service_level = models.ForeignKey(ServiceLevel,on_delete=models.CASCADE,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    care_type = models.ForeignKey(CareType,on_delete=models.CASCADE,null=True,blank=True)
    frequency = models.CharField(max_length=100,null=True,blank=True)
    male = models.BooleanField(default=True)
    female = models.BooleanField(default=True)
    adult = models.BooleanField(default=True)
    minor = models.BooleanField(default=True)

class ItemType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class MedicalItem(models.Model):
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    type = models.ForeignKey(ItemType,on_delete=models.CASCADE,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    care_type = models.ForeignKey(CareType,on_delete=models.CASCADE,null=True,blank=True)
    frequency = models.CharField(max_length=100,null=True,blank=True)
    male = models.BooleanField(default=True)
    female = models.BooleanField(default=True)
    adult = models.BooleanField(default=True)
    minor = models.BooleanField(default=True)

    

class MedicalServicesPriceList(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    services = models.ManyToManyField(MedicalServices,related_name="services")

class MedicalItemsPriceList(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    items = models.ManyToManyField(MedicalItem,related_name="services")


class PayerType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class Payer(models.Model):
    payer_type = models.ForeignKey(PayerType,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    fax = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)


class CalculationRules(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

class ContributionPlan(models.Model):
    calculation_rule = models.ForeignKey(CalculationRules,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    periodically = models.IntegerField(null=True,blank=True)
    valid_from = models.DateField(null=True,blank=True)
    valid_to = models.DateField(null=True,blank=True)