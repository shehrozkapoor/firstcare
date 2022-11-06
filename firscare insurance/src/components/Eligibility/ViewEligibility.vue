<template>
  <Toast />
  <div class="grid">
    <div class="header col-12">
      <Panel class="eligibilty-header" header="Eligibilty:">
        <div class="flex row">
          <div class="col">
            <p>Beneticiary Name: <b>{{ apiData && apiData.patient ? apiData.patient.first_name :'-' }} {{ apiData && apiData.patient ? apiData.patient.second_name :'-' }}</b></p>
            <p>Transection Date: {{ api ? api.name : "NA" }}</p>
          </div>
          <div class="col">
            <p>Service Date: <b>{{ apiData && apiData.response_bundle ? apiData.response_bundle.entry[1].resource.servicedPeriod.start : "NA" }} - {{ apiData && apiData.response_bundle ? apiData.response_bundle.entry[1].resource.servicedPeriod.end : "NA" }}</b></p>
            <p>Eligibility Purpose: <b>{{ apiData && apiData.response_bundle ? String(apiData.response_bundle.entry[1].resource.purpose) : "NA" }}</b></p>
          </div>
          <div class="col">
            <p>Department Name: {{apiData && apiData.patient ? apiData.patient.department :'NA'}}</p>
          </div>
        </div>
        <div class="mt-4 text-primary">
          <p><i class="pi pi-sliders-h"></i> TABLE OF BENEFITS</p>
          <Dropdown
            placeholder="Benefit Category - Medical Coverage"
            class="col-12"
          />
          <Dropdown
            placeholder="Benefit Category - Diagnostic XRay"
            class="col-12 mt-4"
          />
          <Dropdown
            placeholder="Benefit Category - Constitution"
            class="col-12 mt-4"
          />
          <Dropdown
            placeholder="Benefit Category - Surgical"
            class="col-12 mt-4"
          />
          <Dropdown
            placeholder="Benefit Category - Medical Care"
            class="col-12 mt-4"
          />
        </div>
      </Panel>
    </div>
    <div class="flex flex-row col-12">
      <div style="flex:3">
        <Button
        label="Reuse"
        icon="pi pi-undo"
        class="mr-2 mt-3 mb-3 p-button-warning"
      />

      <Button
        label="Progress To Autherization"
        class="mr-2 mt-3 mb-3 p-button-primary"
      />
      <Button
        label="Progress To Claim"
        class="mr-2 mt-3 mb-3 p-button-primary"
      />
      </div>
      <div>
      <Button
        label="Close"
        class="mt-3 mb-3 p-button-outlined p-button-secondary float-right"
        @click="$router.push({name: 'eligibility-transaction'})"
      />
    </div>
    </div>
  </div>
</template>



<script>
import {ref,onMounted} from 'vue'
import EligibilityService from "../../service/EligibilityRequestService";
import { useRoute } from "vue-router";
export default({
  setup() {
    let apiData = ref([]);
    onMounted(() => {
      const {
      params: { id },
    } = useRoute();
    const uid = id;
    let eligibilityService = new EligibilityService();
    eligibilityService.getEligibilityDetails(uid)
        .then((response) => {
          const { data } = response;
          let tempdepartment = [];
          console.log(data)
          data.map((data) => {
            tempdepartment.push({
              data
            });
          });
          apiData.value = tempdepartment[0].data
          console.log(apiData.value)
        })
        .catch((e) => {
          console.log("error :>> ", e);
        });
    });
    return{
      apiData,
    }
  },
})
</script>