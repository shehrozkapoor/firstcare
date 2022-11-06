<template>
    <Toast />

    <Dialog header="Add Insurance Details For Existing Beneficiary" :visible="display" :breakpoints="{'960px': '75vw', '640px': '90vw'}"
        :style="{width: '70vw'}" :maximizable="true" :modal="true" :closable="false" :draggable="false" position="top">
        <Message severity="warn">If you need to add Insurance Details for new Beneficiary please add a new beneficiary and then add insurance details.!!</Message>
        <Divider />
        <div class="grid p-5">
            <div class="col-12">
                <div class="p-inputgroup">
                    <InputText placeholder="Search Beneficiary By Saudi IQMA / NIN value" v-model="search_input" />
                    <Button icon="pi pi-search" class="p-button-warning" @click="searchBeneficiary" />
                </div>
            </div>
            <ProgressSpinner v-show="loading==true"/>
            <div class="col-12 justify-content-center align-content-center">
                <Textarea v-model="insurance_details" rows="10" class="w-full" v-if="showDetails==true"
                    :readonly="true" />
                </div>
            <div class="col-12">
                <CustomDataTable :table_columns="table_columns" :table_data="table_data" :sortable="true"
                :show_header="false" table_related_type="beneficiary" :isLoading="isLoading" :rowEditor="false" :searchBeneficiary="true" @update-search-document-id="getDocumentId($event)" v-if="showDetails==true"/>
            </div>
        </div>
        <template #footer>
            <Button label="cancel" icon="pi pi-times" class="p-button-text p-button-danger"
                @click="updateDisplaySearchBeneficiary" />
        </template>
    </Dialog>
</template>

<script>
import CustomDataTable from '@/components/Datatable.vue';
import BeneficiaryServices from '@/service/BeneficiaryServices'
export default {
    name:"CustomSearchBeneficiary",
    props:['displaySearchBeneficiary','table_columns','table_data','isLoading'],
    components:{
        CustomDataTable
    },
    data(){
        return{
            display:this.displaySearchBeneficiary,
            search_input:null,
            insurance_details:null,
            showDetails:false,
            loading:false,
        }
    },
    methods:{
        showSuccess(message) {this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 3000});},
        showError(message) {this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 3000});},
        updateDisplaySearchBeneficiary(){
            this.$emit('update-displaySearchBeneficiary',false)
        },
        async searchBeneficiary(){
            this.loading = true;
            if(this.search_input === null){
                this.showError('search input cannot be empty!!')
            }
            else{
                var beneficiary = new BeneficiaryServices();
                await beneficiary.getInsuranceSeatchBeneficiary(this.search_input).then(response =>{
                    this.loading = false;
                    if(response['ApiStatus'] === 'Success'){
                        this.insurance_details=  JSON.stringify(response, undefined, 4);
                        this.showDetails = true;
                    }
                }).catch(error=>{
                    this.loading = false;
                    console.log(error);
                    if(error.response.data['ApiStatus'] === 'Fail'){
                        this.showError(error.response.data['ErrorDescription'])
                    }
                })
            }
        },
        async getDocumentId(documentId){
            this.loading = false;
            var beneficiary = new BeneficiaryServices();
            await beneficiary.saveInsuranceSeatchBeneficiaryDetails(this.insurance_details,documentId).then(response =>{
                this.loading = false;
                if(response['status'] === 'ok'){
                    this.insurance_details= null;
                    this.showDetails = false;
                    this.search_input=null;
                    this.showSuccess(response['message']);
                }
            }).catch(error=>{
                this.loading = false;
                console.log(error);
                if(error.response.data['status'] === 'error'){
                    this.showError(error.response.data['message'])
                }
            })
        }
    },
    watch:{
        displaySearchBeneficiary(){
            this.display = this.displaySearchBeneficiary;
        }

    }
}
</script>