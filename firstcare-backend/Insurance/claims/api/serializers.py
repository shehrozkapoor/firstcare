from asyncore import write
from rest_framework import serializers
from Insurance.claims.models import *


class ClaimServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimServices
        fields = '__all__'

class ClaimItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimItems
        fields = '__all__'

class ClaimsSerializer(serializers.ModelSerializer):
    medical_services = ClaimServicesSerializer(read_only=True,many=True)
    medical_items = ClaimItemsSerializer(read_only=True,many=True)

    medical_services_id = serializers.ListField(write_only=True,required=False)
    medical_items_id = serializers.ListField(write_only=True,required=False)

    class Meta:
        model = Claims
        fields = '__all__'
    

    def create(self, validated_data):
        medical_services_id = validated_data.pop('medical_services_id',None)
        medical_items_id = validated_data.pop('medical_items_id',None)

        instance = Claims.objects.create(**validated_data)
        if medical_services_id is not None:
            for id in list(medical_services_id[0].split(',')):
                obj = ClaimServices.objects.get(pk=id)
                instance.medical_services.add(obj)
        if medical_items_id is not None:
            for id in list(medical_items_id[0].split(',')):
                obj = ClaimItems.objects.get(pk=id)
                instance.medical_items.add(obj)
        return instance
    
    def update(self,instance,validated_data):
        medical_services_id = validated_data.pop('medical_services_id',None)
        medical_items_id = validated_data.pop('medical_items_id',None)
        submitted = validated_data.pop('submitted',None)

        print(submitted)
        if submitted is not None:
            instance.submitted = submitted
            instance.save()
        
        if medical_services_id is not None:
            for id in list(medical_services_id[0].split(',')):
                obj = ClaimServices.objects.get(pk=id)
                instance.medical_services.add(obj)
        if medical_items_id is not None:
            for id in list(medical_items_id[0].split(',')):
                obj = ClaimItems.objects.get(pk=id)
                instance.medical_items.add(obj)
        return instance