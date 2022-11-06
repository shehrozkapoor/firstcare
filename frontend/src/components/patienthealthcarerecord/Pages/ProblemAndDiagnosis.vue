<template>
   <div class="diagnosis h-30rem overflow-x-scroll overflow-y-scroll">
    <CustomDiagnosisDialog :display="diagnosisDialog" header="Diagnosis" class="w-11"/>
   <Toolbar class="sticky top-0 font-bold text-white p-4 w-full">
        <template #start>
            <Button label="Add" icon="pi pi-plus" class="mr-2 p-button-text" @click="diagnosisDialog=!diagnosisDialog"/>
            <Button label="Modify" icon="pi pi-pencil" class="mr-2 p-button-text p-button-warning"/>
        </template>
    </Toolbar>
    <CustomDataTable :table_data="table_data.diagnosis" :table_columns="columns.diagnosis" title='Diagnosis' :multipleSelect="false"/>
    </div>
   <div class="diagnosis h-30rem overflow-x-scroll overflow-y-scroll">
    <CustomProblemDialog :display="problemDialog" header="Problem"  class="w-11"/>
   <Toolbar class="sticky top-0 font-bold text-white p-4 w-full">
        <template #start>
            <Button label="Add" icon="pi pi-plus" class="mr-2 p-button-text" @click="problemDialog=!problemDialog"/>
            <Button label="Modify" icon="pi pi-pencil" class="mr-2 p-button-text p-button-warning"/>
        </template>
    </Toolbar>
    <CustomDataTable :table_data="table_data.problem" :table_columns="columns.problem" title='Problem' :multipleSelect="false"/>
    </div>
</template>


<script>
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
import CustomDiagnosisDialog from '@/components/patienthealthcarerecord/customs/Dialogs/CustomDiagnosisDialog.vue'
import CustomProblemDialog from '@/components/patienthealthcarerecord/customs/Dialogs/CustomProblemDialog.vue'

export default {
    name:"ProblemAndDiagnosis",
    components: {
        CustomDataTable,
        CustomDiagnosisDialog,
        CustomProblemDialog
    },
    data(){
        return {
            diagnosisDialog:false,
            problemDialog:false,
            columns: {
                "diagnosis":[
                    {
                        'field':"clinical-dx",
                        "header":"Clinical Dx"
                    },
                    {
                        'field':"date",
                        "header":"Date"
                    },
                    {
                        'field':"dx-type",
                        "header":"Dx Type"
                    },
                    {
                        'field':"code",
                        "header":"Code"
                    },
                    {
                        'field':"vocabulary",
                        "header":"Vocabulary"
                    },
                    {
                        'field':"last-reviewed",
                        "header":"Last Reviewed"
                    },
                    {
                        'field':"condition-named",
                        "header":"Condition Named"
                    },
                    {
                        'field':"service-type",
                        "header":"Service Type"
                    }
                ],
                "problem":[
                    {
                        'field':"name-of-problem",
                        "header":"Name Of Problem"
                    },
                    {
                        'field':"on-set-date",
                        "header":"Onset Date"
                    },
                    {
                        'field':"life-cycle",
                        "header":"Life Cycle"
                    },
                    {
                        'field':"responsible-provider",
                        "header":"Responsible Provider"
                    },
                ]
            },
            table_data: {
                "diagnosis": [
                    {
                        "clinical-dx":"COPD",
                        "date": "03/24/2022",
                        "dx-type": "Working",
                        "code": "496",
                        "vocabulary":"ICD-9_CM",
                        "last-reviewed":"",
                        "condition-named":"",
                        "service-type":""
                    }
                ],
                "problem": [
                    {
                        "name-of-problem":"Acute UTI",
                        "on-set-date":"03/12/2020",
                        "life-cycle":"Resolved",
                        "responsible-provider":"test provider"
                    }
                ]
            }
        }
    }
}
</script>