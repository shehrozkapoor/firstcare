<template>
  <Toast />
  <div class="grid">
    <div class="col-12">
      <Message severity="warn" class="text-lg font-bold"
        >"All the Field with <span class="font-bold text-pink-700">*</span> are
        compulsory"</Message
      >
    </div>
    <div class="parent-body col-12">
      <div class="col-6">
        <h3>Pre-Authorization info :</h3>
      </div>
      <div class="fields col-6 flex flex-row">
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Date Ordered <span class="font-bold text-pink-700">*</span></label
          >
          <Calendar class="col-12 h-4rem mt-2 p-0" placeholder="Select Date" />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Type <span class="font-bold text-pink-700">*</span></label
          >
          <Dropdown placeholder="Select The Type" :options="preAuth_type"
            optionLabel="type" class="col-12 mt-2" />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >SubType</label
          >
          <Dropdown placeholder="Select SubType" class="col-12 mt-2" />
        </div>
      </div>
    </div>
    <div class="parent-body col-12 mt-2">
      <div class="col-6">
        <h3>Diagnosis Information :</h3>
      </div>
      <div class="fields col-6 flex flex-row">
        <div class="col-5">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Diagnosis Code/Description<span class="font-bold text-pink-700"
              >*</span
            ></label
          >
          <Dropdown
            placeholder="Select Diagnosis Code/Description"
            :options="diagnosis_type"
            optionLabel="icd_10"
            class="col-12 mt-2"
          />
        </div>
        <div class="col-3">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Type <span class="font-bold text-pink-700">*</span></label
          >
          <Dropdown
            :options="diagnosis_type"
            optionLabel="type"
            placeholder="Select The Type"
            class="col-12 mt-2"
          />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >On Admission <span class="font-bold text-pink-700">*</span></label
          >
          <Dropdown
            :options="diagnosis_type"
            optionLabel="on_admission"
            placeholder="Select Admission"
            class="col-12 mt-2"
          />
        </div>
      </div>
    </div>
    <div class="parent-body col-12 mt-2">
      <div class="col-6">
        <h3>Supporting Information :</h3>
      </div>
      <div class="fields col-6 flex flex-row">
        <div class="col-5">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Value Type <span class="font-bold text-pink-700">*</span></label
          >
          <Dropdown
            :options="supportive_type" optionLabel="type"
            placeholder="Select Diagnosis Code/Description"
            class="col-12 mt-2"
          />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Reason <span class="font-bold text-pink-700">*</span></label
          >
          <InputText
            placeholder="Enter Reason"
            class="col-12 mt-2 h-4rem mt-2 p-0"
          />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Category <span class="font-bold text-pink-700">*</span>
          </label>
          <Dropdown placeholder="Select Category" class="col-12 mt-2" :options="supportive_type" optionLabel="category" />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Value <span class="font-bold text-pink-700">*</span>
          </label>
          <Dropdown placeholder="Select Value" class="col-12 mt-2" :options="supportive_type" optionLabel="value" />
        </div>
        <div class="col-4">
          <label for="" class="text-lg font-bold col-12 ml-0 pl-0"
            >Code <span class="font-bold text-pink-700">*</span>
          </label>
          <Dropdown placeholder="Select Code" class="col-12 mt-2" :options="supportive_type" optionLabel="code" />
        </div>
      </div>
    </div>
    <div
      class="col-12 flex flex-row justify-content-center align-content-center"
    >
      <Button
        label="Send Pre-Autherization Request"
        icon="pi pi-send"
        class="p-text-button p-button-success col-6"
        @click="onSubmitForm"
        :disabled="submitButtonDisabled"
      />
    </div>
  </div>
</template>

<script>
import { onMounted } from "vue";
import EligibilityService from "@/service/EligibilityRequestService";
export default {
  setup() {
    let diagnosis_type = [];
    let supportive_type = [];
    let preAuth_type = [
      {'type': 'Institutional: Inpatient authorizations' },
      {'type': 'Professional: Outpatient authorizations' },
      {'type': 'Pharmacy: Outpatient Pharmacy authorizations' },
      {'type': 'Dental: Outpatient Dental authorizations' },
    ];
    onMounted(() => {
      let eligibilityService = new EligibilityService();
      eligibilityService
        .getDiagnosisinformation()
        .then((response) => {
          const { data } = response;
          data.map((x) => {
            diagnosis_type.push({
              type: x.type,
              icd_10: x.icd_10,
              on_admission: x.on_admission,
            });
          });
          //   apiData.value = tempdepartment[0].data
        })
        .catch((e) => {
          console.log("error :>> ", e);
        });
      eligibilityService
        .getSupportinginfo()
        .then((response) => {
          const { data } = response;
          console.log(response, data, "response");
          data.map((x) => {
            supportive_type.push({
              type: x.type,
              category: x.category,
              code: x.code,
              value: x.value,
            });
          });
        })
        .catch((e) => {
          console.log("error :>> ", e);
        });
    });
    return {
      diagnosis_type,
      supportive_type,
      preAuth_type
    };
  },
};
</script>


<style scoped>
.parent-body {
  background: white;
}
</style>