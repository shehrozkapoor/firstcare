import PatientRegistration from '@/components/PatientManagement/Pages/Registration.vue'
import PatientManagement from '@/views/PatientManagement.vue'


import RegistrationRelatedInformation from '@/components/PatientManagement/Pages/RelatedInformation.vue'
import RegistrationInsuranceInformation from '@/components/PatientManagement/Pages/Insurance.vue'
import RegisterPatientCoverage from '@/components/PatientManagement/Pages/PatientCoverage.vue'
import RegisterEncounterInformation from '@/components/PatientManagement/Pages/Encounter.vue'



import Billing from '@/components/PatientManagement/Pages/Billing.vue'

const PatientManagementRoutes = [
    {
      path: '/patient-management',
      name: 'patient-management',
      component: PatientManagement,
      children:[
          {
              path:'patient-registration',
              name: 'patient-registration',
              component:PatientRegistration,
          },
          {
            path:'related-information',
            name:'related-information',
            component:RegistrationRelatedInformation
        },
        {
            path:'insurance-information',
            name:'insurance-information',
            component:RegistrationInsuranceInformation
        },
        {
            path:'coverage-information',
            name:'coverage-information',
            component:RegisterPatientCoverage
        },
        {
            path:'encounter-information',
            name:'encounter-information',
            component:RegisterEncounterInformation
        },
        {
            path:'billing',
            name:'billing',
            component:Billing,
        }
      ]
    },
    {
        path:'/patient-management/',
        redirect:'/patient-management/patient-registration'
    }

]
export default PatientManagementRoutes;
