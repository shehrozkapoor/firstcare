<template>
    <Toast />
    <div class="grid">
        <div class="header col-12">
            <Panel header="Search">
                <SearchForm :p_document_id="searchProps.document_id" :p_first_name="searchProps.first_name"
                    :p_second_name="searchProps.second_name" :p_file_id="searchProps.file_id"
                    :p_number="searchProps.number" :p_start_date="searchProps.start_date"
                    :p_end_date="searchProps.end_date" :p_selectedInsuracePlan="searchProps.selectedInsuracePlan"
                    :p_selectedGender="searchProps.selectedGender" @updateProps="updateSearchProps($event)" />
                <Divider />
                <div class="flex flex-row justify-content-between">
                    <div>
                        <Button label="Search " class="mr-2 mt-3 mb-3 p-button-success" @click="searchTable" />
                        <Button label="reset " class="ml-2 mt-3 mb-3 p-button-danger" @click="clearProps" />
                    </div>
                    <div>
                        <Button label="Search Insurance" class="mr-2 mt-3 mb-3 p-button-success" @click="display_search_beneficiary=!display_search_beneficiary" />
                        <CustomSearchBeneficiary :displaySearchBeneficiary="display_search_beneficiary" @update-displaySearchBeneficiary="updateSearchBeneficiary($event)" :table_columns="table_columns" :table_data="table_data" :isLoading="isLoading"/> 
                    </div>
                </div>
            </Panel>
        </div>
        <div class="flex flex-row col-12">
            <Button label="New Beneficiary " icon="pi pi-plus" class="mr-2 mt-3 mb-3 p-button-success"
                @click="display_new_beneficiary=!display_new_beneficiary" />
            <CustomAddBeneficiaryDialog :displayMaximizable="display_new_beneficiary"
                @update-display-maximizable="updateDisplayMaximizable($event)"
                @addNewRowBenefciaryTable="addNewRowBenefciaryTable($event)" />
            <FileUpload mode="basic" name="demo[]" url="http://localhost:8000/upload"
                class="mr-2 mt-3 mb-3 p-button-success" />
            <Button label="Download Sample " class="mr-2 mt-3 mb-3 p-button-text" />
        </div>
        <div class="col-12">
            <CustomDataTable :table_columns="table_columns" :table_data="table_data" :sortable="true"
                show_header="false" table_related_type="beneficiary" :isLoading="isLoading" :rowEditor="true"/>
        </div>
    </div>
</template>


<script>
import SearchForm from '@/components/Beneficiary/Components/SearchForm';
import CustomAddBeneficiaryDialog from '@/components/Beneficiary/Components/CustomAddBeneficiaryDialog';
import CustomDataTable from '@/components/Datatable.vue';
import BeneficiaryServices from '../../service/BeneficiaryServices';
import CustomSearchBeneficiary from '@/components/Beneficiary/Components/CustomSearchInsurance'
export default {
    name:'Beneficiary',
    components:{
        SearchForm,
        CustomDataTable,
        CustomAddBeneficiaryDialog,
        CustomSearchBeneficiary
    },
    data(){
        return{
            isLoading:true,
            display_new_beneficiary:false,
            display_search_beneficiary:false,
            searchProps:{
                document_id: null,
                first_name: null,
                second_name: null,
                file_id: null,
                number: null,
                start_date: null,
                end_date: null,
                selectedInsuracePlan: null,
                selectedGender: null,
            },
            table_columns: [{
                    'field': 'document_id',
                    'header': 'Document ID'
                },
                {
                    'field': 'first_name',
                    'header': 'Name'
                },
                {
                    'field': 'DOB',
                    'header': 'Date of Birth'
                },
                {
                    'field': 'insurance_plan',
                    'header': 'Insurance Plan'
                },
                {
                    'field': 'e_health_id',
                    'header': 'E-Health ID'
                },
            ],
            table_data: []
        }
    },
    beneficiaryServices:null,
    created(){
        this.beneficiaryServices = new BeneficiaryServices();
    },
    async mounted(){
        await this.beneficiaryServices.getAllBeneficiary().then((data) => {
        this.table_data = data.data;
        this.isLoading=false;
        }).catch((error)=>{
            console.log(error);
            this.showError('Connection Error Please Check your Internet Connection!!')
        });
    },
    methods:{
    showSuccess(message) {this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 3000});},
    showError(message) {this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 3000});},
    clearProps(){
        this.searchProps.document_id=null;
        this.searchProps.first_name=null;
        this.searchProps.second_name=null;
        this.searchProps.file_id=null;
        this.searchProps.number=null;
        this.searchProps.start_date=null;
        this.searchProps.end_date=null;
        this.searchProps.selectedInsuracePlan=null;
        this.searchProps.selectedGender=null;
    },
    updateSearchBeneficiary(newVal){
        this.display_search_beneficiary = newVal;
    },
    updateSearchProps(newVal){
        if(newVal.field == 'document_id'){
            this.document_id = newVal.val;
        }
        if(newVal.field == 'first_name'){
            this.first_name = newVal.val;
        }
        if(newVal.field == 'second_name'){
            this.second_name = newVal.val;
        }
        if(newVal.field == 'file_id'){
            this.file_id = newVal.val;
        }
        if(newVal.field == 'number'){
            this.number = newVal.val;
        }
        if(newVal.field == 'start_date'){
            this.start_date = newVal.val;
        }
        if(newVal.field == 'end_date'){
            this.end_date = newVal.val;
        }
        if(newVal.field == 'insurance_plan'){
            this.selectedInsuracePlan = newVal.val;
        }
        if(newVal.field == 'gender'){
            this.selectedGender = newVal.val;
        }
    },
    addNewRowBenefciaryTable(newVal){
        this.table_data.push(newVal);
    },
    updateDisplayMaximizable(newValue){
        this.display_new_beneficiary = newValue;
    },
    async searchTable(){
        this.isLoading=true;
        await this.beneficiaryServices.getSearchBeneficiary(this.document_id,this.first_name,this.second_name,this.file_id,this.number,this.start_date,this.end_date,this.selectedInsuracePlan,this.selectedGender).then((data) => {
        this.table_data = data.data;
        this.isLoading=false;
        }).catch((error)=>console.log(error));
    }
    },
}
</script>