from Patient.models import *
from rest_framework import serializers
from accounts.serializers import UserSerializer
from management.ward_management.api.serializers import HospitalSerializer,WardSerializer
from management.ward_management.models import Ward
from FHIR.NAPHIES_FHIR_REQUEST.FHIRPatient import FHIRPatient
import asyncio
from accounts.models import CustomUser

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    contact_info = ContactInformationSerializer(read_only=True)
    contact_info_id = serializers.IntegerField(write_only=True)

    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self,validate):

        user_id = validate.pop('user_id',None)
        contact_info_id = validate.pop('contact_info_id',None)

        patient = Patient.objects.create(**validate)

        user = CustomUser.objects.get(id=user_id)
        contact_info = ContactInformation.objects.get(id=contact_info_id)

        patient.user = user
        patient.contact_info = contact_info
        patient.save()
        return patient


class PatientSerializerForInsurance(serializers.ModelSerializer):
    contact_info = ContactInformationSerializer(read_only=True)
    email = serializers.EmailField(required=False,write_only=True)
    phone_number = serializers.CharField(required=True,write_only=True)
    emergency_contact_number = serializers.CharField(required=False,write_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
        
    def create(self,validate):
        print(validate)
        phone_number = validate.pop('phone_number','')
        emergency_contact_number = validate.pop('emergency_contact_number','')
        email = validate.pop('email','')
        if phone_number == '':
            error = {'message': "phone_number is required"}
            raise serializers.ValidationError(error)
        contact_info = ContactInformation(phone_number=phone_number,emergency_contact_number=emergency_contact_number,email=email)
        contact_info.save()
        patient = Patient.objects.create(**validate)
        patient.contact_info = contact_info
        patient.save()
        return patient
    
    def update(self, patient, validated_data):
        patient.contact_info.phone_number = validated_data.get('phone_number', patient.contact_info.phone_number)
        patient.contact_info.save()
        patient.save()
        return patient
        

class PatientListSerializer(serializers.ModelSerializer):
    location = WardSerializer(read_only=True,many=True)
    patient = PatientSerializer(read_only=True,many=True)
    location_id = serializers.ListField(write_only=True)
    patient_id = serializers.ListField(write_only=True)


    class Meta:
        model = PatientList
        fields = '__all__'

    def create(self, validated_data):
        location_id = validated_data.pop('location_id',None)
        patient_id = validated_data.pop('patient_id',None)

        patient_list = PatientList.objects.create(**validated_data)
        if location_id is not None:
            for id in list(location_id[0].split(',')):
                location = Ward.objects.get(pk=id)
                patient_list.location.add(location)
        if patient_id is not None:
            for id in list(patient_id[0].split(',')):
                print(id)
                patientObj = Patient.objects.get(pk=id)
                patient_list.patient.add(patientObj)
        return patient_list
