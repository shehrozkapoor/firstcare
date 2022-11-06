<template>
<form @submit.prevent="SubmitBillingForm({'icd_version':selectedIcd,'status':selectedStatus,'pre_authorization_approval':preauthapproval,'refferal_num':refferal_num,'appointment_id':selectedAppointment})">
    <CustomToast v-if="displaytoast==true"/>
    <div class="grid mt-4 p-3">
        <div class="col-12">
            <CustomTitleHeader title="Billing" />
        </div>
        <div class="col-6">
            <CustomAutoComplete class="w-full" placeholder="Search Patient By Name or ID.." :selectedPatient="selectedPatient"/>
        </div>
        <div class="col-6">
            <Dropdown v-model="selectedAppointment" :options="patientAppointments" placeholder="Select Appointment" class="w-full" :disabled="appointDropdown" optionLabel="appointment" @change="getAllAppointPayments(selectedAppointment)"/>
        </div>
        <div class="grid col-6">
            <div class="col-2 pt-2">
                <label for="" class="text-center">Billing Status</label>
            </div>
            <div class="col-10">
                <Dropdown v-model="selectedStatus" :options="status" placeholder="Select Billing Status"
                    class="w-full" />
            </div>
        </div>
        <div class="grid col-6">
            <div class="col-2">
                <label for="" class="pt-2">ICD Version</label>
            </div>
            <div class="col-10">
                <Dropdown v-model="selectedIcd" :options="ICD" placeholder="Select ICD Version" class="w-full" />
            </div>
        </div>
        <div class="grid col-6">
            <div class="col-3">
                <label for="" class="pt-2">Patient Payments</label>
            </div>
            <div class="grid col-6">
                <div class="p-inputgroup">
                    <span class="p-inputgroup-addon">$</span>
                    <InputText v-model="billing_patient_total_balance" :value="billing_patient_total_balance" disabled />
                    <span class="p-inputgroup-addon"></span>
                </div>
            </div>
            <div class="col-3">
                <Button icon="pi pi-plus" iconPos="center" class="p-button-text"
                    @click="addPaymentDialog=!addPaymentDialog" :disabled="appointDropdown"/>
                <Dialog header="Add New Payment" v-model:visible="addPaymentDialog"
                    :breakpoints="{'960px': '75vw', '640px': '100vw'}" :style="{width: '50vw'}" position="top">
                    <div class="grid col-12">
                        <div class="grid col-12">
                            <div class="col-5">
                                <label for="">Payment Date</label>
                            </div>
                            <div class="col-7">
                                <Calendar v-model="paymentDate" placeholder="payment date.." class="w-full" />
                            </div>
                        </div>
                        <div class="grid col-12">
                            <div class="col-5">
                                <label for="">Appointment</label>
                            </div>
                            <div class="col-7">
                                <Dropdown v-model="selectedAppointment" :options="patientAppointments"
                                    placeholder="Select appointment" class="w-full" optionLabel="appointment" @change="getAllAppointPayments(selectedAppointment)"/>
                            </div>
                        </div>
                        <div class="grid col-12">
                            <div class="col-5">
                                <label for="">Payment Method</label>
                            </div>
                            <div class="col-7">
                                <Dropdown v-model="selectedPaymentMethod" :options="payment_methods"
                                    placeholder="Select Payment Method" class="w-full" optionLabel="name"/>
                            </div>
                        </div>
                        <div class="grid col-12">
                            <div class="col-5">
                                <label for="">Payment Type</label>
                            </div>
                            <div class="col-7">
                                <Dropdown v-model="selectedPaymentType" :options="payment_types"
                                    placeholder="Select Payment TYpe" class="w-full" optionLabel="name"/>
                            </div>
                        </div>
                        <div class="grid col-12">
                            <Textarea v-model="notes" placeholder="notes..." class="w-full border-1 p-2" />
                            </div>
                        <div class="grid col-12">
                            <div class="col-5">
                                <label for="">Amount</label>
                            </div>
                            <div class="col-7">
                                <div class="p-inputgroup">
                                    <span class="p-inputgroup-addon">$</span>
                                    <InputText v-model="payment_amount"/>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <CustomDataTable :table_columns="table_columns" :table_data="appointment_table_payments" />
                        </div>
                    </div>
                    <template #footer>
                        <Button label="Cancel" icon="pi pi-times" class="p-button-text p-text-danger"/>
                        <Button label="Add" icon="pi pi-check" autofocus @click="addPayment"/>
                    </template>
                </Dialog>
            </div>
        </div>
        <div class="grid col-6">
            <div class="col-3 pt-2">
                <label for="" class="text-center">Pre Authorized Approval</label>
            </div>
            <div class="col-9">
                <InputText v-model="preauthapproval" class="w-full"/>
            </div>
        </div>
        <div class="grid col-6">
            <div class="col-3 pt-2">
                <label for="" class="text-center">Refferal#</label>
            </div>
            <div class="col-9">
                <InputText v-model="refferal_num" class="w-full"/>
            </div>
        </div>
        <!-- <div class="grid col-6">
            <div class="col-3 pt-2">
                <label for="" class="text-center">Payment Profile</label>
            </div>
            <div class="col-9">
                <Dropdown v-model="selectedAppointment" :options="appointment" placeholder="Select Profile" class="w-full" />
            </div>
        </div> -->
        <div class="col-12 mt-2 border-1 surface-border">
            <CustomDataTable :table_columns="table_columns" :table_data="table_data" title="ICD 10 CODES"/>
        </div>
        <div class="col-6  mt-2 border-1 surface-border">
            <CustomDataTable :table_columns="table_columns" :table_data="table_data" title="CPT CODES"/>
        </div>
        <div class="col-6  mt-2 border-1 surface-border">
            <CustomDataTable :table_columns="table_columns" :table_data="table_data" title="HCPCS CODES"/>
        </div>
        <Button label="submit" type="submit" class="p-button-primary w-full"></Button>
    </div>
</form>
</template>


<script>
import CustomTitleHeader from '@/components/PatientManagement/Custom/CustomTitleHeader.vue'
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
import CustomAutoComplete from '@/components/Custom/CustomAutoComplete.vue'
import {mapState,mapActions, mapMutations} from 'vuex'
import CustomToast from '@/components/Custom/CustomToast.vue'
export default {
    name: "Billing",
    components: {
        CustomTitleHeader,
        CustomDataTable,
        CustomAutoComplete,
        CustomToast
    },
    mounted() {
        this.getToken()
        this.getAllPaymentType()
        this.getAllPaymentMethod()
    },
    computed:{
        ...mapState(['appointDropdown','token','patientAppointments','payment_types','payment_methods','appointment_table_payments','billing_patient_total_balance','displaytoast'])
    },
    methods:{
        ...mapMutations(['getToken']),
        ...mapActions(['getAllPaymentType','getAllPaymentMethod','getAllAppointPayments','addAppointmentPayment','SubmitBillingForm']),
        addPayment(){
            this.addAppointmentPayment({'payment_date':this.paymentDate,'appointment_id':this.selectedAppointment,'type_id':this.selectedPaymentType,'method_id':this.selectedPaymentMethod,'note':this.notes,'amount':this.payment_amount})
            this.payment_amount=0;
            this.selectedPaymentMethod=null;
            this.selectedPaymentType=null;
            this.notes=null;
            this.addPaymentDialog = false;

        }
    },
    data() {
        return {
            addPaymentDialog:false,
            selectedStatus: null,
            selectedIcd: null,
            paymentDate:null,
            preauthapproval:null,
            refferal_num:null,
            payment_amount:0,
            selectedAppointment:null,
            selectedPaymentMethod:null,
            selectedPaymentType:null,
            selectedPatient:null,
            notes:null,
            status: ["Paid In Full","Balance Due","Settled","Internal Review","Bill Insurance","Bill Secondary Insurance","Worker's Comp Claim","Auto Accident Claim","Durable Medical Equipment Claim"],
            ICD:["AUTO",'ICD-10',"ICD-9"],
            table_columns:[
                {
                    'field': "code",
                    "header": "Code"
                },
                {
                    'field': "balance",
                    "header": "Balance"
                },
                {
                    'field': "type",
                    "header": "Payment Type"
                },
            ],
            table_data:[]
        }
    }
}
</script>