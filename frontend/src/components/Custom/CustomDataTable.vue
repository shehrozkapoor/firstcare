<template>
    <div>
        <DataTable :value="table_data" responsiveLayout="scroll" stripedRows :paginator="paginator??false" :rows="10"
            v-model:filters="filters" filterDisplay="menu" :loading="loading" v-model:selection="selectedRows"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[10,25,50]"
            currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries"
            :globalFilterFields="globalFilterField" :rowEditor="true">
            <template #header>
                <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                    <h5 class="m-0">{{title}}</h5>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Keyword Search" :v-show="show_header"/>
                    </span>
                </div>
            </template>
            <template #empty>
                No customers found.
            </template>
            <template #loading>
                Loading customers data. Please wait.
            </template>
            <Column selectionMode="multiple" style="min-width: 3rem" v-if="multipleSelect"></Column>
            <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" :sortable="sortable??false"
                style="min-width: 14rem">
                <template #body="{data}">
                    {{data[col.field]}}
                </template>
                <template #filter="{filterModel}" v-if="filter??false">
                    <InputText type="text" v-model="filterModel.value" class="p-column-filter"
                        placeholder="Search by Id" />
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
    name: "CustomDataTable",
    props: ['table_columns', 'table_data','title','multipleSelect','paginator','filter','sortable','show_header'],
    data() {
        return {
            filters: {
                'global': {
                    value: null,
                    matchMode: FilterMatchMode.STARTS_WITH
                },
            },
            multiSelect:this.multipleSelect??false,
            selectedRows: null,
            globalFilterField:[],
            loading: false,
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