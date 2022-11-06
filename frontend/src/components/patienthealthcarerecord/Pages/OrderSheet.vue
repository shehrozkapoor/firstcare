<template>
<div>
    <Handsontable :data="handsonData1.data" :colHeaders="handsonColData" :rowHeaders="handsonData1.handsonRowData" :dropdownMenu="false" :filter="true" :colWidths=200 :rowHeaderWidth="auto"/>
</div>
<div class="mt-16" v-if="showHeader">
    <CustomHeader title="Notes"/>
    <CustomDataTable :table_columns="table_columns" :table_data="table_data" />

</div>
</template>
<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'
import CustomHeader from '@/components/Custom/CustomHeader.vue'
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
export default {
    name: "OrderSheet",
    components: {
        Handsontable,
        CustomHeader,
        CustomDataTable
    },
    data() {
        return {
            showHeader: true,
            handsonColData: ['Procedure ID', 'Procedure', 'Ordered By', 'Created By', 'Created Datetime'],
            handsonData1: {
                handsonRowData: true,
                data: [
                    ['', '', '', '', ''],
                    ['', '', '', '', ''],
                ]
            },
            table_columns: [{
                    'field': 'id',
                    'header': 'ID'
                },
                {
                    'field': 'description',
                    'header': 'Description'
                },
            ],
            table_data: [{
                id: "1",
                description: "testing",
            }]
        }
    }
}
</script>