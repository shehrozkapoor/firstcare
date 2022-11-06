<template>
    <div class="vld-parent">
        <loading :active="isLoading" 
        :is-full-page="true"></loading>
    </div>
</template>

<script>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
    
export default {
    props:['is_loading'],
    data(){
        return {
            isLoading:this.is_loading
        }
    },
    components:{
        Loading
    },
    watch:{
        is_loading(){
            this.isLoading=this.is_loading;
        }
    }
}
</script>