from rest_framework import serializers
from Insurance.insurance_administration.models import *



class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class InsureeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insuree
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class ExtraMemberCeilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraMemberCeiling
        fields = '__all__'

class MaximumCeilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaximumCeiling
        fields = '__all__'

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'

class CeilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceiling
        fields = '__all__'

class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class SubLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLevel
        fields = '__all__'

class CapitationPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitationPayment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class HealthFacilityLegalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilityLegalForm
        fields = '__all__'

class HealthFacilitySubLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilitySubLevel
        fields = '__all__'

class CareTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareType
        fields = '__all__'

class ServicesPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPriceList
        fields = '__all__'

class ItemPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPriceList
        fields = '__all__'

class HealthFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacilities
        fields = '__all__'

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLevel
        fields = '__all__'

class MedicalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalServices
        fields = '__all__'

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'

class MedicalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalItem
        fields = '__all__'

class MedicalServicesPriceListSerializer(serializers.ModelSerializer):
    services = MedicalServicesSerializer(read_only=True,many=True)
    services_id = serializers.ListField(write_only=True)

    class Meta:
        model = MedicalServicesPriceList
        fields = '__all__'

    def create(self, validated_data):
        services_id = validated_data.pop('services_id',None)

        instance = MedicalServicesPriceList.objects.create(**validated_data)
        if services_id is not None:
            for id in list(services_id[0].split(',')):
                type = MedicalServices.objects.get(pk=id)
                instance.services.add(type)
        return instance

class MedicalItemsPriceListSerializer(serializers.ModelSerializer):
    items = MedicalItemSerializer(read_only=True,many=True)
    items_id = serializers.ListField(write_only=True)

    class Meta:
        model = MedicalItemsPriceList
        fields = '__all__'

    def create(self, validated_data):
        items_id = validated_data.pop('items_id',None)

        instance = MedicalItemsPriceList.objects.create(**validated_data)
        if items_id is not None:
            for id in list(items_id[0].split(',')):
                type = MedicalItem.objects.get(pk=id)
                instance.items.add(type)
        return instance

class PayerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayerType
        fields = '__all__'

class PayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = '__all__'

class CalculationRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationRules
        fields = '__all__'

class ContributionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionPlan
        fields = '__all__'