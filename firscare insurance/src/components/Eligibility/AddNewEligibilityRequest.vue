<template>
    <Toast />
    <div class="grid">
        <div class="col-12">
            <Message severity="warn" class="text-lg font-bold">"All the Field with <span class="font-bold text-pink-700">*</span> are compulsory"</Message>
        </div>
        <div class="col-3">
            <label for="" class="text-lg font-bold col-12 ml-0 pl-0">Select Beneficiary <span class="font-bold text-pink-700">*</span></label>
            <Dropdown v-model="selectedBeneficiary" :options="beneficiaryOptions" optionLabel="document_id" :filter="true" filterPlaceholder="search..." placeholder="Select a Beneficiary" class="col-12" @change="OnSelectedBeneficiary"/>
        </div>
        <div class="col-3">
            <label for="" class="text-lg font-bold col-12 ml-0 pl-0">Select Eligibility Purpose</label>
            <MultiSelect v-model="SelectedEligibilityPurose" :options="EligibilityPuroseOptions" optionLabel="option" placeholder="Select a Eligibility Purpose" class="col-12" :disabled="purposeDisabled"/>
        </div>
        <div class="col-3">
            <label for="" class="text-lg font-bold col-12 ml-0 pl-0">Select Department/Location</label>
            <Dropdown v-model="selectedLocation" :options="locationOptions" optionLabel="name" :filter="true" filterPlaceholder="search..." placeholder="Select a Department/Location" class="col-12"/>
        </div>
        <div class="col-3">
            <label for="" class="text-lg font-bold col-12 ml-0 pl-0">Service Start Date<span class="font-bold text-pink-700">*</span></label>
            <Calendar v-model="startDate" placeholder="Select start date" class="col-12 h-4rem m-0 p-0" dateFormat="yy-mm-dd"/>
        </div>
        <div class="col-3">
            <label for="" class="text-lg font-bold col-12 ml-0 pl-0">Service End Date</label>
            <Calendar v-model="endDate" placeholder="Select end date" class="col-12 h-4rem m-0 p-0" dateFormat="yy-mm-dd"/>
        </div>
        <div class="col-12 flex flex-row justify-content-center align-content-center">
            <Button label="Send Eligibility Request" icon="pi pi-send" class="p-text-button p-button-success col-6" @click="onSubmitForm" :disabled="submitButtonDisabled"/>
        </div>
    </div>

</template>

<script>
import BeneficiaryServices from '@/service/BeneficiaryServices';
import LocationServices from '@/service/LocationServices';
import CoverageServices from '@/service/CoverageServices';
import EligibilityRequestService from '@/service/EligibilityRequestService';
export default {
    name:"AddNewEligibilityRequest",
    data(){
        return{
            selectedBeneficiary:null,
            beneficiaryOptions:null,
            selectedLocation:null,
            locationOptions:null,
            checkCoverage:false,
            startDate:null,
            purposeDisabled:true,
            submitButtonDisabled:true,
            endDate:null,
            SelectedEligibilityPurose:null,
            EligibilityPuroseOptions:[
                {option: 'Benefits', value: 'benefits'},
                {option: 'Validation', value: 'validation'},
            ]
        }
    },
    beneficiaryService:null,
    locationServices:null,
    created(){
        this.beneficiaryService = new BeneficiaryServices();
        this.locationServices = new LocationServices();
    },
    async mounted() {
        await this.beneficiaryService.getAllBeneficiary().then(response =>{
            this.beneficiaryOptions = response.data;
        })
        .catch((error)=>{
            console.log(error);
            this.showError('Unable to connect the server please check your internet or try after sometime!!!');
        });
        await this.locationServices.getAllLocations().then(response =>{
            this.locationOptions = response.data;
        })
        .catch((error)=>{
            console.log(error);
            this.showError('Unable to connect the server please check your internet or try after sometime!!!');
        });
    },
    methods:{
        showSuccess(message) {this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 6000});},
        showError(message) {this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 6000});},
        async OnSelectedBeneficiary(){
            this.purposeDisabled = true;
            this.submitButtonDisabled = true;
            this.SelectedEligibilityPurose=null;

            this.EligibilityPuroseOptions.forEach((item,key) =>{
                if(item.option==='Discovery'){
                    var result = this.EligibilityPuroseOptions.splice(key,1); 
                    console.log(result);
                }
            })


            const coverage_service = new CoverageServices();
            await coverage_service.checkCoverageBeneficiary(this.selectedBeneficiary.document_id).then(response =>{
                if(response.data.resourceType=='Coverage'){
                    this.purposeDisabled = false;
                    this.submitButtonDisabled = false;
                    this.showSuccess("Coverage Exist!! no option provided Discovery in Purpose")
                }
            })
            .catch(() => {
                this.showError("No Coverage Found!!.You can only send the eligibility request Beneficiary that have Coverage");
                if(!Object.hasOwn(this.EligibilityPuroseOptions, 2)){
                    this.EligibilityPuroseOptions.push({option: 'Discovery', value: 'discovery'},)
                }
                this.purposeDisabled = false;
            })
        },
        async onSubmitForm(){
            if(this.selectedBeneficiary === null || this.selectedLocation === null || this.startDate === null || this.SelectedEligibilityPurose === null){
                this.showError("Please Select All the Fields with *");
            }
            else{
                var purpose_list = [];
                this.SelectedEligibilityPurose.forEach(item =>{
                    purpose_list.push(item.value);
                });
                const eligibilityServices = new EligibilityRequestService();
                await eligibilityServices.sendEligibilityRequestManual(this.selectedBeneficiary.document_id,this.selectedLocation.fhir_id,this.startDate,this.endDate,purpose_list).then(()=>{
                    this.selectedBeneficiary=null;
                    this.selectedLocation=null;
                    this.purposeDisabled=true;
                    this.submitButtonDisabled=true;
                    this.endDate=null;
                    this.startDate=null;
                    this.SelectedEligibilityPurose=null;
                    this.showSuccess("Coverage Eligibility Request Submitted.you can see it in the transaction tab!")
                })
                .catch(error => {
                    console.log(error);
                })
            }
        }
    }
}
</script>