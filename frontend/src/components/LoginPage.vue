<template>
    <div class="login-form ">
    <h1>LOGIN</h1>
    <Message severity="error" v-if="login_message=='Invalid username or password!!'">{{login_message}}</Message>
    <Message severity="success" v-if="login_message=='Login Successful!!'">{{login_message}}</Message>
    <form class="flex flex-column" @submit.prevent="Login(payload)">
        <InputText class="mt-2" placeholder="Enter your username" type="text" v-model="payload.username" required/>
        <InputText class="mt-2" placeholder="Enter your password" type="password" v-model="payload.password" required/>
        <div class="w-full justify-content-center">
            <Button class="p-button-primary w-25 mt-2" type="submit" label="Login"></button>
        </div>
    </form>
</div>
</template>

<script>
import {mapState,mapMutations,mapActions} from 'vuex'


export default {
    name:"LoginPage",
    data(){
        return{
        payload:{
            username:"",
            password:"",
        },
           message:"Invalid username or password!",
        }
    },
    computed:{
        ...mapState(['login','login_message'])
    },
    methods:{
        ...mapActions(['Login']),
    }
}
</script>

<style scoped>
.login-form{
    border: 1px solid transparent;
    width: 40%;
    min-height: 300px;
    height: auto;
    padding: 30px;
    text-align: center;
    margin: 0 auto;
    margin-top: 15%;
    background-color: rgba(111, 158, 245, 0.507);
    border-radius: 12px;
    box-shadow: 1px 1px 10px gray;
}
</style>