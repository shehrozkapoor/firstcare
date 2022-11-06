<template>
    <div>
    <Handsontable :data="handsonData1.data" :colHeaders="handsonColData" :rowHeaders="handsonData1.handsonRowData" :dropdownMenu="false" :filter="false" :colWidths=100 :rowHeaderWidth="250"/>
    </div>
</template>

<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'

export default {
    name:"Suction",
    components:{
        Handsontable,
    },
    data(){
        return{
        handsonColData:['00:00', '01:00', '02:00', '03:00', '04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
        handsonData1:{
            handsonRowData:['Suction','Spectrum','Type','Amount'],
            data:[
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
        ]
        },
    }
}
}
</script>