<template>
    <EligibilityTransactionTable :table_columns="table_columns" :table_data="table_data" :sortable="true"
                show_header="false" table_related_type="Eligibility Request" :isLoading="isLoading" :eligiblityServices="EligibilityService"/>
</template>

<script>
import EligibilityService from '@/service/EligibilityRequestService';
import EligibilityTransactionTable from '@/components/EligibilityTransactionTable.vue';

export default {
    name:"EligibilityTransactions",
    components:{
        EligibilityTransactionTable,
    },
    data(){
        return{
            isLoading:true,
            table_columns: [{
                    'field': 'document_id',
                    'inner_header':'patient',
                    'header': 'Beneficiary ID'
                },
                {
                    'field': 'first_name',
                    'inner_header':'patient',
                    'header': 'Beneficiary First Name'
                },
                {
                    'field': 'second_name',
                    'inner_header':'patient',
                    'header': 'Beneficiary Last Name'
                },
                {
                    'field': 'insurance_plan',
                    'inner_header':'patient',
                    'header': 'Beneficiary Insurance Plan'
                },
                {
                    'field': 'insurance_plan',
                    'inner_header':'patient',
                    'header': 'Beneficiary Insurance Plan'
                },
                {
                    'field': 'eligibility_request_id',
                    'inner_header':'eligibility',
                    'header': 'Eligibility Request ID'
                },
            ],
            table_data: []
        }
    },
    EligibilityService:null,
    created(){
        this.EligibilityService = new EligibilityService();
    },
    async mounted(){
        await this.EligibilityService.getAllEligibility().then(data => {
        console.log(data.data)
        this.table_data = data.data;
        this.isLoading=false;
        }).catch((error)=>{
            console.log(error);
            this.showError('Connection Error Please Check your Internet Connection!!')
        });
    },
}
</script>