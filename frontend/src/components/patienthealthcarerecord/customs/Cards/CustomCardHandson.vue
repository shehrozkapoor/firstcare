<template>
    <v-col cols="auto">
        <v-card height="300" width="450" class="overflow-auto">
            <v-card-title class="text-center v-card-title" justify="center">
                {{title}}
            </v-card-title>
            <Handsontable :data="handsonData" :colHeaders="handsonColData" :rowHeaders="handsonRowData" :dropdownMenu="true" :filter="true"/>
        </v-card>
    </v-col>
</template>

<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'
export default{
    name:"CustomCardHandson",
    props:['title'],
    components:{
        Handsontable
    },
    data(){
        return {
            handsonData:[
          ['2016', 10, 11, 12, 13],
          ['2017', 20, 11, 14, 13],
          ['2018', 30, 15, 12, 13],
          ['2018', 30, 15, 12, 13],
          ['2018', 30, 15, 12, 13],
        ],
        handsonColData:['Year', 'Ford', 'Volvo', 'Toyota', 'Honda'],
        handsonRowData:['Row1','Row2', 'Row3', 'Row4', 'Row5'],
        }
    }
}
</script>
