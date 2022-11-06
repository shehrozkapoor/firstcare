from rest_framework import serializers
from billing.models import *
from Patient.api.serializers import PatientSerializer
from management.schedule_management.api.serializers import AppointmentSerializer
from FHIR.api.serializers import *
'''
all the serializers for the billing model are present here
if you can see PaymentSerializer is little different then other serializers because
payment model contains manyToManyField so that's why
'''


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(read_only=True)
    type = PaymentTypeSerializer(read_only=True)
    method = PaymentMethodSerializer(read_only=True)

    appointment_id = serializers.IntegerField(write_only=True)
    type_id = serializers.IntegerField(write_only=True)
    method_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
    def create(self,validate):
        appointment_id = validate.pop('appointment_id',None)
        type_id = validate.pop('type_id',None)
        method_id = validate.pop('method_id',None)


        appointment = Appointment.objects.get(id=appointment_id)
        payment_type = PaymentType.objects.get(id=type_id)
        payment_method = PaymentMethod.objects.get(id=method_id)

        obj = Payment.objects.create(**validate)
        obj.appointment = appointment
        obj.type = payment_type
        obj.method = payment_method
        obj.save()
        return obj

class PaymentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProfile
        fields = '__all__'

class OnsetDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnsetDataType
        fields = '__all__'

class OtherDateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDateType
        fields = '__all__'

class HcfaBOXSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcfaBOX
        fields = '__all__'

class ICD10Serializer(serializers.ModelSerializer):
    class Meta:
        model = ICD10
        fields = '__all__'

class ICD9Serializer(serializers.ModelSerializer):
    class Meta:
        model = ICD9
        fields = '__all__'

class CPTITEMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPTITEM
        fields = '__all__'

class CPTCODESerializer(serializers.ModelSerializer):
    class Meta:
        model = CPTCODE
        fields = '__all__'

class HCPCSSerializer(serializers.ModelSerializer):
    class Meta:
        model = HCPCS
        fields = '__all__'

class HCPCSCODESerializer(serializers.ModelSerializer):
    class Meta:
        model = HCPCSCODE
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    patient =  PatientSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True,many=True)
    payment_profile = PaymentProfileSerializer(read_only=True,many=True)
    icd_10 = ICD10Serializer(read_only=True,many=True)
    icd_9 = ICD9Serializer(read_only=True,many=True)
    cpt_code = CPTCODESerializer(read_only=True,many=True)
    hcpcs_code = HCPCSCODESerializer(read_only=True,many=True)
    eligibility_bundle = CoverageEligibilityBundleSerializer(read_only=True)
    pre_auth_bundle = PreAuthBundleSerializer(read_only=True)
    claim_bundle = ClaimBundleSerializer(read_only=True)
    claim_bundle = ClaimBundleSerializer(read_only=True)
    communication_bundle = CommunicationBundleSerializer(read_only=True)
    payment_reconciliation_bundle = PaymentReconciliationBundleSerializer(read_only=True)
    payment_notice_bundle = PaymentNoticeBundleSerializer(read_only=True)
    payment_notice_bundle = PaymentNoticeBundleSerializer(read_only=True)
    payment_cancel_bundle = TaskBundleSerializer(read_only=True)
    payment_status_bundle = TaskBundleSerializer(read_only=True)
    payment_poll_bundle = TaskBundleSerializer(read_only=True)

    patient_id = serializers.CharField(write_only=True,required=True)
    payment_id = serializers.ListField(write_only=True,required=False)
    payment_profile_id = serializers.ListField(write_only=True,required=False)
    icd_10_id = serializers.ListField(write_only=True,required=False)
    cpt_code_id = serializers.ListField(write_only=True,required=False)
    hcpcs_code_id = serializers.ListField(write_only=True,required=False)
    creation_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)

    class Meta:
        model = Billing
        fields = '__all__'

    def create(self, validated_data):

        patient_id = validated_data.pop('patient_id',None)
        payment_id = validated_data.pop('payment_id',None)
        payment_profile_id = validated_data.pop('payment_profile_id',None)
        icd_10_id = validated_data.pop('icd_10_id',None)
        icd_9_id = validated_data.pop('icd_9_id',None)
        cpt_code_id = validated_data.pop('cpt_code_id',None)
        hcpcs_code_id = validated_data.pop('hcpcs_code_id',None)

        instance = Billing.objects.create(**validated_data)

        if patient_id is not None:
            patient = Patient.objects.get(pk=patient_id)
            instance.patient = patient
        if payment_id is not None:
            for id in list(payment_id[0].split(',')):
                try:
                    id = int(id)
                    print(id)
                    obj = Payment.objects.get(pk=id)
                    instance.payment.add(obj)
                except:
                    pass
        if payment_profile_id is not None:
            for id in list(payment_profile_id[0].split(',')):
                try:
                    obj = PaymentProfile.objects.get(pk=id)
                    instance.payment_profile.add(obj)
                except:
                    pass
        if icd_10_id is not None:
            for id in list(icd_10_id[0].split(',')):
                try:
                    id = int(id)
                    obj = ICD10.objects.get(pk=id)
                    instance.icd_10.add(obj)
                except:
                    pass
        if cpt_code_id is not None:
            for id in list(cpt_code_id[0].split(',')):
                try:
                    id = int(id)
                    obj = CPTCODE.objects.get(pk=id)
                    instance.cpt_code.add(obj)
                except:
                    pass
        if hcpcs_code_id is not None:
            for id in list(hcpcs_code_id[0].split(',')):
                try:
                    id = int(id)
                    obj = HCPCSCODE.objects.get(pk=id)
                    instance.hcpcs_code.add(obj)
                except:
                    pass
        instance.save()
        return instance