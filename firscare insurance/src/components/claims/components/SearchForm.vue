<template>
  <div class="grid">
    <div class="col-12">
      <div class="card">
        <div class="p-fluid formgrid grid">
          <div class="field col-6">
            <label for="insurer">Insurer</label>
            <InputText
              id="insurer"
              type="text"
              v-model="insurer"
              @keyup="$emit('updateProps', { field: 'insurer', val: insurer })"
            />
          </div>
          <div class="field col-6">
            <label for="insurancePlan">Insurance Plan</label>
            <InputText
              id="insurancePlan"
              type="text"
              v-model="insurancePlan"
              @keyup="
                $emit('updateProps', {
                  field: 'insurancePlan',
                  val: insurancePlan,
                })
              "
            />
          </div>
          <div class="field col-6">
            <label for="second_name">Start Date</label>
            <Calendar
              v-model="start_date"
              @date-select="
                $emit('updateProps', { field: 'start_date', val: start_date })
              "
              dateFormat="yy-mm-dd"
              :showTime="false"
            />
          </div>
          <div class="field col-6">
            <label for="second_name">End Date</label>
            <Calendar
              v-model="end_date"
              @date-select="
                $emit('updateProps', { field: 'end_date', val: end_date })
              "
              dateFormat="yy-mm-dd"
              :showTime="false"
            />
          </div>
          <div class="field col-6">
            <label for="claimID">Claim ID</label>
            <InputText
              id="claimID"
              type="text"
              v-model="claimID"
              @keyup="
                $emit('updateProps', {
                  field: 'claimID',
                  val: claimID,
                })
              "
            />
          </div>
          <div class="field col-6">
            <label for="beneficiary-type">Type</label>
            <Dropdown
              id="beneficiary-type"
              type="text"
              v-model="type"
              @keyup="$emit('updateProps', { field: 'type', val: type })"
            />
          </div>
          <div class="field col-6">
            <label for="contact-benificiary">Benificiary</label>
            <Dropdown
              id="contact-benificiary"
              type="text"
              v-model="benificiary"
              @keyup="
                $emit('updateProps', { field: 'benificiary', val: benificiary })
              "
            />
          </div>
          <div class="field col-3">
            <label for="start-date">Status</label>
            <Dropdown
              v-model="status"
              @date-select="
                $emit('updateProps', { field: 'status', val: status })
              "
              dateFormat="yy-mm-dd"
              :showTime="false"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "SearchBeneficiaryForm",
  props: [
    "p_insurer",
    "p_insurancePlan",
    "p_claimID",
    "p_second_name",
    "p_type",
    "p_benificiary",
    "p_status",
    "p_end_date",
    "p_start_date",
    "p_insurance_plan",
    "p_gender",
  ],
  data() {
    return {
      insurer: this.p_insurer,
      insurancePlan: this.p_insurancePlan,
      claimID: this.p_claimID,
      second_name: this.p_second_name,
      type: this.p_type,
      benificiary: this.p_benificiary,
      status: this.p_status,
      end_date: this.p_end_date,
      start_date: this.start_date,
      selectedInsuracePlan: this.p_insurance_plan,
      selectedGender: this.p_gender,
      insurancePlanDropDown: [
        { name: "Insurance Plan 1", code: "plan-1" },
        { name: "Insurance Plan 2", code: "plan-2" },
        { name: "Insurance Plan 3", code: "plan-3" },
      ],
    };
  },
  watch: {
    p_insurer() {
      this.insurer = this.p_insurer;
    },
    p_insurancePlan() {
      this.insurancePlan = this.p_insurancePlan;
    },
    p_second_name() {
      this.second_name = this.p_second_name;
    },
    p_type() {
      this.type = this.p_type;
    },
    p_benificiary() {
      this.benificiary = this.p_benificiary;
    },
    p_status() {
      this.status = this.p_status;
    },
	p_claimID() {
      this.claimID = this.p_claimID;
    },
    p_end_date() {
      this.end_date = this.p_end_date;
    },
    p_start_date() {
      this.end_date = this.p_end_date;
    },

    p_insurance_plan() {
      this.selectedInsuracePlan = this.p_insurance_plan;
    },
    p_gender() {
      this.selectedGender = this.p_gender;
    },
  },
};
</script>
