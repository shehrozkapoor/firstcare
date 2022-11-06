from rest_framework import serializers
from Patient_health_record.models import *
from Laboratory.administration.models import TestResult
from Laboratory.api.serializers import AvailableTestsSerializer
from Laboratory.administration.api.serializers import TestResultSerializers


class DosageInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageInstruction
        fields = '__all__'

class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = '__all__'

class EncounterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncounterType
        fields = '__all__'

class ChiefComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiefComplain
        fields = '__all__'

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = '__all__'

class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = '__all__'

class ProblemListSerializer(serializers.ModelSerializer):
    problem = ProblemsSerializer(read_only=True,many=True)
    problem_id = serializers.ListField(write_only=True)

    class Meta:
        model = ProblemList
        fields = '__all__'
    
    def create(self, validated_data):
        problem_list = validated_data.pop('problem_id',None)
        obj = ProblemList.objects.create(**validated_data)
        if problem_list is not None:
            for id in list(problem_list[0].split(',')):
                type = Problems.objects.get(pk=id)
                obj.problem.add(type)
        return obj

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class HistoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryType
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class ReviewOfSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewOfSystem
        fields = '__all__'

class PhysicalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalExam
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    test = AvailableTestsSerializer(read_only=True,many=True)
    test_id = serializers.ListField(write_only=True)

    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        test_id = validated_data.pop('test_id',None)
        obj = Order.objects.create(**validated_data)
        if test_id is not None:
            for id in list(test_id[0].split(',')):
                type = AvailableTests.objects.get(pk=id)
                obj.test.add(type)
        return obj

class AssessmentAndPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentAndPlan
        fields = '__all__'

class ProgressNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressNote
        fields = '__all__'

class EncounterSerializer(serializers.ModelSerializer):
    home_medication = DosageInstructionSerializer(read_only=True,many=True)
    home_medication_id = serializers.ListField(write_only=True)

    document = DocumentSerializer(read_only=True,many=True)
    document_id = serializers.ListField(write_only=True)

    lab_result = TestResultSerializers(read_only=True,many=True)
    lab_result_id = serializers.ListField(write_only=True)

    history = HistorySerializer(read_only=True,many=True)
    history_id = serializers.ListField(write_only=True)

    assessment_and_plan = AssessmentAndPlanSerializer(read_only=True,many=True)
    assessment_and_plan_id = serializers.ListField(write_only=True)

    class Meta:
        model = Encounter
        fields = '__all__'

    
    def create(self, validated_data):
        home_medication_id = validated_data.pop('home_medication_id',None)
        document_id = validated_data.pop('document_id',None)
        lab_result_id = validated_data.pop('lab_result_id',None)
        history_id = validated_data.pop('history_id',None)
        assessment_and_plan_id = validated_data.pop('assessment_and_plan_id',None)



        obj = Encounter.objects.create(**validated_data)
        
        if home_medication_id is not None:
            for id in list(home_medication_id[0].split(',')):
                type = DosageInstruction.objects.get(pk=id)
                obj.home_medication.add(type)
        
        if document_id is not None:
            for id in list(document_id[0].split(',')):
                type = Document.objects.get(pk=id)
                obj.document.add(type)
        
        if lab_result_id is not None:
            for id in list(lab_result_id[0].split(',')):
                print(id)
                type = TestResult.objects.get(pk=id)
                obj.lab_result.add(type)
        
        if history_id is not None:
            for id in list(history_id[0].split(',')):
                type = History.objects.get(pk=id)
                obj.history.add(type)
        
        if assessment_and_plan_id is not None:
            for id in list(assessment_and_plan_id[0].split(',')):
                type = AssessmentAndPlan.objects.get(pk=id)
                obj.assessment_and_plan.add(type)
        return obj







