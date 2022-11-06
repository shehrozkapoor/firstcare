<template>
    <form action="">
    <div class="grid mt-4 p-3">
        <div class="col-12">
            <p class="text-xl font-bold">Related Information</p>
            <hr>
        </div>
        <div class="col-6">
        <CustomAutoComplete class="w-full" placeholder="Search Patient By Name or ID.."/>
        </div>
        <div class="grid col-6">
            <div class="col-2 pt-3">
            <label for="relation">Relationship</label>
            </div>
            <div class="col-10">
            <CustomInput placeholder="relationship with patient" type="text" class="w-full" />
            </div>
        </div>
        <div class="col-6">
            <label for="First Name">First Name</label>
            <CustomInput placeholder="first name" type="text" class="w-full" />
        </div>
        <div class="col-6">
            <label for="last Name">Last Name</label>
            <CustomInput placeholder="last name" type="text" class="w-full" />
        </div>
        <div class="col-2">
            <label for="last Name">Contact Type</label>
            <CustomSelect :items="items"/>
        </div>
        <div class="col-4">
            <label for="contact-details">Contact Details</label>
            <CustomInput placeholder="Contact.." type="text" class="w-full" />
        </div>
        <div class="col-2">
            <label for="Gender">Gender</label>
            <CustomSelect :items="gender"/>
        </div>
        <div class="col-2 ml-3">
            <label for="Gender">Date Of Birth</label>
            <Calendar v-model="dob" />
        </div>
        <div class="col-2">
            <label for="blood-group">Upload Image</label>
            <FileUpload mode="basic" name="demo[]" url="./upload" accept="image/*" />
        </div>
    </div>
    <hr>

    <CustomAddressForm />

    <Button label="Submit" type="submit" class="w-full"/>
</form>
</template>

<script>
import CustomAutoComplete from '@/components/Custom/CustomAutoComplete.vue'
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomAddressForm from '@/components/PatientManagement/Custom/CustomAddressForm.vue'

export default {
    name:"RegistrationRelatedInformation",
    components:{
        CustomAutoComplete,
        CustomInput,
        CustomSelect,
        CustomAddressForm
    },
    data(){
        return{
            items:['phone','fax','email','pager','url','sms','other'],
            gender:['male','female','other','unknown'],
            dob:''
        }
    }
}
</script>