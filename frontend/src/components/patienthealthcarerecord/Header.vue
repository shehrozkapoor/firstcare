<template>
    <v-app-bar height="100" class="header">
        <v-container>
            <v-row justify="space-between">
                <p>4927 NASER MOHAMMED KH ALANAZI</p>
                <CustomButton />
            </v-row>
            <v-row class="mt-5">
                <p class="mr-5">23 YR 7 MARCH 11</p>
                <p class="ml-10 mr-10">23 YR 7 MARCH 11</p>
                <p class="ml-10 mr-10">Mobile_no:31575776726</p>
                <p class="ml-10 mr-10">Alergic: ROOD,MON</p>
                <p class="ml-10 mr-10">Admitted</p>
            </v-row>
        </v-container>
    </v-app-bar>
</template>

<script>
import CustomButton from './customs/buttons/CustomButton.vue'

export default {
    name:"Header",
    components:{
        CustomButton
    }
}
</script>