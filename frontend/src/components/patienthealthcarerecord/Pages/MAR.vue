<template>
    <div class="grid col-12">
        <div class="col-3">
            <SideBar :showTitle="false" :routes="routes" />
        </div>
        <div class="col-9 w-full">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/Custom/SideBar.vue'
export default {
    name:"MAR",
    components:{
        SideBar
    },
    data(){
        return{
            routes:[
                {
                    title:'Summary',
                    name:'mar-summary'
                },
                {
                    title:'Schedule',
                    name:'mar-schedule'
                }
            ]
        }
    }
}
</script>