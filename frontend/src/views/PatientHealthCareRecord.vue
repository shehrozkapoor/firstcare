<template>
    <v-app>
    <Header/>
    <SideBar :routes="routes" title="Patient Health Care Record" :showTitle="showTitle"/>
    <MainContent />
    </v-app>
</template>

<script>
import Header from '@/components/patienthealthcarerecord/Header.vue'
import SideBar from '@/components/Custom/SideBar.vue'
import MainContent from '@/components/patienthealthcarerecord/MainContent.vue'

export default {
    name:"PatientHealthCareRecord",
        components: {
            Header,
            SideBar,
            MainContent,
        },
        data(){
            return{
                showTitle:true,
                routes:[
                    {
                        'title':'Home',
                        'name':'patient-healthcare-HomePage'
                    },
                    {
                        'title':'Timeout Form',
                        'name':'timeout-form'
                    },
                    {
                        'title':'VitalSign',
                        'name':'vital-sign'
                    },
                    {
                        'title':'Ventilator',
                        'name':'ventilator'
                    },
                    {
                        'title':'Neuromuscular',
                        'name':'neuromuscular'
                    },
                    {
                        'title':'Hemodynamic',
                        'name':'hemodynamic'
                    },
                    {
                        'title':'XrayResult',
                        'name':'xray-result'
                    },
                    {
                        'title':'RentalReplacementTherapy',
                        'name':'rental-replacement-therapy'
                    },
                    {
                        'title':'Order Sheet',
                        'name':'order-sheet'
                    },
                    {
                        'title':'Progress Note',
                        'name':'progress-note'
                    },
                    {
                        'title':'Physician Care Plan',
                        'name':'physician-care-plan'
                    },
                    {
                        'title':'Critical Care Pain Observation Tool',
                        'name':'critical-care-pain-observation-tool'
                    },
                    {
                        'title':'Intake/Output',
                        'name':'intake-output'
                    },
                    {
                        'title':'Graph',
                        'name':'graph'
                    },
                    {
                        'title':'Prescription',
                        'name':'prescription'
                    },
                    {
                        'title':'Initial Nursing Assessment',
                        'name':'initial-nursing-assessment'
                    },
                    {
                        'title':'Patient List',
                        'name':'patient-list'
                    },
                    {
                        'title':'Problem And Diagnosis',
                        'name':'problem-and-diagnosis'
                    },
                    {
                        'title':'Documentation',
                        'name':'documentation'
                    },
                    {
                        'title':'Lab Result',
                        'name':'lab-result'
                    },
                    {
                        'title':'MAR',
                        'name':'MAR'
                    },
                    {
                        'title': 'Order',
                        'name': 'order'
                    }
                ]
            }
        }
    }
    </script>