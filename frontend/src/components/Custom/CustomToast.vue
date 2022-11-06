<template>
    <Toast />
</template>

<script>
import {mapState} from 'vuex'
export default{
    name:"CustomToast",
    mounted(){
        this.$toast.add({severity:this.toast_severity, summary: this.toast_title, detail:this.toast_message});
    },
    computed:{
        ...mapState(['toast_message','toast_title','toast_severity'])
    }
}
</script>

