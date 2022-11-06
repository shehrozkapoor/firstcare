<template>
    <v-container>
        <p>Patient Details</p>
        <v-divider></v-divider>
        <v-row>
            <v-col cols="4">
                <label for="">Care Plan No</label>
                <CustomInput disabled="true" type="text" placeholder="care plan no" value="2318327" />
            </v-col>
            <v-col cols="4">
                <label for="">Date</label>
                <CustomInput type="date" />
            </v-col>
            <v-col cols="4">
                <label for="">Care Plan Type</label>
                <CustomSelect :items="items" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="4">
                <label for="">Review Date</label>
                <CustomInput type="date" />
            </v-col>
            <v-col cols="4">
                <label for="">Clinic</label>
                <CustomSelect :items="items" />
            </v-col>
            <v-col cols="4">
                <label for="">Written By Dr.</label>
                <CustomSelect :items="items" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="5">
                <label for="">Expected Stay(Days)</label>
                <CustomInput type="number" value="0" />
            </v-col>
            <v-col cols="4">
                <label for="">Status</label>
                <v-radio-group inline>
                    <v-radio :label="item" :value="item" v-for="(item,key) in status" :key="key"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="3">
                <label for="">Revied On</label>
                <CustomSelect :items="items" />
            </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="mt-5">
            <v-col cols="12">
            <h3>Initial/Modified/Surgical/Post Surgical Care Plan</h3>
            </v-col>
            <v-col cols="12">
            <label for="">Dietary Regime</label>
            <CustomSelect :items="items" />
            <CustomInput type="text"/>
            <CustomSelect :items="items" />
            </v-col>
            <v-col cols="12">
            <label for="">Diagnosis</label>
            <CustomInput type="text"/>
            </v-col>
            <v-col cols="12">
            <label for="">Main Line Of Treatment</label>
            <v-textarea background-color="white" color="transparent"></v-textarea>
            </v-col>
            <v-col cols="12">
            <label for="">Element For Improvement</label>
            <v-textarea background-color="white" color="transparent"></v-textarea>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'

export default {
    name:"PhysicianCarePlan",
    components: {
        CustomInput,
        CustomSelect
    },
    data(){
        return{
            items:['1','2','3'],
            status:['hold','active','cancelled','delete']
        }
    }
}
</script>