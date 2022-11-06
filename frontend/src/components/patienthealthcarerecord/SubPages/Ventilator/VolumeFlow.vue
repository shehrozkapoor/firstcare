<template>
<div>
    <Handsontable :data="handsonData" :colHeaders="handsonColData" :rowHeaders="handsonRowData" :dropdownMenu="false" :filter="false" :colWidths=100 :rowHeaderWidth="250"/>
</div>
</template>
<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'

export default {
    name:"VolumeFlow",
    components:{
        Handsontable
    },
    data(){
        return{

        handsonData:[
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
        ],
        handsonColData:[
            '00:00', '01:00', '02:00', '03:00', '04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
        handsonRowData:[
            'MODE','FrO2','RR SetTotal(Ht)','VT(Sec)','VT(Extra)','MV(Measure)','Flow Rate L/Sec'],
        }
    }
}
</script>