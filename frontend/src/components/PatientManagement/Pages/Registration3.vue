<template>
    <v-container>
    <TabMenu :model="items" class="border-1 border-primary surface-ground"/>
    </v-container>
    <div class="p-5">
    <router-view></router-view>
    </div>
</template>
<script>
import CustomTabs from '@/components/Custom/CustomTabs.vue'
export default {
    name:"PatientRegistration",
    components:{
        CustomTabs
    },
    data(){
        return{
            items:[
                 {label: 'Basic Info', to: {name:'patient-registration-basic-info'}},
                 {label: 'Related Information', to: {name:'patient-registration-related-information'}},
            ]
        }
    }
}
</script>