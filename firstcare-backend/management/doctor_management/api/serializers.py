from management.doctor_management.models import *
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    fhir_id = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Department
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    