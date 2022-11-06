<template>
<form action="">
    <div class="grid mt-4 p-3">
        <div class="col-12">
            <CustomTitleHeader title="Patient Encounter Information" />
        </div>
        <div class="col-6">
            <CustomAutoComplete class="w-full" placeholder="Search Patient By Name or ID.."/>
        </div>
        <div class="grid col-6">
            <div class="col-2 pt-3 pl-3 font-bold">
                <label for="location">Location</label>
            </div>
            <div class="col-8">
                <CustomSelect class="w-full" :items="location" />
            </div>
        </div>
        <div class="col-3">
            <label for="encounter#" class="font-bold pl-2">Encounter No.</label>
            <CustomInput class="w-full" placeholder="Encounter #.."/>
        </div>
        <div class="col-3">
            <label for="visit-reason" class="font-bold pl-2">Visit Reason</label>
            <CustomInput class="w-full" placeholder="Visit Reason.."/>
        </div>
        <div class="col-3">
            <label for="location" class="pl-2 font-bold">Admit Date time</label>
            <Calendar v-model="admit_date" class="w-full" placeholder="Admit Datetime" showTime="true" hourFormat="12"  />
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Patient Type</label>
            <CustomSelect :items="patient_type" class="w-full"/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Admit Source</label>
            <CustomSelect :items="admit_source" class="w-full"/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Medical Service</label>
            <CustomSelect :items="medical_service" class="w-full"/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Financial Class</label>
            <CustomSelect :items="patient_type" class="w-full"/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Room</label>
            <CustomInput class="w-full" placeholder="Room.."/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Bed</label>
            <CustomInput class="w-full" placeholder="Bed.."/>
        </div>
        <div class="col-3">
            <label for="location" class="font-bold pl-2">Discharge Date</label>
            <Calendar v-model="discharge_date" class="w-full" placeholder="Discharge Datetime" showTime="true" hourFormat="12"  />
        </div>
        <div class="col-12">
            <label for="location" class="font-bold pl-2">Provider Relationship</label>
            <CustomAutoComplete class="w-full" placeholder="Search Name.."/>
        </div>
    </div>
    <Button class="w-full" label="Submit" type="submit"></Button>
</form>
</template>

<script>
import CustomTitleHeader from '@/components/PatientManagement/Custom/CustomTitleHeader.vue'
import CustomAutoComplete from '@/components/Custom/CustomAutoComplete.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomPeriod from '@/components/PatientManagement/Custom/CustomPeriod.vue'

export default {
    name:"RegisterEncounterInformation",
    components:{
        CustomTitleHeader,
        CustomAutoComplete,
        CustomSelect,
        CustomInput,
        CustomPeriod
    },
    data(){
        return{
            location:['location 1','location 2','location 3 ','location 4'],
            patient_type:['inpatient','outpatient'],
            admit_date:'',
            admit_source:['source 1','source 2'],
            medical_service:['service 1','service 2'],
            discharge_date:''
        }
    }
}
</script>