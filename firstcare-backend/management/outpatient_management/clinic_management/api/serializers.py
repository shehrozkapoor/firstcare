from dataclasses import field
from management.outpatient_management.clinic_management.models import *
from rest_framework import serializers



class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

        