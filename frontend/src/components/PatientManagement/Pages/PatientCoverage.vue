<template>
<form action="">
    <div class="grid mt-4 p-3">
        <div class="col-12">
            <CustomTitleHeader title="Patient Coverage Information" />
        </div>
        <div class="col-6">
            <CustomAutoComplete class="w-full" placeholder="Search Patient By Name or ID.."/>
        </div>
        <div class="grid col-6">
            <div class="col-1 pt-3 pl-3 font-bold">
                <label for="status">Status</label>
            </div>
            <div class="col-10">
                <CustomSelect class="w-full" :items="status" />
            </div>
        </div>
        <div class="col-3">
            <label for="coverage-type" class="font-bold ml-3 mb-2">Coverage Type</label>
            <CustomSelect class="w-full" :items="coverage_type" />
        </div>
        <div class="col-3">
            <label for="subscriber" class="font-bold mb-2">Subscriber</label>
            <CustomAutoComplete class="w-full" placeholder="Search Subscriber By Name or ID.."/>
        </div>
        <div class="col-3">
            <label for="subscriber-id" class="font-bold ml-3 mb-2">Subscriber Id</label>
            <CustomInput class="w-full" placeholder="subscriber-id" type="text"/>
        </div>
        <div class="col-3">
            <label for="beneficiary" class="font-bold mb-2">Beneficiary</label>
            <CustomAutoComplete class="w-full" placeholder="Search Beneficiary By Name or ID.."/>
        </div>
        <div class="col-3">
            <label for="relation" class="font-bold ml-3">Dependent no</label>
            <CustomInput placeholder="Dependent no.." type="text" class="w-full" />
        </div>
        <div class="grid col-3">
            <label for="relation" class="font-bold">Relationship</label>
            <CustomInput placeholder="relationship with subscriber" type="text" class="w-full" />
        </div>
        <div class="grid col-6 mt-3">
            <CustomPeriod />
        </div>
        <div class="col-3">
            <label for="Payor" class="font-bold mb-2">Payor</label>
            <CustomAutoComplete class="w-full" placeholder="Search Payor By Name or ID.."/>
        </div>
    </div>
    <hr>
    <div class="grid mt-4 p-3">
        <div class="col-12">
            <CustomTitleHeader title="Additional Coverage Information" />
        </div>
        <div class="grid col-12">
            <div class="grid col-7 ">
                <div class="col-12">
                    <label for="additional-type" class="font-bold ml-3 mb-2">Type</label>
                    <CustomSelect class="w-full" :items="additional_type" />
                </div>
                <div class="col-12">
                    <label for="additional-value" class="font-bold ml-3 mb-2">Value</label>
                    <CustomInput placeholder="value.." type="text" class="w-full" />
                </div>
            </div>
            <div class="grid col-4 col-offset-1">
                <Textarea v-model="value" rows="5" cols="30" placeholder="description"/>
            </div>
        </div>
        <div class="field-checkbox col-2 mt-4">
                <Checkbox name="subrogation" value="subrogation" v-model="subrogation" />
                <label for="patient-pregnant">Subrogation</label>
        </div>
        <div class="col-4 mt-2">
            <CustomAutoComplete class="w-full" placeholder="Search Contract By Id.."/>
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
    name:"RegisterPatientCoverage",
    components:{
        CustomTitleHeader,
        CustomAutoComplete,
        CustomSelect,
        CustomInput,
        CustomPeriod
    },
    data(){
        return{
            status:['active','cancelled ','draft','entered-in-error'],
            coverage_type:['type 1','type 2','type 3 ','type 4'],
            additional_type:['group','plan'],
            subrogation:''
        }
    }
}
</script>