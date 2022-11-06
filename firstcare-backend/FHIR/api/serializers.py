from rest_framework import serializers
from FHIR.models import *
from Patient.api.serializers import PatientSerializer
from management.doctor_management.api.serializers import DoctorSerializer

'''
all the serializers for the patient insurance
'''

class CoverageEligibilityBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = CoverageEligibilityBundle
        fields = '__all__'

class PreAuthBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = PreAuthBundle
        fields = '__all__'

class ClaimBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = ClaimBundle
        fields = '__all__'

class CommunicationBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = CommunicationBundle
        fields = '__all__'

class PaymentReconciliationBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = PaymentReconciliationBundle
        fields = '__all__'

class PaymentNoticeBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = PaymentNoticeBundle
        fields = '__all__'

class TaskBundleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = TaskBundle
        fields = '__all__'

class DiagnosisInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisInformation
        fields = '__all__'

class SupportingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingInfo
        fields = '__all__'

class CareTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareTeam
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    care_teams = CareTeamSerializer(many=True,read_only=True)
    diagnoses = DiagnosisInformationSerializer(many=True,read_only=True)
    support_info = SupportingInfoSerializer(many=True,read_only=True)
    
    care_teams_ids = serializers.ListField(write_only=True)
    diagnoses_ids = serializers.ListField(write_only=True)
    support_info_ids = serializers.ListField(write_only=True)
        
    class Meta:
        model = Items
        fields = '__all__'
        
    def create(self, validated_data):
        care_teams = validated_data.pop("care_teams_ids", None)
        diagnoses = validated_data.pop("diagnoses_ids", None)
        support_info = validated_data.pop("support_info_ids", None)

        item = Items.objects.create(**validated_data)
        
        if care_teams is not None:
            for id in list(care_teams[0].split(',')):
                try:
                    obj = CareTeam.objects.get(pk=id)
                    print(obj)
                    item.care_teams.add(obj)
                except:
                    pass
            
        if diagnoses is not None:
            for id in list(diagnoses[0].split(',')):
                try:
                    obj = DiagnosisInformation.objects.get(pk=id)
                    item.diagnoses.add(obj)
                except:
                    pass
            
        if support_info is not None:
            for id in list(support_info[0].split(',')):
                try:
                    obj = SupportingInfo.objects.get(pk=id)
                    item.support_info.add(obj)
                except:
                    pass
        
        return item

class ClaimSerializer(serializers.ModelSerializer):
    care_team = CareTeamSerializer(many=True,read_only=True)
    diagnosis_information = DiagnosisInformationSerializer(many=True,read_only=True)
    supporting_info = SupportingInfoSerializer(many=True,read_only=True)
    items = ItemsSerializer(many=True,read_only=True)
    
    care_teams_ids = serializers.ListField(write_only=True)
    diagnoses_ids = serializers.ListField(write_only=True)
    support_info_ids = serializers.ListField(write_only=True)
    items_ids = serializers.ListField(write_only=True)
    
    class Meta:
        model = Claim
        fields = '__all__'
        
    def create(self, validated_data):
        care_teams = validated_data.pop("care_teams_ids", None)
        diagnoses = validated_data.pop("diagnoses_ids", None)
        support_info = validated_data.pop("support_info_ids", None)
        items = validated_data.pop("items_ids", None)

        claim = Claim.objects.create(**validated_data)
        
        if care_teams is not None:
            for id in list(care_teams[0].split(',')):
                try:
                    obj = CareTeam.objects.get(pk=id)
                    print(obj)
                    claim.care_team.add(obj)
                except:
                    pass
            
        if diagnoses is not None:
            for id in list(diagnoses[0].split(',')):
                try:
                    obj = DiagnosisInformation.objects.get(pk=id)
                    claim.diagnosis_information.add(obj)
                except:
                    pass
            
        if support_info is not None:
            for id in list(support_info[0].split(',')):
                try:
                    obj = SupportingInfo.objects.get(pk=id)
                    claim.supporting_info.add(obj)
                except:
                    pass
        if items is not None:
            for id in list(items[0].split(',')):
                try:
                    obj = Items.objects.get(pk=id)
                    claim.items.add(obj)
                except:
                    pass
        
        return claim