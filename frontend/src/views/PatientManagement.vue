<template>
    <v-layout>

        <SideBar :routes="routes" title="Patient Management"/>
        <MainContent />
    </v-layout>
</template>

<script>
import SideBar from '@/components/Custom/SideBar.vue'
import MainContent from '@/components/patienthealthcarerecord/MainContent.vue'


export default {
    name:"PatientManagement",
        components: {
            SideBar,
            MainContent
        },
        data(){
            return{
                routes:[
                    {
                        name:'patient-registration',
                        title:'Patient Registration'
                    },
                    {
                        name:'related-information',
                        title:'Patient Related Information'
                    },
                    {
                        name:'insurance-information',
                        title:'Patient Insurance Information'
                    },
                    {
                        name:'coverage-information',
                        title:'Patient Coverage Information'
                    },
                    {
                        name:'encounter-information',
                        title:'Patient Encounter Information'
                    },
                    {
                        name:'billing',
                        title:'Billing'
                    }
                ]
            }
        }
    }
    </script>