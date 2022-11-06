<template>
    <Toast />
    <Dialog header="Add New Beneficiary" :visible="display" :breakpoints="{'960px': '75vw', '640px': '90vw'}"
        :style="{width: '70vw'}" :maximizable="true" :modal="true" :closable="false" :draggable="false" position="top">
        <Divider />
        <div class="grid p-5">
            <div class="col-12">
                    <div class="p-fluid formgrid grid">
                        <div class="field col-6">
                            <label for="first-name" class="font-bold">Beneficiary First Name <span class="font-bold text-pink-700">*</span></label>
                            <InputText id="first-name" type="text" v-model="first_name"/>
                        </div>
                        <div class="field col-6">
                            <label for="second-name" class="font-bold">Beneficiary Second Name <span class="font-bold text-pink-700">*</span></label>
                            <InputText id="second-name" type="text" v-model="second_name"/>
                        </div>
                        <div class="field col-6">
                            <label for="third-name" class="font-bold">Beneficiary Third Name</label>
                            <InputText id="third-name" type="text" v-model="third_name"/>
                        </div>
                        <div class="field col-6">
                            <label for="file-id" class="font-bold">Beneficiary File ID</label>
                            <InputText id="file-id" type="text" v-model="file_id"/>
                        </div>
                        <div class="field col-6">
                            <label for="dobH" class="font-bold">Date Of Birth(Hijri)</label>
                            <Calendar id="dobH" type="text" v-model="dobH"/>
                        </div>
                        <div class="field col-6">
                            <label for="dob" class="font-bold">Date of Birth<span class="font-bold text-pink-700">*</span></label>
                            <Calendar id="dob" type="text" dateFormat="yy-mm-dd" v-model="dob"/>
                        </div>
                        <div class="field col-6">
                            <label for="e-health-id" class="font-bold">E-Health ID<span class="font-bold text-pink-700">*</span></label>
                            <InputText id="e-health-id" type="text" v-model="e_health_id"/>
                        </div>
                        <div class="field col-6">
                            <label for="nationality" class="font-bold">Nationality<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="nationality" optionLabel="type" v-model="selectNationality"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="residencey-type" class="font-bold">Residency Type<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="residentialType" optionLabel="type" v-model="selectresidentialType"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="residencey-type" class="font-bold">Document Type<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="documentType" optionLabel="type" v-model="selectDocumentType"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="document-id" class="font-bold">Document ID<span class="font-bold text-pink-700">*</span></label>
                            <InputText id="document-id" type="text" v-model="document_id"/>
                        </div>
                        <div class="field col-6">
                            <label for="contact-number" class="font-bold">Contact Number<span class="font-bold text-pink-700">*</span></label>
                            <InputText id="contact-number" type="text" v-model="phone_number"/>
                        </div>
                        <div class="field col-6">
                            <label for="maritial-status" class="font-bold">Maritial Status</label>
                            <Dropdown id="dropdown" :options="maritialStatus" optionLabel="type" v-model="selectMaritialStatus"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="gender" class="font-bold">Gender<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="gender" optionLabel="type" v-model="selectGender"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="blood-group" class="font-bold">Blood Group<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="bloodGroup" optionLabel="type" v-model="selectBloodGroup"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="prefred-lang" class="font-bold">Preferred language<span class="font-bold text-pink-700">*</span></label>
                            <Dropdown id="dropdown" :options="prefferLang" optionLabel="type" v-model="selectPrefferLang"></Dropdown>
                        </div>
                        <div class="field col-6">
                            <label for="emergency-contact-number" class="font-bold">Emergency phone number</label>
                            <InputText id="emergency-contact-number" type="text" v-model="emergency_phone_number"/>
                        </div>
                        <div class="field col-6">
                            <label for="email" class="font-bold">Email</label>
                            <InputText id="email" type="email" v-model="email"/>
                        </div>
                        <div class="field col-6">
                            <label for="insurance-plan" class="font-bold">Insurance plan</label>
                            <InputText id="insurance-plan" type="text" v-model="insurance_plan"/>
                        </div>
                </div>
            </div>
        </div>
        <template #footer>
            <Button label="Save & Add New" icon="pi pi-check" autofocus @click="submitForm(1)"/>
            <Button label="Save" icon="pi pi-check" autofocus @click="submitForm(2)"/>
            <Button label="cancel" icon="pi pi-times" class="p-button-text p-button-danger"
                @click="updateDisplayMaximizable" />
        </template>
    </Dialog>
</template>

<script>
import BeneficiaryServices from '@/service/BeneficiaryServices';

export default {
    name:"CustomAddBeneficiaryDialog",
    props:['displayMaximizable'],
    data(){
        return{
            display: this.displayMaximizable,
            first_name:null,
            second_name:null,
            third_name:null,
            file_id:null,
            dobH:null,
            dob:null,
            e_health_id:null,
            document_id:null,
            phone_number:null,
            emergency_phone_number:null,
            email:null,
            insurance_plan:null,
            selectDocumentType:null,
            selectresidentialType:null,
            selectNationality:null,
            selectMaritialStatus:null,
            selectGender:null,
            selectBloodGroup:null,
            selectPrefferLang:null,
            documentType:[
                {'type':'Resident Card','code':'rc'},
                {'type':'Passport','code':'passport'},
                {'type':'GCC ID','code':'gcc-id'},
                {'type':'National Card','code':'national-card'},
                {'type':'Boarder Number','code':'boarder-number'}
            ],
            residentialType:[
                {'type':'Visitor','code':'visitor'},
                {'type':'Dependent','code':'dependent'},
                {'type':'Citizen','code':'citizen'},
                {'type':'Resident','code':'resident'},
            ],
            nationality:[
                {'type':'Saudi Arabia','code':'sa'},
            ],
            maritialStatus:[
                {'type':'Single','code':'SINGLE'},
                {'type':'Married','code':'MARRIED'},
            ],
            gender:[
                {'type':'Male','code':'male'},
                {'type':'Female','code':'female'},
                {'type':'Other','code':'other'},
            ],
            bloodGroup:[
                {'type':'A+','code':'a+'},
                {'type':'B+','code':'b+'},
                {'type':'AB+','code':'ab+'},
                {'type':'AB-','code':'ab-'},
                {'type':'O+','code':'O+'},
                {'type':'O-','code':'O-'},
            ],
            prefferLang:[
                {'type':'English','code':'English'},
                {'type':'Arabic','code':'Arabic'},
            ],
        }
    },
    methods:{
        showSuccess(message) {
            this.$toast.add({severity:'success', summary: 'Success Message', detail:message, life: 3000});
        },
		showError(message) {
            this.$toast.add({severity:'error', summary: 'Error Message', detail:message, life: 3000});
        },
        updateDisplayMaximizable(){
            this.$emit("update-display-maximizable", false) 
        },
        async submitForm(id){
            if(this.first_name === null || this.first_name.length <=2 || this.second_name === null || this.second_name.length <=2 || this.dob === null || this.dob.length <=2 || this.e_health_id === null || this.e_health_id.length <= 0 || this.selectNationality === null || this.selectNationality.lenght == 0 || this.selectresidentialType === null || this.selectresidentialType.lenght == 0 || this.selectDocumentType === null || this.selectDocumentType.lenght == 0 || this.document_id === null || this.document_id.lenght == 0 || this.phone_number === null || this.phone_number.lenght == 0 || this.selectGender === null || this.selectGender.lenght == 0 || this.selectBloodGroup === null || this.selectBloodGroup.lenght == 0 || this.selectPrefferLang === null || this.selectPrefferLang.lenght == 0){
                this.showError('Please Fill All the Field with *');
            }
            else{
                const beneficiaryServices = new BeneficiaryServices();
                await beneficiaryServices.addNewBeneficiary(this.first_name,this.second_name,this.third_name,this.file_id,this.dobH,this.dob,this.e_health_id,this.document_id,this.phone_number,this.emergency_phone_number,this.email,this.insurance_plan,this.selectDocumentType.code,this.selectresidentialType.code,this.selectNationality.code,this.selectMaritialStatus.code,this.selectGender.code,this.selectBloodGroup.code,this.selectPrefferLang.code)
                .then((data)=>{
                    this.first_name=null;
                    this.second_name=null;
                    this.third_name=null;
                    this.file_id=null;
                    this.dobH=null;
                    this.dob=null;
                    this.e_health_id=null;
                    this.document_id=null;
                    this.phone_number=null;
                    this.emergency_phone_number=null;
                    this.email=null;
                    this.insurance_plan=null;
                    this.selectDocumentType=null;
                    this.selectresidentialType=null;
                    this.selectNationality=null;
                    this.selectMaritialStatus=null;
                    this.selectGender=null;
                    this.selectBloodGroup=null;
                    this.selectPrefferLang=null;
                    this.$emit('addNewRowBenefciaryTable',data.data);
                    if(id==1){
                        console.log('pass')
                    }
                else{
                    this.updateDisplayMaximizable();
                    }
                }).catch((error)=>{
                    console.log(error);
                    this.showError(error.response.data.message);
                });
            }
        }
    },
    watch:{
        displayMaximizable () {
        this.display = this.displayMaximizable
        }
    }
}
</script>