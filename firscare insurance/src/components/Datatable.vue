<template>
    <Toast />
    <Dialog :header="'Insurance Details of '+insuranceDetailsId" v-model:visible="displayInsuranceDetails"
        :breakpoints="{'960px': '75vw', '640px': '90vw'}" :style="{width: '70vw'}" :modal="true">
        <div v-if="insuranceDetails.length !== 0">
            <div v-for="(insurance,key) of insuranceDetails" :key="key" class="grid">
                <div class="col-12 mt-2">
                     <h3>Insurance Details {{key+1}} </h3>
                </div>
                <div class="col-4">
                     <label for="policy-number" class="text-lg font-bold ml-0 pl-0 mt-2 mb-2 col-12">Policy Number</label>
                     <InputText type="text" v-model="insurance.policy_number" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="classname" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Class Name</label>
                     <InputText type="text" v-model="insurance.classname" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="gender" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Gender</label>
                     <InputText type="text" v-model="insurance.gender" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="DeductibleRate" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Deductible Rate</label>
                     <InputText type="text" v-model="insurance.DeductibleRate" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="MaxLimit" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Max Limit</label>
                     <InputText type="text" v-model="insurance.MaxLimit" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="BeneficiaryType" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Beneficiary Type</label>
                     <InputText type="text" v-model="insurance.BeneficiaryType" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="BeneficiaryTypeId" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Beneficiary Type ID</label>
                     <InputText type="text" v-model="insurance.BeneficiaryTypeId" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="BeneficiaryNumber" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Beneficiary Number</label>
                     <InputText type="text" v-model="insurance.BeneficiaryNumber" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="IdentityNumber" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Identity Number</label>
                     <InputText type="text" v-model="insurance.IdentityNumber" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="BeneficiaryName" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Beneficiary Name</label>
                     <InputText type="text" v-model="insurance.BeneficiaryName" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="InceptionDate" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Inception Date</label>
                     <InputText type="text" v-model="insurance.InceptionDate" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="PolicyHolder" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Policy Holder</label>
                     <InputText type="text" v-model="insurance.PolicyHolder" :readonly="true" class="col-12"/>
                </div>
                <div class="col-4">
                     <label for="InsurancePolicyExpiryDate" class="text-lg font-bold text-left ml-0 pl-0 mt-2 mb-2 col-12">Insurance Policy Expiry Date</label>
                     <InputText type="text" v-model="insurance.InsurancePolicyExpiryDate" :readonly="true" class="col-12"/>
                </div>
            </div>
        </div>
        <div v-if="insuranceDetails.length === 0">
            <Message severity="error">Insurance Details Not Found!!!</Message>
        </div>
    </Dialog>
    <div>
        <DataTable :value="table_data" responsiveLayout="scroll" stripedRows :paginator="paginator??false" :rows="10"
            v-model:filters="filters" filterDisplay="menu" :loading="loading" v-model:selection="selectedRows"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[10,25,50]"
            currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries"
            :globalFilterFields="globalFilterField" :rowEditor="rowEditor" editMode="row"
            v-model:editingRows="editingRows" @row-edit-save="onRowEditSave">
            <template #header>
                <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                    <h5 class="m-0">{{title}}</h5>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Keyword Search"
                            :v-show="show_header" />
                    </span>
                </div>
            </template>
            <template #empty>
                No {{table_related_type}} found.
            </template>
            <template #loading>
                Loading {{table_related_type}} data. Please wait.
            </template>
            <Column selectionMode="multiple" style="min-width: 3rem" v-if="multipleSelect"></Column>
            <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"
                :sortable="sortable??false" style="min-width: 14rem">

                <template #body="{data}">
                    {{data[col.field]}}
                </template>

                <template #filter="{filterModel}" v-if="filter??false">
                    <InputText type="text" v-model="filterModel.value" class="p-column-filter"
                        placeholder="Search by Id" />
                </template>
                <template #editor="slotProps">
                    <InputText v-model="slotProps.data[slotProps.field]" autofocus />
                </template>
            </Column>

            <Column field="contact_info.phone_number" header="Contact Number" :sortable="sortable??false"
                style="min-width: 14rem">
                <template #editor="{data}">
                    <InputText v-model="data['contact_info']['phone_number']" />
                </template>
            </Column>
            <Column header="Insurance">
                <template #body="{data}">
                    <Button type="button" icon="pi pi-eye" class="p-button-primart" style="margin-right: .5em"
                        label="View Details" @click="viewDetails(data.document_id)"></Button>
                </template>
            </Column>
            <Column :rowEditor="rowEditor" headerStyle="width:7rem" bodyStyle="text-align:center"></Column>
            <Column header="Option" v-if="searchBeneficiary===true">
                <template #body="{data}">
                    <Button type="button" icon="pi pi-search" class="p-button-primart" style="margin-right: .5em"
                        label="Select" @click="sendSearchDocumentId(data.document_id)"></Button>
                </template>
            </Column>

        </DataTable>
    </div>
</template>


<script>
import {
    FilterMatchMode,
    FilterOperator
} from 'primevue/api';

import BeneficiaryServices from '@/service/BeneficiaryServices';

export default {
    name: "CustomDataTable",
    props: ['table_columns', 'table_data','title','multipleSelect','paginator','filter','sortable','show_header','table_related_type','isLoading','rowEditor','searchBeneficiary'],
    data() {
        return {
            filters: {
                'global': {
                    value: null,
                    matchMode: FilterMatchMode.STARTS_WITH
                },
            },
            displayInsuranceDetails:false,
            insuranceDetailsId:null,
            insuranceDetails:[],
            editingRows:[],
            multiSelect:this.multipleSelect??false,
            selectedRows: null,
            globalFilterField:[],
            loading: this.isLoading,
            columns: this.table_columns,
            data: this.table_data
        }
    },
    created() {
        this.table_columns.forEach(item =>
            this.filters[item.field] = {
            operator: FilterOperator.AND,
            constraints: [{
                value: null,
                matchMode: FilterMatchMode.STARTS_WITH
            }]
        });
        this.table_columns.forEach(item => this.globalFilterField.push(item.field))
    },
    methods:{
        showSuccess(message) {this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 3000});},
        showError(message) {this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 3000});},
        async onRowEditSave(event) {
            let { newData, index } = event;
            const beneficiaryServices = new BeneficiaryServices();
                await beneficiaryServices.updateBeneficiary(newData)
                .then((data)=>{
                    console.log(data);
                }).catch((error)=>{
                    console.log(error);
                    this.showError(error.response.data.message);
                });
            
            this.data[index] = newData;
        },
        sendSearchDocumentId(id){
            this.$emit('update-search-document-id',id)
        },
        async viewDetails(id){
            const beneficiaryServices = new BeneficiaryServices();
            await beneficiaryServices.getInsuranceDetails(id)
            .then((data)=>{
                console.log(data);
                this.insuranceDetails=data.data;
                this.insuranceDetailsId=id;
                this.displayInsuranceDetails=true;
            }).catch((error)=>{
                console.log(error);
                this.showError(error.response.data.message);
            });
        }
    },
    watch:{
        isLoading() {
        this.loading = this.isLoading;
        },
        table_data(){
            this.data = this.table_data
        }
    }
}
</script>


<style lang="scss" scoped>
::v-deep(.p-paginator) {
    .p-paginator-current {
        margin-left: auto;
    }
}

::v-deep(.p-progressbar) {
    height: .5rem;
    background-color: #D8DADC;

    .p-progressbar-value {
        background-color: #607D8B;
    }
}

::v-deep(.p-datepicker) {
    min-width: 25rem;

    td {
        font-weight: 400;
    }
}

::v-deep(.p-datatable.p-datatable-customers) {
    .p-datatable-header {
        padding: 1rem;
        text-align: left;
        font-size: 1.5rem;
    }

    .p-paginator {
        padding: 1rem;
    }

    .p-datatable-thead > tr > th {
        text-align: left;
    }

    .p-datatable-tbody > tr > td {
        cursor: auto;
    }

    .p-dropdown-label:not(.p-placeholder) {
        text-transform: uppercase;
    }
}
</style>