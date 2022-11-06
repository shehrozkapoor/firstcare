<template>
    <div>
        <DataTable :value="table_data" responsiveLayout="scroll" stripedRows :paginator="paginator??false" :rows="10"
            v-model:filters="filters" filterDisplay="menu" :loading="loading" v-model:selection="selectedRows"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[10,25,50]"
            currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries"
            :globalFilterFields="globalFilterField">
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

                <template #body="{data}" >
                <div v-if="col['inner_header'] === 'patient'">
                    {{data['patient'][col.field]}}
                </div>
                <div v-else>
                    {{data[col.field]}}
                </div>
                </template>

                <template #filter="{filterModel}" v-if="filter??false">
                    <InputText type="text" v-model="filterModel.value" class="p-column-filter"
                        placeholder="Search by Id" />
                </template>
            </Column>

            <Column field="response_eligibility_status" header="Eligibility Response Status" :sortable="sortable??false"
                style="min-width: 14rem">
                <template #body="{data,field}">
                    <div v-if="data[field]=='eligible'">
                        Approved
                    </div>
                    <div v-else-if="data[field]=='requested'">
                        Requested
                    </div>
                    <div v-else>
                        Rejected
                    </div>
                </template>
            </Column>

            <Column header="Option" style="min-width: 17rem">
                <template #body="{data}">
                <div class="flex flex-row justify-content-evenly">
                    <Button type="button" @click="$router.push({name: 'view-eligibility', params: { id: data.id }})" icon="pi pi-search" class="p-button-primart" style="margin-right: .5em"
                        label="View Details">View Details</Button>
                    <Button type="button" icon="pi pi-replay" class="p-button-primart" style="margin-right: .5em" @click="resendEligibility(data.id)"></Button>
                </div>
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
export default {
    name: "EligibilityTransactionTable",
    props: ['table_columns', 'table_data','title','multipleSelect','paginator','filter','sortable','show_header','table_related_type','isLoading','eligiblityServices'],
    data() {
        return {
            filters: {
                'global': {
                    value: null,
                    matchMode: FilterMatchMode.STARTS_WITH
                },
            },
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
        async resendEligibility(id){
            await this.eligiblityServices.resendEligibility(id).then(response =>{
                this.data.push(response.data)
                this.showSuccess('Successfully Resended!!')
            })
            .catch(error=>{
                console.log(error)
            })
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