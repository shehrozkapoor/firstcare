<template>
	<div class="grid">
		<div class="col-12">
			<div class="card">
				<div class="p-fluid formgrid grid">
					<div class="field col-6">
						<label for="document-id">Document ID</label>
						<InputText id="document-id" type="text" v-model="document_id" @keyup="$emit('updateProps',{'field':'document_id','val':document_id})"/>
					</div>
					<div class="field col-6">
						<label for="first_name">First Name</label>
						<InputText id="first_name" type="text" v-model="first_name" @keyup="$emit('updateProps',{'field':'first_name','val':first_name})"/>
					</div>
					<div class="field col-6">
						<label for="second_name">Second Name</label>
						<InputText id="second_name" type="text" v-model="second_name" @keyup="$emit('updateProps',{'field':'second_name','val':second_name})"/>
					</div>
					<div class="field col-6">
						<label for="beneficiary-file-id">Beneficiary File ID</label>
						<InputText id="beneficiary-file-id" type="text" v-model="file_id" @keyup="$emit('updateProps',{'field':'file_id','val':file_id})"/>
					</div>
					<div class="field col-6">
						<label for="contact-number">Contact Number</label>
						<InputText id="contact-number" type="text" v-model="number" @keyup="$emit('updateProps',{'field':'number','val':number})"/>
					</div>
                    <div class="field col-3">
                        <label for="start-date">Start Date</label>
                        <Calendar  v-model="start_date" @date-select="$emit('updateProps',{'field':'start_date','val':start_date})" dateFormat="yy-mm-dd" :showTime="false"/>
                    </div>
                    <div class="field col-3">
                        <label for="end-date">End Date</label>
                        <Calendar  v-model="end_date" @date-select="$emit('updateProps',{'field':'end_date','val':end_date})" dateFormat="yy-mm-dd" :showTime="false"/>
                    </div>
					<div class="field col-6">
						<label for="insurance-plan">Insurance Plan</label>
                        <Dropdown id="insurance-plan" v-model="selectedInsuracePlan" :options="insurancePlan" optionLabel="name" placeholder="Insurance Plan" @change="$emit('updateProps',{'field':'insurance_plan','val':selectedInsuracePlan.code})"></Dropdown>
					</div>
                    <div class="field col-6">
						<label for="gender">Gender</label>
                        <Dropdown id="gender" v-model="selectedGender" :options="gender" optionLabel="name" placeholder="Gender" @change="$emit('updateProps',{'field':'gender','val':selectedGender.code})"></Dropdown>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default {
        name:"SearchBeneficiaryForm",
		props:['p_document_id','p_first_name','p_second_name','p_file_id','p_number','p_start_date','p_end_date','p_insurance_plan','p_gender'],
        data() {
			return {
				document_id:this.p_document_id,
				first_name:this.p_first_name,
				second_name:this.p_second_name,
				file_id:this.p_file_id,
				number:this.p_number,
				start_date:this.p_start_date,
				end_date:this.p_end_date,
				selectedInsuracePlan:this.p_insurance_plan,
				selectedGender:this.p_gender,
				insurancePlan: [
					{name: 'Insurance Plan 1', code: 'plan-1'},
					{name: 'Insurance Plan 2', code: 'plan-2'},
					{name: 'Insurance Plan 3', code: 'plan-3'}
				],
				gender: [
					{name: 'Male', code: 'male'},
					{name: 'Female', code: 'female'},
					{name: 'Other', code: 'other'}
				],
			}
		},
		watch:{
			p_document_id(){
				this.document_id=this.p_document_id
			},
			p_first_name(){
				this.first_name=this.p_first_name
			},
			p_second_name(){
				this.second_name=this.p_second_name
			},
			p_file_id(){
				this.file_id=this.p_file_id
			},
			p_number(){
				this.number=this.p_number
			},
			p_start_date(){
				this.start_date=this.p_start_date
			},
			p_end_date(){
				this.end_date=this.p_end_date
			},
			p_insurance_plan(){
				this.selectedInsuracePlan=this.p_insurance_plan
			},
			p_gender(){
				this.selectedGender=this.p_gender
			}
		}
	}
</script>
