<template>
    <form action="">
        <div class="grid mt-4 p-3">
            <div class="col-12">
                <CustomTitleHeader title="Patient Insurance Information" />
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
            <div class="grid col-6 mt-2">
                <CustomPeriod />
            </div>
            <div class="col-6">
                <label for="name" class="font-bold ml-3 mb-2">Insurance Organization</label>
                <CustomSelect class="w-full" :items="company" />
            </div>
            <div class="col-6">
                <label for="name" class="font-bold ml-3 mb-2">Coverage Area</label>
                <CustomSelect class="w-full" :items="location" />
            </div>
            <div class="col-3">
                <label for="name" class="font-bold ml-3 mb-2">Coverage Type</label>
                <CustomSelect class="w-full" :items="coverage_type" />
            </div>
            <div class="col-3">
                <label for="name" class="font-bold ml-3 mb-2">Plan Type</label>
                <CustomSelect class="w-full" :items="plan_type" />
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
    name:"RegistrationInsuranceInformation",
    components:{
        CustomTitleHeader,
        CustomAutoComplete,
        CustomSelect,
        CustomInput,
        CustomPeriod
    },
    data(){
        return{
            status:['draft','active','retired ','unknown'],
            company:['company 1','company 2','company 3 ','company 4'],
            coverage_type:['type 1','type 2','type 3 ','type 4'],
            location:['location 1','location 2','location 3 ','location 4'],
            plan_type:['plan 1','plan 2','plan 3 ','plan 4'],

        }
    }
}
</script>