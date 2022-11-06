<template>
    <div class="grid">
        <div class="col-3">
            <SideBar :showTitle="false" :routes="routes" />
        </div>
        <div class="grid col-9 w-full p-4">
            <div class="grid col-12">
                <div class="col-12 w-full">
                    <label for="">Start Date</label>
                    <Calendar v-model="start_date" class="w-full" placeholder="Select the start date"/>
                </div>
                <div class="col-12">
                    <label for="">End Date</label>
                    <Calendar v-model="end_date" placeholder="Select the end date" class="w-full" />
                </div>
            </div>
            <div class="col-12">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>
<script>
import SideBar from '@/components/Custom/SideBar.vue'
import moment from 'moment'

export default {
    name:"LabResult",
    components:{
        SideBar
    },
    data(){
        return{
            start_date:moment().format('MM-DD-YYYY'),
            end_date:null,
            routes:[
                {
                    title:'Sample Information',
                    name:'sample-info'
                },
                {
                    title:'CBC and Peripheral smear',
                    name:'cbc-peripheral'
                },

            ]
        }
    }
}
</script>