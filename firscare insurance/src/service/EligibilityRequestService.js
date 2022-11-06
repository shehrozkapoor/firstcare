import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class EligibilityRequestService {
  async getInsuranceBilling() {
    const res = await axios.get(constants.billing_url, {
      headers: {
        "Authorization": constants.token
      }
    });
    return res.data;
  }
  async getAllEligibility() {
    const res = await axios.get(constants.eligibility_request_manual, {
      headers: {
        "Authorization": constants.token
      }
    });
    return res.data;
  }

  async resendEligibility(id) {
    const res = await axios.get(constants.resend_eligibility_request_manual, {
      headers: {
        "Authorization": constants.token
      },
      params: {
        eligibility_id: id
      }
    });
    return res.data;
  }
  async getEligibilityDetails(id) {
    const res = await axios.get(constants.eligibility_details, {
      headers: {
        "Authorization": constants.token
      },
      params: {
        coverage_id: id
      }
    });
    return res.data;
  }

  async getDiagnosisinformation() {
    const res = await axios.get(constants.getdiagnosisinformation, {
      headers: {
        "Authorization": constants.token
      }
    });
    return res.data;
  }
  async getSupportinginfo() {
    const res = await axios.get(constants.getsupportinginfo, {
      headers: {
        "Authorization": constants.token
      }
    });
    return res.data;
  }
  


  async sendEligibilityRequest(id) {
    var _data = {
      "billing-id": id
    }
    const res = await axios({
      url: constants.send_eligibility_request_patient_healthcare,
      method: "POST",
      headers: {
        "Authorization": constants.token,
      },
      body: _data
    }).then(response => response.json()).then(result => result).catch((error) => error);
    return res;
  }

  async sendEligibilityRequestManual(document_id, location_id, start_date, end_date, purpose) {
    var _data = {
      document_id: document_id,
      eligibility_purpose: purpose,
      location_id: location_id,
      start_date: start_date,
      end_date: end_date
    }
    const res = await axios({
      url: constants.eligibility_request_manual,
      method: "POST",
      headers: {
        "Authorization": constants.token,
      },
      data: _data
    }).then(response => response.json()).then(result => result).catch((error) => error);
    return res;
  }

}
