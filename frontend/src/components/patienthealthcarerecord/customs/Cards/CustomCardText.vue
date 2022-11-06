<template>
    <v-col cols="auto">
        <v-card height="300" width="450" class="overflow-auto">
            <v-card-title class="text-center v-card-title" justify="center">
                {{title}}
            </v-card-title>
            <v-container width="30%">
            <v-row v-for="(item,index) in rowCount" :key="index">
            <tr>
                <td><h2 class="custom-card-heading m-5">hello1:</h2></td>
                <td><p class="custom-card-text ml-10">hello2</p></td>
            </tr>
            </v-row>
            </v-container>
        </v-card>
    </v-col>
</template>

<script>

export default{
    name:"CustomCardText",
    props:['title'],
    data(){
        return {
        rowCount:10
        }
    },
    components:{
    }
}
</script>
