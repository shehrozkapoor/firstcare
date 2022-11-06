<template>
    <div class="grid">
        <div class="col-3 surface-200 shadow-8 mr-2">
            <div class="grid col-12 w-full">
                <div class="col-4">
                    <label class="text w-full">Medication</label>
                </div>
                <div class="col-8">
                    <InputText :disabled="true" v-model="medication_input" class="w-full"/>
                </div>
            </div>
            <div class="grid col-12 w-full">
                <div class="col-3">
                    <label for="" class="text">Order Type:</label>
                </div>
                <div class="col-9">
                    <TextArea disabled :autoResize="true" class="disabled-text-area w-full" />
                    </div>
        </div>
        <div class="col-12">
            <CustomSelect :items="items" class="w-full"/>
        </div>
        <div class="grid col-12">
            <div class="col-3">
                <label for="" class="text">Routine Dose:</label>
            </div>
            <div class="col-4">
                <CustomInput disabled="true" class="auto-input-select-measurement w-full"/>
            </div>
            <div class="col-5">
                <CustomSelect :items="items" class="auto-input-select-measurement w-full"/>
            </div>
        </div>
        <div class="col-12">
            <CustomInput type="number" value=0 class="auto-input-select-measurement"/>
        </div>
        <div class="grid col-12">
            <div class="col-3">
                <label for="" class="text">Route</label>
            </div>
            <div class="col-9">
                <CustomSelect :items="items" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-3">
                <label for="" class="text">Direction</label>
            </div>
            <div class="col-9">
                <CustomSelect :items="items" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-3">
                <label for="" class="text">Indication</label>
            </div>
            <div class="col-9">
                <CustomSelect :items="items" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-3">
                <label for="" class="text">Start Date</label>
            </div>
            <div class="col-9">
                <CustomSelect :items="items" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-2">
                <CustomInput type="checkbox" class="auto-input-select-measurement"/>
            </div>
            <div class="col-3">
                <label for="" class="text">Duration (Days)</label>
            </div>
            <div class="col-7">
                <CustomSelect :items="items" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-2">
                <CustomInput type="checkbox" class="auto-input-select-measurement"/>
            </div>
            <div class="col-3">
                <label for="" class="text">Total Doses</label>
            </div>
            <div class="col-7">
                <CustomInput type="number" value="1" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-2">
                <CustomInput type="checkbox" class="auto-input-select-measurement"/>
            </div>
            <div class="col-3">
                <label for="" class="text">Total Doses</label>
            </div>
            <div class="col-7">
                <CustomInput type="number" value="1" class="auto-input-select-measurement"/>
            </div>
        </div>
        <div class="grid col-12">
            <div class="col-12">
                <label for="" class="text">Customize Dose Schedule</label>
            </div>
            <div class="col-12">
                <v-textarea background-color="white" color="transparent" label="Remarks" height="200"></v-textarea>
            </div>
        </div>
    </div>
    <div class="grid col-9">
        <CustomDataTable sortable="true" :table_columns="table_columns" :table_data="table_data" title="Prescription" class="w-full"/>
    </div>
    </div>
</template>

<script>
import CustomSelect from '@/components/Custom/CustomSelect.vue';
import CustomInput from '@/components/Custom/CustomInput.vue';
import CustomDataTable from '@/components/Custom/CustomDataTable.vue';

export default {
    name:"Prescription",
    components:{
        CustomSelect,
        CustomInput,
        CustomDataTable
    },
    data(){
        return{
            medication_input:"",
            items:[1,2,4],
            table_headers:['header 1','header 2','header 3','header 4'],
            table_columns:[
                {
                    'field':'id',
                    'header':'ID'
                },
                {
                    'field':'description',
                    'header':'Description'
                },
            ],
            table_data:[
                {
                    "id":"1",
                    "description":"test"
                }
            ]
        }
    }
}
</script>
