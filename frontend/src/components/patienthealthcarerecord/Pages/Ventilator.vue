<template>
<div class="d-flex flex-row mb-5 ml-5 mr-5">
    <CustomTabs v-for="(tab,index) in routing_tabs" :key="index" :link="tab.link" :name="tab.name"/>
</div>
<router-view></router-view>
</template>

<script>
import CustomTabs from '@/components/Custom/CustomTabs.vue'
const ventilator_link ="/patient-health-care/ventilator/";

export default {
    name: "Ventilator",
    components: {
        CustomTabs
    },
    data() {
        return {
            routing_tabs: [{
                name: "Volume/Flow",
                link: '/patient-health-care/ventilator/volume-flow'
            }]
        }
    }
}
</script>
