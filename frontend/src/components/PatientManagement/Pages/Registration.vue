<template>
<form action="">
    <div class="grid mt-4 p-3">
        <CustomTitleHeader title="Patient Registration" />
        <div class="col-4">
            <label for="Patient-id">Patient ID</label>
            <CustomInput placeholder="patient-id" type="text" value="0" />
        </div>
        <div class="col-4">
            <label for="Registeration-date">Registration Date</label>
            <CustomInput type="date" />
        </div>
        <div class="col-4">
            <label for="Registeration-type">Registration Type</label>
            <CustomSelect :items="items" />
        </div>
        <div class="col-3">
            <label for="Registeration-type">Account ID</label>
            <CustomInput placeholder="account-id" type="text" value="0" />
        </div>
        <div class="col-3">
            <label for="Registeration-type">Relationship</label>
            <CustomSelect :items="items" />
        </div>
        <div class="col-2">
            <Button label="Passport Auth" />
        </div>
        <div class="col-3">
            <label for="health-id">Health ID</label>
            <CustomInput placeholder="health-id" type="text" />
        </div>
        <div class="col-4">
            <label for="identification-type">Identification Type</label>
            <CustomSelect :items="items" />
        </div>
        <div class="col-3">
            <label for="id-number">ID Number</label>
            <CustomInput placeholder="id-number" type="text" />
        </div>
        <div class="col-2">
            <Button label="ID Auth" />
        </div>
    </div>

    <hr />




    <!-- Basic Info Start -->


    <div class="grid mt-4 p-3">
        <CustomTitleHeader title="Basic Info"/>
        <div class="grid col-8">
            <div class="col-6">
                <label for="id-number">First Name</label>
                <CustomInput placeholder="first-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">First Name Arabic</label>
                <CustomInput placeholder="first-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Second Name</label>
                <CustomInput placeholder="second-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Second Name Arabic</label>
                <CustomInput placeholder="second-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Third Name</label>
                <CustomInput placeholder="third-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Third Name Arabic</label>
                <CustomInput placeholder="third-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Last Name</label>
                <CustomInput placeholder="Last-name" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="id-number">Last Name Arabic</label>
                <CustomInput placeholder="Last-name" type="text" class="w-full" />
            </div>
            <div class="col-3">
                <label for="dob">Date Of Birth</label>
                <Calendar v-model="dob" />
            </div>
            <div class="col-2 ml-2 mt-1">
                <label for="blood-group">Blood Group</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-2 col-offset-1 mt-1">
                <label for="blood-group">RH Factor</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-2 col-offset-1 mt-1">
                <label for="blood-group">Marital Status</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-2">
                <label for="blood-group">File Type</label>
                <FileUpload mode="basic" name="demo[]" url="./upload" accept="image/*" />
            </div>
            <div class="col-2">
                <label for="blood-group">DOB in Hijri</label>
                <!-- need to be changed to hijri in future -->
                <Calendar v-model="hijri_dob" />
            </div>
            <div class="field-checkbox col-2 mt-4">
                <Checkbox name="patient-pregnant" value="patient-pregnant" v-model="gender" />
                <label for="patient-pregnant">patient pregnant</label>
            </div>
            <div class="field-checkbox col-2 mt-4">
                <Checkbox name="privilege-member" value="privilege-member" v-model="gender" />
                <label for="privilege-member">privilege member</label>
            </div>
            <div class="col-4">
                <label for="id-number">Membership #</label>
                <CustomInput placeholder="Membership#.." type="text" class="w-full" />
            </div>
            <div class="col-3">
                <label for="id-number">Age</label>
                <CustomInput placeholder="age" type="number" value="0" class="w-full" />
            </div>
            <div class="col-3">
                <label for="id-number">years</label>
                <CustomInput placeholder="years" type="number" value="0" class="w-full" />
            </div>
            <div class="col-3">
                <label for="id-number">months</label>
                <CustomInput placeholder="months" type="number" class="w-full" />
            </div>
            <div class="col-2">
                <label for="nationality">Nationality</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
            <div class="col-4 mt-4">
                <Button label="Renew Membership" />
            </div>
            <div class="col-4">
                <label for="">Expiry Date</label>
                <Calendar v-model="expiry_date" />
            </div>
        </div>
        <div class="grid col-4">
            <div class="col">
                <label for="id-number" class="col-12">Gender</label>
                <div class="field-checkbox col-4">
                    <Checkbox name="male" value="male" v-model="gender" />
                    <label for="male">Male</label>
                </div>
                <div class="field-checkbox col-4">
                    <Checkbox name="female" value="female" v-model="gender" />
                    <label for="female">Female</label>
                </div>
                <div class="field-checkbox col-4">
                    <Checkbox name="unknown" value="unknown" v-model="gender" />
                    <label for="unknown">Unknown</label>
                </div>
            </div>
        </div>
    </div>
    <hr />
    <!-- Basic Info ends -->

    <!-- contact information starts -->
    <div class="grid mt-4 p-3">
        <CustomTitleHeader title="Contact Information"/>
        <div class="grid col-7">
            <div class="col-6">
                <label for="phone-res">Phone Residence</label>
                <CustomInput placeholder="phone residence" type="text" class="w-full" />
            </div>
            <div class="col-6">
                <label for="phone-off">Off.</label>
                <CustomInput placeholder="phone off" type="text" class="w-full" />
            </div>
            <div class="col-4">
                <label for="phone-num">mobile</label>
                <CustomInput placeholder="mobile number" value="05" type="text" class="w-full" />
            </div>
            <div class="field-checkbox col-3 mt-5 col-offset-1">
                <Checkbox name="int-mob" value="int-mob" v-model="gender" />
                <label for="int-mob">Int. Mob</label>
            </div>
            <div class="col-4">
                <label for="phone-off">Off.</label>
                <CustomInput placeholder="phone off" type="text" class="w-full" />
            </div>
            <div class="col-12">
                <label for="phone-off">Email Address</label>
                <CustomInput placeholder="Email" type="email" class="w-full" />
            </div>
            <div class="col-12">
                <label for="phone-off">Emergency Contact Name</label>
                <CustomInput placeholder="phone off" type="text" class="w-full" />
            </div>
            <div class="col-4">
                <label for="emergency-phone-no">Emergency Contact No</label>
                <CustomInput placeholder="emergency contact number" type="text" class="w-full" />
            </div>
            <div class="field-checkbox col-3 mt-5 col-offset-1">
                <Checkbox name="send-email" value="send-email" v-model="gender" />
                <label for="send-email">Send Email</label>
            </div>
            <div class="field-checkbox col-4 mt-5">
                <Checkbox name="send-sms" value="send-sms" v-model="gender" />
                <label for="send-sms">Send Sms</label>
            </div>
            <div class="field-checkbox col-12 mt-5">
                <Checkbox name="health-summary" value="health-summary" v-model="gender" />
                <label for="health-summary">Receive Health Summary Report</label>
            </div>
            <div class="grid">
                <div class="col-4">
                    <label for="Pay-type">Patient Pay Type</label>
                </div>
                <div class="col-8 border-1 d-flex flex-row">
                    <div class="field-checkbox col-3">
                        <Checkbox name="company" value="company" v-model="gender" />
                        <label for="company">company</label>
                    </div>
                    <div class="field-checkbox col-3 col-offset-1 pl-3">
                        <Checkbox name="insurance" value="insurance" v-model="gender" />
                        <label for="insurance">Insurance</label>
                    </div>
                    <div class="field-checkbox col-3 col-offset-2">
                        <Checkbox name="self" value="self" v-model="gender" />
                        <label for="self">self</label>
                    </div>
                </div>
            </div>
            <div class="col-3 ml-3">
                <label for="prefer-lang">Pref Lang</label>
                <CustomSelect :items="items" class="w-full" />
            </div>
        </div>
        <div class="grid col-4 border-1 col-offset-1">
            <label for="">others</label>
            <div class="field-checkbox col-3">
                <Checkbox name="donate-blood" value="donate-blood" v-model="gender" />
                <label for="donate-blood">willing to donate blood</label>
            </div>
            <div class="field-checkbox col-3">
                <Checkbox name="emergency-patient" value="emergency-patient" v-model="gender" />
                <label for="emergency-patient">Emergency Patient</label>
            </div>
            <div class="field-checkbox col-3">
                <Checkbox name="data-update" value="data-update" v-model="gender" />
                <label for="data-update">Require Data Update</label>
            </div>
            <div class="col-12">
                <label for="emergency-phone-no">Last Modification Date</label>
                <Calendar v-model="mod_date" class="w-full" />
            </div>
            <div class="col-12">
                <label for="emergency-phone-no">Modified User Name</label>
                <CustomInput placeholder="name" type="text" class="w-full" />
            </div>
            <div class="grid">
                <div class="col-2">
                    <label for="Pay-type">Status</label>
                </div>
                <div class="col-10 d-flex flex-row w-full">
                    <div class="field-checkbox col-2">
                        <Checkbox name="active-status" value="active-status" v-model="gender" />
                        <label for="active-status">Active</label>
                    </div>
                    <div class="field-checkbox col-4 col-offset-1">
                        <Checkbox name="need-update-status" value="need-update-status" v-model="gender" />
                        <label for="need-update-status">Need to be Updated</label>
                    </div>
                    <div class="field-checkbox col-2">
                        <Checkbox name="hold-status" value="hold-status" v-model="gender" />
                        <label for="hold-status">Hold</label>
                    </div>
                    <div class="field-checkbox col-2">
                        <Checkbox name="inactive-status" value="inactive-status" v-model="gender" />
                        <label for="inactive-status">Inactive</label>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <hr>
    <!-- contact information ends -->

    <!-- Address Info Starts  -->
    <CustomAddressForm />
    <!-- Address Info ends  -->
    <Button label="Submit" type="submit" class="w-full"/>
</form>
</template>

<script>
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomHijriDatePicker from '@/components/Custom/CustomHijriDatePicker.vue'
import CustomAddressForm from '@/components/PatientManagement/Custom/CustomAddressForm.vue'
import CustomTitleHeader from '@/components/PatientManagement/Custom/CustomTitleHeader.vue'

export default {
    name:"PatientRegistration",
    components:{
        CustomInput,
        CustomSelect,
        CustomHijriDatePicker,
        CustomAddressForm,
        CustomTitleHeader
    },
    data(){
        return{
            items:[1,2,3],
            dob:'',
            hijri_dob:'',
            mod_date:'',
            expiry_date:'',
            gender:[],
            checked:false,
            date:''
        }
    }
}
</script>