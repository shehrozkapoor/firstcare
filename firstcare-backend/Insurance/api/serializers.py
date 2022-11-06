from asyncore import read, write
from Insurance.models import *
from rest_framework import serializers


class InsuranceUserPermisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceUserPermision
        fields = '__all__'

class InsuranceUserRolesSerializer(serializers.ModelSerializer):
    permisions = InsuranceUserPermisionSerializer(read_only=True,many=True)
    permissions_id = serializers.ListField(write_only=True)

    class Meta:
        model = InsuranceUserRoles
        fields = '__all__'

    def create(self, validated_data):
        
        permissions_id = validated_data.pop('permissions_id',None)

        instance = InsuranceUserRoles.objects.create(**validated_data)
        if permissions_id is not None:
            for id in list(permissions_id[0].split(',')):
                permision = InsuranceUserPermision.objects.get(pk=id)
                instance.permisions.add(permision)
        return instance

class InsuranceUserSerializer(serializers.ModelSerializer):
    role = InsuranceUserRolesSerializer(read_only=True,many=True)
    role_id = serializers.ListField(write_only=True)

    class Meta:
        model = InsuranceUser
        fields = '__all__'
    
    def create(self, validated_data):
        role_id = validated_data.pop('role_id',None)

        instance = InsuranceUser.objects.create(**validated_data)
        if role_id is not None:
            for id in list(role_id[0].split(',')):
                role = InsuranceUserRoles.objects.get(pk=id)
                instance.role.add(role)

        return instance

class FamilyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyType
        fields = '__all__'


class ConfirmationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationType
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = '__all__'

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdType
        fields = '__all__'

class HeadInsureeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadInsuree
        fields = '__all__'

class HealthFacilityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilityLevel
        fields = '__all__'

class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = '__all__'

class FirstServicePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstServicePoint
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class InsureeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insuree
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class PolicyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDetails
        fields = '__all__'

class DeductableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deductable
        fields = '__all__'

class RemuneratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remunerated
        fields = '__all__'

class PoliciesValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliciesValues
        fields = '__all__'

class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'

class ContributionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionCategory
        fields = '__all__'

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

class LegalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalForm
        fields = '__all__'

class ActivityCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCode
        fields = '__all__'

class PolicyHoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHolders
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

