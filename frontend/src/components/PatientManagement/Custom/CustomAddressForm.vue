<template>
    <div class="grid mt-4 p-3">
        <CustomTitleHeader title="Address Information"/>
        <div class="grid col-6">
            <div class="col-12">
                <label for="Country">Country</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-12">
                <label for="city">City</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-12">
                <label for="area">Area</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-6">
                <label for="PO Box">P.O. Box</label>
                <CustomInput placeholder="P.O. Box" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="Zip Code">Zip Code</label>
                <CustomInput placeholder="Zip Code" type="text" class="w-full" />
            </div>
        </div>
        <div class="col-6">
                <div class="field-checkbox col-12 mt-3">
                    <Checkbox name="ivr-call" value="ivr-call" v-model="gender" />
                    <label for="ivr-call">Stop IVR Call</label>
                </div>
                <div class="grid col-12">
                <div class="col-5">
                    <label for="Permanent Address">Permanent Address</label>
                    <Textarea v-model="value" rows="5" cols="30" />
                </div>
                <div class="col-5 col-offset-2">
                    <label for="Temporary Address">Temporary Address</label>
                    <Textarea v-model="value" rows="5" cols="30" />
                </div>
                </div>
            </div>
    </div>
</template>

<script>
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomTitleHeader from '@/components/PatientManagement/Custom/CustomTitleHeader.vue'

export default {
    name:"CustomAddressForm",
    components:{
        CustomInput,
        CustomSelect,
        CustomTitleHeader
    },
    data(){
        return{
            items:[1,2,3],
        }
    }
}
</script>