from management.ward_management.models import *
from rest_framework import serializers


class bedTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bedTags
        fields = '__all__'


class bedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = bedType
        fields = '__all__'


class BedLayoutSerializer(serializers.ModelSerializer):
    tags = bedTagsSerializer(read_only=True)
    type = bedTypeSerializer(read_only=True)

    tags_id = serializers.IntegerField(write_only=True)
    type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BedLayout
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    layout = BedLayoutSerializer(read_only=True)
    layout_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Room
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    hospital = HospitalSerializer(read_only=True)
    hospital_id = serializers.IntegerField(write_only=True)
    room_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Ward
        fields = '__all__'
