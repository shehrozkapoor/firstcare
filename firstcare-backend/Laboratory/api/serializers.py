from dataclasses import field
from re import I
from rest_framework import serializers
from Laboratory.models import *




class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = '__all__'

class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasure
        fields = '__all__'

class AvailableTestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailableTests
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    tests = AvailableTestsSerializer(read_only=True,many=True)
    available_tests_list = serializers.ListField(write_only=True)

    class Meta:
        model = Sample
        fields = '__all__'
    
    def create(self, validated_data):
        available_tests_list = validated_data.pop('available_tests_list',None)

        obj = Sample.objects.create(**validated_data)
        if available_tests_list is not None:
            for id in list(available_tests_list[0].split(',')):
                type = AvailableTests.objects.get(pk=id)
                obj.tests.add(type)
        return obj

class refusalReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = refusalReason
        fields = '__all__'


class NonConformitySerializer(serializers.ModelSerializer):
    reason = refusalReasonSerializer(read_only=True,many=True)
    reason_list = serializers.ListField(write_only=True)

    class Meta:
        model = NonConformity
        fields = '__all__'
    
    def create(self, validated_data):
        reason_list = validated_data.pop('reason_list',None)
        obj = NonConformity.objects.create(**validated_data)
        if reason_list is not None:
            for id in list(reason_list[0].split(',')):
                type = refusalReason.objects.get(pk=id)
                obj.reason.add(type)
        return obj



