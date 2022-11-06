import {createRouter, createWebHashHistory} from 'vue-router';

const routes = [
	{
		path: '/',
		name: 'dashboard',
		exact: true,
		component: () => import('./components/Dashboard.vue')
	},
	{
		path: '/beneficiary',
		name: 'beneficiary',
		component: () => import('./components/Beneficiary/Beneficiary.vue')
	},
	{
		path: '/eligibility-request',
		name: 'eligibility-request',
		component: () => import('./components/Eligibility/EligibilityRequest.vue')
	},
	{
		path: '/new-eligibility-request',
		name: 'new-eligibility-request',
		component: () => import('./components/Eligibility/AddNewEligibilityRequest.vue')
	},
	{
		path: '/eligibility-transaction',
		name: 'eligibility-transaction',
		component: () => import('./components/Eligibility/EligibilityTransaction.vue')
	},
	{
		path: '/view-eligibility/:id',
		name: 'view-eligibility',
		component: () => import('./components/Eligibility/ViewEligibility.vue')
	},
	{
		path: '/request/pre-autherization',
		name: 'request-pre-autherization',
		component: () => import('./components/PreAutherization/PreAuthRequest.vue')
	},
	{
		path: '/add-pre-autherization',
		name: 'add-pre-autherization',
		component: () => import('./components/PreAutherization/AddNewPreAuth.vue')
	},
	{
		path: '/pre-autherization-request',
		name: 'pre-autherization-request',
		component: () => import('./components/PreAutherization/PreAuthTransection.vue')
	},
	{
		path: '/claim-response',
		name: 'claim-response',
		component: () => import('./components/claims/ClaimResponses.vue')
	},
	
	{
        path: '/login',
        name: 'login',
        component: () => import('./pages/Login.vue')
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
	scrollBehavior () {
        return { left: 0, top: 0 };
    }
});

export default router;