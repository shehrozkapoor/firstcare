import { createRouter, createWebHistory } from 'vue-router'
import PatientHealthCareRoutes from './PatientHealthCareRecord/index';
import PatientManagementRoutes from './PatientManagement/index'
import Login from './login'

var allRoutes: any[] = []
allRoutes = allRoutes.concat(PatientHealthCareRoutes,PatientManagementRoutes,Login)

const routes = allRoutes

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
