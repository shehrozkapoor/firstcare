import PatientHealthCareRecord from '@/views/PatientHealthCareRecord.vue'
import HomePage from '@/components/patienthealthcarerecord/Pages/HomePage.vue'
import TimeOutForm from '@/components/patienthealthcarerecord/Pages/TimeOutForm.vue'
import VitalSign from '@/components/patienthealthcarerecord/Pages/VitalSign.vue'
import Ventilator from '@/components/patienthealthcarerecord/Pages/Ventilator.vue'
import Neuromuscular from '@/components/patienthealthcarerecord/Pages/Neuromuscular.vue'
import Hemodynamic from '@/components/patienthealthcarerecord/Pages/Hemodynamic.vue'
import XrayResult from '@/components/patienthealthcarerecord/Pages/XrayResult.vue'
import RentalReplacementTherapy from '@/components/patienthealthcarerecord/Pages/RentalReplacementTherapy.vue'
import OrderSheet from '@/components/patienthealthcarerecord/Pages/OrderSheet.vue'
import ProgressNote from '@/components/patienthealthcarerecord/Pages/ProgressNote.vue'
import PhysicianCarePlan from '@/components/patienthealthcarerecord/Pages/PhysicianCarePlan.vue'
import CriticalCarePainObservationTool from '@/components/patienthealthcarerecord/Pages/CriticalCarePainObservationTool.vue'
import IntakeOutput from '@/components/patienthealthcarerecord/Pages/IntakeOutput.vue'
import Graph from '@/components/patienthealthcarerecord/Pages/Graph.vue'
import Prescription from '@/components/patienthealthcarerecord/Pages/Prescription.vue'
import InitialNursingAssessment from '@/components/patienthealthcarerecord/Pages/InitialNursingAssessment.vue'
import Documentation from '@/components/patienthealthcarerecord/Pages/Documentation.vue'
import TestDocument from '@/components/patienthealthcarerecord/SubPages/Documentation/TestDocument.vue'
//Patient List@/components/patienthealthcarerecord/Pages/PatientList.vue
import PatientList from '@/components/patienthealthcarerecord/Pages/PatientList.vue'

import LabResult from '@/components/patienthealthcarerecord/Pages/LabResult.vue'
import SampleInfo from '@/components/patienthealthcarerecord/SubPages/LabResult/SampleInfo.vue'
import cbcPeripheral from '@/components/patienthealthcarerecord/SubPages/LabResult/cbcPeripheral.vue'

// problem and diagnosis
import ProblemAndDiagnosis from '@/components/patienthealthcarerecord/Pages/ProblemAndDiagnosis.vue'

// sub temlates hemodynamics
import Cpp from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/Cpp.vue'
import Vent from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/Vent.vue'
import Auscultation from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/Auscultation.vue'
import Suction from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/Suction.vue'
import GlucoseMonitor from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/GlucoseMonitor.vue'
import BloodGasses from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/BloodGasses.vue'
import CentralPressure from '@/components/patienthealthcarerecord/SubPages/Hemodynamic/CentralPressure.vue'

 // sub templates ventilator
import VolumeFlow from '@/components/patienthealthcarerecord/SubPages/Ventilator/VolumeFlow.vue'

import MAR from '@/components/patienthealthcarerecord/Pages/MAR.vue'
import Summary from '@/components/patienthealthcarerecord/SubPages/MAR/Summary.vue'
import Schedule from '@/components/patienthealthcarerecord/SubPages/MAR/Schedule.vue'

import Order from '@/components/patienthealthcarerecord/Pages/Order.vue'
import OrderSummary from '@/components/patienthealthcarerecord/SubPages/Order/Summary.vue'
import OrderLaboratory from '@/components/patienthealthcarerecord/SubPages/Order/Laboratory.vue'
import OrderRadiology from '@/components/patienthealthcarerecord/SubPages/Order/Radiology.vue'
import OrderMedication from '@/components/patienthealthcarerecord/SubPages/Order/Medication.vue'

const PatientHealthCareRoutes = [
    {
      path: '/patient-health-care',
      name: 'patient-healthcare-main',
      component: PatientHealthCareRecord,
      children:[
        {
          path: 'home-page',
          name: 'patient-healthcare-HomePage',
          component: HomePage
        },
        {
          path: 'timeout-form',
          name: 'timeout-form',
          component: TimeOutForm
        },
        {
          path: 'vital-sign',
          name: 'vital-sign',
          component: VitalSign
        },
        {
          path: 'ventilator/:tab_name?',
          name: 'ventilator',
          component: Ventilator,
          children:[
            {
              path:'volume-flow',
              component:VolumeFlow
            }
          ]
        },
        {
          path: 'neuromuscular',
          name: 'neuromuscular',
          component: Neuromuscular
        },
        {
          path: 'hemodynamic/:tab_name?',
          name: 'hemodynamic',
          component:Hemodynamic,
          children:[
            {
              path:'cpp',
              component:Cpp
            },
            {
              path:'vent',
              component:Vent
            },
            {
              path:'auscultation',
              component:Auscultation
            },
            {
              path:'suction',
              component:Suction
            },
            {
              path:'glucose-monitor',
              component:GlucoseMonitor
            },
            {
              path:'blood-gasses',
              component:BloodGasses
            },
            {
              path:'central-pressure',
              component:CentralPressure
            }
          ],
        },
        {
          path: 'xray-result',
          name: 'xray-result',
          component: XrayResult
        },
        {
          path: 'rental-replacement-therapy',
          name: 'rental-replacement-therapy',
          component: RentalReplacementTherapy
        },
        {
          path: 'order-sheet',
          name: 'order-sheet',
          component: OrderSheet
        },
        {
          path: 'progress-note',
          name: 'progress-note',
          component: ProgressNote
        },
        {
          path: 'physician-care-plan',
          name: 'physician-care-plan',
          component: PhysicianCarePlan
        },
        {
          path: 'critical-care-pain-observation-tool',
          name: 'critical-care-pain-observation-tool',
          component: CriticalCarePainObservationTool
        },
        {
          path: 'intake-output',
          name: 'intake-output',
          component: IntakeOutput
        },
        {
          path: 'graph',
          name: 'graph',
          component: Graph
        },
        {
          path: 'prescription',
          name: 'prescription',
          component: Prescription
        },
        {
          path: 'initial-nursing-assessment',
          name: 'initial-nursing-assessment',
          component: InitialNursingAssessment
        },
        {
          path: 'patient-list/:id?',
          name: 'patient-list',
          component: PatientList,
          props:true,
        },
        {
          path: 'problem-and-diagnosis',
          name: 'problem-and-diagnosis',
          component: ProblemAndDiagnosis,
        },
        {
          path: 'documentation',
          name: 'documentation',
          component: Documentation,
          children:[
            {
              path:'test-document',
              name:"test-document",
              component:TestDocument
            }
          ]
        },
        {
          path: 'lab-result',
          name: 'lab-result',
          component: LabResult,
          children:[
            {
              path:'sample-info',
              name:"sample-info",
              component:SampleInfo
            },
            {
              path:'cbc-peripheral',
              name:"cbc-peripheral",
              component:cbcPeripheral
            }
          ]
        },
        {
          path:"MAR",
          name:"MAR",
          component:MAR,
          children:[
            {
              path:'summary',
              name:"mar-summary",
              component:Summary
            },
            {
              path:'schedule',
              name:"mar-schedule",
              component:Schedule
            },
          ]
        },
        {
          path:"order",
          name:"order",
          component: Order,
          children:[
            {
              path:'order-summary',
              name:'order-summary',
              component: OrderSummary
            },
            {
              path:'order-laboratory',
              name:'order-laboratory',
              component: OrderLaboratory
            },
            {
              path:'order-radiology',
              name:'order-radiology',
              component: OrderRadiology
            },
            {
              path:'order-medication',
              name:'order-medication',
              component: OrderMedication
            }
          ]
        }
      ]
    },
    {
      path: '/',
      redirect:"/patient-health-care/home-page"
    },
    {
      path: '/patient-health-care/',
      redirect:"/patient-health-care/home-page"
    },
    {
      path: '/patient-health-care/patient-list/',
      redirect: '/patient-health-care/patient-list/list-1'
    },
    {
      path:'/patient-health-care/ventilator/',
      redirect:'/patient-health-care/ventilator/volume-flow'
    },
    {
      path:'/patient-health-care/hemodynamic/',
      redirect:'/patient-health-care/hemodynamic/cpp'
    },
    {
      path:'/patient-health-care/documentation/',
      redirect:'/patient-health-care/documentation/test-document'
    }

  ]

export default PatientHealthCareRoutes;