<template>
    <v-main class="mt-16" >
        <Button label="logout" class="p-button-danger absolute right-0 m-5" icon="pi pi-times" @click="logout"></Button>
        <router-view></router-view>
    </v-main>
</template>

<script>
import {mapMutations} from 'vuex'

export default{
    name:"MainContent",
    methods:{
        ...mapMutations(['logout'])
    },
}
</script>
