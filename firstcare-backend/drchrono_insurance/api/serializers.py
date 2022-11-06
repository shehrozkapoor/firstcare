from rest_framework import serializers
from drchrono_insurance.models import *


'''
all the serializers for the patient insurance
'''

class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'

class InsurancePlanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlanType
        fields = '__all__'

class HCFASerializer(serializers.ModelSerializer):
    class Meta:
        model = HCFA
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'