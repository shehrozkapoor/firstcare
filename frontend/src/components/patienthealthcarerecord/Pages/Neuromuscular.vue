<template>
<div>
    <div>
    <Handsontable :data="handsonData1.data" :colHeaders="handsonColData" :rowHeaders="handsonData1.handsonRowData" :dropdownMenu="false" :filter="false" :colWidths=100 :rowHeaderWidth="250"/>
    </div>
    <div class="mt-10 mb-10">
    <Handsontable :data="handsonData2.data" :colHeaders="handsonColData" :rowHeaders="handsonData2.handsonRowData" :dropdownMenu="false" :filter="false" :colWidths=100 :rowHeaderWidth="250"/>
    </div>
    <div class="mt-10 mb-10">
    <Handsontable :data="handsonData3.data" :colHeaders="handsonColData" :rowHeaders="handsonData3.handsonRowData" :dropdownMenu="false" :filter="false" :colWidths=100 :rowHeaderWidth="250"/>
    </div>
</div>
</template>
<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'
export default {
    name:"Neuromuscular",
    components:{
        Handsontable
    },
    data(){
        return{
        handsonColData:['00:00', '01:00', '02:00', '03:00', '04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
        handsonData1:{
            handsonRowData:['Tracts/Intubased','Paralyzed'],
            data:[
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
        ]
        },
        handsonData2:{
            handsonRowData:['Eye Opening','Motor Response','Verbal Response','Scope'],
            data:[
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
        ]
        },
           handsonData3:{
            handsonRowData:['Cough','GAG Reflex','Spont Respiration','Left Pupil Size','Left Pupil Reaction','Right Pupil Size','Right Pupil Reaction'],
            data:[
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','',''],
        ]
        }
    }
}
}
</script>