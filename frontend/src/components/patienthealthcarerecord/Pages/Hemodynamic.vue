<template>
<div class="d-flex flex-row mb-5 ml-5 mr-5">
    <CustomTabs v-for="(tab,index) in routing_tabs" :key="index" :link="tab.link" :name="tab.name"/>
</div>
<router-view></router-view>
</template>
<script>

import CustomTabs from '@/components/Custom/CustomTabs.vue'

const hemodynamic_link ="/patient-health-care/hemodynamic/";

export default {
    name:"Hemodynamic",
    components:{
        CustomTabs
    },
    data (){
        return{
            routing_tabs:[
        {
            name:"CPP",
            link:hemodynamic_link+'cpp'
        },
        {
            name:"Vent/O2 Therapy",
            link:hemodynamic_link+'vent'
        },
        {
            name:"Auscultation",
            link:hemodynamic_link+'auscultation'
        },
        {
            name:"Suction",
            link:hemodynamic_link+'suction'
        },
        {
            name:"GlucoseMonitor",
            link:hemodynamic_link+'glucose-monitor'
        },
        {
            name:"Blood Gasses",
            link:hemodynamic_link+'blood-gasses'
        },
        {
            name:"Central Pressure",
            link:hemodynamic_link+'central-pressure'
        },
    ]
        }
    }
}
</script>