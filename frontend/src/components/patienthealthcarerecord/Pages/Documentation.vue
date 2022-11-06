<template>
    <div class="grid">
        <div class="col-3">
            <CustomSideBarFolder :nodeSelection="nodeSelection" :selectedNodeKey="selectedNodeKey"/>
        </div>
        <div class="col-9 h-screen p-3 mb-2">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import CustomTitleHeader from '@/components/PatientManagement/Custom/CustomTitleHeader.vue'
import CustomSideBarFolder from '@/components/Custom/CustomSideBarFolder.vue'
export default {
    name:"Documentation",
    components:{
        CustomTitleHeader,
        CustomSideBarFolder
    },
    methods:{
        toggle(event) {
            this.$refs.menu.toggle(event);
        },
        nodeSelection(){
            console.log(this.selectedNodeKey)
        }
    },
    data(){
        return{
            selectedNodeKey:null
        }
    }

}
</script>