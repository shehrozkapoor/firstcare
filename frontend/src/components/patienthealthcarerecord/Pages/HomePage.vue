<template>
        <v-layout>
            <v-row justify="center">
                <CustomCardTable title="CURRENT ADMISSION"/>
                <CustomCardHandson title="MultiDispensary Care Plan"/>
                <CustomCardHandson title="Clinical Alerts"/>
                <CustomCardText title="Triage/Vital/Measurements"/>
                <CustomCardHandson title="Lab"/>
                <CustomCardTable title="Outstanding Orders"/>
                <CustomCardHandson title="Outstanding Orders"/>
                <CustomCardHandson title="Chief Complain"/>
                <CustomCardHandson title="Progress Note"/>
                <CustomCardHandson title="Current Medication"/>
                <CustomCardHandson title="Problems/Diagnostics"/>
                <CustomCardHandson title="Allergies"/>
            </v-row>
        </v-layout>
</template>

<script>
import CustomCardHandson from '@/components/patienthealthcarerecord/customs/Cards/CustomCardHandson.vue'
import CustomCardTable from '@/components/patienthealthcarerecord/customs/Cards/CustomCardTable.vue'
import CustomCardText from '@/components/patienthealthcarerecord/customs/Cards/CustomCardText.vue'

export default{
    name:"HomePage",
    components:{
        CustomCardHandson,
        CustomCardTable,
        CustomCardText
    }
}
</script>