<template>
    <v-col cols="auto">
        <v-card height="300" width="450" class="overflow-auto">
            <v-card-title class="text-center v-card-title" justify="center">
                {{title}}
            </v-card-title>
            <CustomDataTable :table_columns="table_columns" :table_data="table_data" sortable="true" show_header="false"/>
        </v-card>
    </v-col>
</template>

<script>
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'

export default{
    name:"CustomCardTable",
    props:['title'],
    components:{
        CustomDataTable
    },
    data(){
        return{
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
