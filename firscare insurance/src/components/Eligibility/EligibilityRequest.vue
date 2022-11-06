<template>
	<div class="grid">
		<div class="col-3">
			<Button label="Create New Request" @click="$router.push('new-eligibility-request') " class="p-text-button p-button-success" icon="pi pi-plus"/>
		</div>
		<div class="col-12">
			<div class="card">
				<Toast />
				<h5>Eligibility Request</h5>
				<DataTable :value="billing" :paginator="true" class="p-datatable-gridlines" :rows="10" dataKey="id" :rowHover="true" 
					:loading="loading" :filters="filters" responsiveLayout="scroll"
					:globalFilterFields="['id','patient.account_id','patient.patient_id','unit_amount','paid_amount','total_amount','patient.first_name','patient.second_name','patient.third_name']" >
					<template #header>
                        <div class="flex justify-content-end flex-column sm:flex-row">
                            <span class="p-input-icon-left mb-2">
                                <i class="pi pi-search" />
                                <InputText v-model="filters['global'].value" placeholder="Keyword Search" style="width: 100%"/>
                            </span>
                        </div>
                    </template>
                    <template #empty>
                        No Eligibilty found.
                    </template>
                    <template #loading>
                        Loading Eligibilty Requests...
                    </template>
                    <Column field="id" header="Billing ID" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.id}}
                        </template>
                    </Column>
                    <Column header="FHIR ID" field="account_id" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.patient.account_id}}
                        </template>
                    </Column>
                    <Column header="Patient ID" field="patient" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.patient.patient_id}}
                        </template>
                    </Column>
                    <Column header="Patient Name" field="patient_name" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.patient.first_name}} {{data.patient.second_name}} {{data.patient.third_name}}
                        </template>
                    </Column>
                    <Column header="Appointment" field="appointment" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.appointment}}
                        </template>
                    </Column>
                    <Column header="Unit Amount" field="unit_amount" style="min-width:12rem">
                        <template #body="{data}">
							{{formatCurrency(data.unit_amount)}}
                        </template>
                    </Column>
                    <Column header="Paid Amount" field="paid_amount" filterField="paid_amount" style="min-width:12rem">
                        <template #body="{data}">
							{{formatCurrency(data.paid_amount)}}
                        </template>
                    </Column>
                    <Column header="Total Amount(Inc tax.)" field="total_amount" style="min-width:12rem">
                        <template #body="{data}">
						{{formatCurrency(data.total_amount)}}
                        </template>
                    </Column>
                    <Column header="Service Note" field="service_note" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.service_note}}
                        </template>
                    </Column>
                    <Column header="Billing Note" field="billing_note" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.billing_note}}
                        </template>
                    </Column>
                    <Column header="Billing Type" field="status" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.status}}
                        </template>
                    </Column>
                    <Column header="Eligibility Request Status" field="eligibility_bundle" style="min-width:12rem">
                        <template #body="{index}">
                            {{eligibility_request[index]==false?"Not Submitted":"Submitted"}}
                        </template>
                    </Column>
                    <Column header="Eligibility Response Status" field="eligibility_bundle" style="min-width:12rem">
                        <template #body="{index}">
                            {{eligibility_response[index]==false?"Not Received":"Received"}}
                        </template>
                    </Column>
                    <Column header="Created On" field="creation_date" style="min-width:12rem">
                        <template #body="{data}">
                            {{data.creation_date}}
                        </template>
                    </Column>
                    <Column style="min-width:12rem">
                        <template #body="{data,index}">
							<div class="flex flex-row justify-content-evenly">
							<Button class="p-button-raised p-button-rounded p-button-success" :id="data.id" icon="pi pi-send" v-tooltip="'Send Eligibility Request'"  :disabled="eligibility_request[index]==true" v-on:click="sendEligibilityRequest(data.id,index)"/>
							<Button class="p-button-raised p-button-rounded p-button-warning" :id="data.id" icon="pi pi-refresh"  v-tooltip="'Resend Eligibility Request'" :disabled="eligibility_response[index]==true" v-on:click="sendEligibilityRequest(data.id,index)"/>
							</div>
                        </template>
                    </Column>
				</DataTable>
			</div>
		</div>		
	</div>
</template>

<script>
	import {FilterMatchMode} from 'primevue/api';
	import EligibilityRequestService from '../../service/EligibilityRequestService';
	export default {
		data() {
			return {
				billing: null,
				filters: null,
				loading: true,
				eligibility_request:[],
				eligibility_response:[],
			}
		},
		billingService: null,
		created() {
			this.billingService = new EligibilityRequestService();
			this.initFilters();
		},
		async mounted() {
			this.getDataLoaded();
		},
		methods: {
			showSuccess(message) {this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 3000});},
			showError(message) {this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 3000});},
			async getDataLoaded(){
				await this.billingService.getInsuranceBilling().then(data => {
				this.billing = data.data; 
				this.loading = false;
				data.forEach((item,index) => {
					if(item.eligibility_bundle == null){
						this.eligibility_request[index] = false;
						this.eligibility_response[index]= false;
					}
					if(item.eligibility_bundle != null){
						this.eligibility_request[index] = true;
						try {
							var response_status = item.eligibility_bundle.response_bundle_status;
							this.eligibility_response[index] = response_status;
						} catch (error) {
							this.eligibility_response[index] = false;
						}
					}
				})
				});
			},
			initFilters() {
				this.filters = {
					'global': {value: null, matchMode: FilterMatchMode.STARTS_WITH},
				}
			},
			formatCurrency(value) {
				return value.toLocaleString('en-US', {style: 'currency', currency: 'SAR'});
			},
			async sendEligibilityRequest(id,index){
				var response = await this.billingService.sendEligibilityRequest(id);
				if (response.status == 'error'){
					this.showError(response.message)
				}
				if (response.status == 'ok'){
					this.eligibility_request[index] = true;
					this.showSuccess(response.data)
				}

			}
		}
	}
</script>

<style scoped lang="scss">
@import '../../assets/demo/styles/badges.scss';

::v-deep(.p-datatable-frozen-tbody) {
	font-weight: bold;
}

::v-deep(.p-datatable-scrollable .p-frozen-column) {
	font-weight: bold;
}

::v-deep(.p-progressbar) {
	height: .5rem;
	background-color: #D8DADC;

	.p-progressbar-value {
		background-color: #607D8B;
	}
}
.custom-error .p-tooltip-text {
    background-color: var(--pink-800);
    color: rgb(255, 255, 255);
}
.custom-error.p-tooltip-right .p-tooltip-arrow {
    border-right-color: var(--pink-800);
}
</style>
