from rest_framework import serializers

from Laboratory.administration.models import *



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DictionarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'

class OrganizationTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'

class OrganizationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class PanelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = '__all__'

class PanelItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = PanelItem
        fields = '__all__'

class ResultLimitSerializers(serializers.ModelSerializer):
    class Meta:
        model = ResultLimit
        fields = '__all__'

class SiteInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteInformation
        fields = '__all__'

class SampleEntryConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = SampleEntryConfig
        fields = '__all__'

class PrintedReportsConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = SampleEntryConfig
        fields = '__all__'

class TestResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'
class SampleTypePanelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SampleTypePanel
        fields = '__all__'

class SampleTypeTestSerializers(serializers.ModelSerializer):
    class Meta:
        model = SampleTypeTest
        fields = '__all__'