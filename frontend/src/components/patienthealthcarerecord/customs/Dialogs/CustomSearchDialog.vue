<template>
    <Dialog v-model:visible="display" position="top">
        <template #header>
            <h3>{{header}}</h3>
        </template>

        <div class="formgrid grid">
            <div class="col-6">
                <div class="field col" inline>
                    <label for="">Search</label>
                    <CustomInput placeholder="Search..." class="w-full" />
                </div>
            </div>
            <div class="col-3">
                <div class="field col">
                    <label for="">search type</label>
                    <CustomSelect class="w-full" :items="items" />
                </div>
            </div>
            <div class="col-3">
                <div class="field col">
                    <label for="">Within:</label>
                    <CustomSelect class="w-full" :items="items" />
                </div>
            </div>
            <div class="col-12">
                <div class="field col">
                    <Button label="Search" class="w-full"/>
                </div>
            </div>
        </div>

        <CustomDataTable :multipleSelect="false" :table_columns="table_columns" :table_data="table_data" title="Problem" sortable="true"/>
        <template #footer>
            <Button label="Ok" icon="pi pi-check" autofocus />
            <Button label="cancel" icon="pi pi-times" class="p-button-text p-button-danger" @click="HideDialog" />
        </template>
    </Dialog>

</template>

<script>
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'

export default {
    name:"CustomSearchDialog",
    components:{
        CustomDataTable,
        CustomInput,
        CustomSelect
    },
    props:['display','header'],
    data() {
        return {
            items: [1, 2, 3],
            table_data: [{
                "term": "HTN [hypertension]",
                "code": "401.9",
                "terminology": "ICD-9-CM",
                "terminology-axis": "IMO Disease & Injuries",
            }],
            table_columns: [{
                    'field': "term",
                    "header": "Term"
                },
                {
                    'field': "code",
                    "header": "Code"
                },
                {
                    'field': "terminology",
                    "header": "Terminology"
                },
                {
                    'field': "terminology-axis",
                    "header": "Terminology Axis"
                },
            ],
        }
    }
}
</script>