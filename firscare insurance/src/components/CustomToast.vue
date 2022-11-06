<template>
    <Toast />
</template>

<script>
export default {
    name:"CustomToast",
    props:['message','type','call'],
    mounted(){
        if (this.call==true){
        this.showMessage();
        }
    },
    methods:{
        showMessage(){
            this.$toast.add({severity:this.type, summary: this.type=='success'?'Success Message':'Error Message', detail:this.message, life: 3000});
            this.$emit('update-call',false);
            },
    }
}
</script>