from rest_framework import serializers
from management.bed_management.models import *

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
