from asyncore import write
from dataclasses import field
from datetime import timedelta
from management.schedule_management.models import *
from rest_framework import serializers


class AppointmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentType
        fields = '__all__'




class SlotSerializer(serializers.ModelSerializer):
    # provider = ProviderAvailSerializer(read_only=True)
    # provider_id = serializers.IntegerField(write_only=True)
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Slot
        fields = '__all__'



class AppointmentSerializer(serializers.ModelSerializer):
    slot = SlotSerializer(read_only=True)
    slot_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        slot_id = validated_data.pop('slot_id',None)
        slot = Slot.objects.get(id=slot_id)
        typeObj = Appointment.objects.create(**validated_data)
        typeObj.slot=slot
        typeObj.save()
        return typeObj


class ProviderAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAvail
        fields = '__all__'
    
    def create(self, validated_data):
        available_types_list = validated_data.pop('available_types',None)
        typeObj = ProviderAvail.objects.create(**validated_data)
        for available_type in available_types_list:
            typeObj.available_types.add(available_type)
        difference = (typeObj.end_date - typeObj.start_date)
        total_hours = int(difference.total_seconds()//3600)
        previous_time=typeObj.start_date
        for i in range(0,total_hours):
            Slot.objects.create(provider=typeObj,start_time=previous_time,end_time=(previous_time+timedelta(hours=1)))
            previous_time=previous_time+timedelta(hours=1)
        return typeObj