import moment from 'moment';

class Constants {
    token = "Token 275ddfa517c68a2c195375e2dde4b02bb415eead";

    base_url = 'http://20.127.29.249:8000/';
    // base_url = 'http://127.0.0.1:8000/';

    billing_url = this.base_url+'billing/api/billing/';

    fhir = this.base_url+'fhir/api/';
    check_coverage_request = this.fhir+'checkcoverage/';

    
    eligibility_request_patient_healthcare = this.fhir+'eligibilityrequestauto/';
    eligibility_request_manual = this.fhir+'eligibilityrequestmanual/';
    resend_eligibility_request_manual = this.fhir+'resendeligibilityrequest/';
    eligibility_details = this.fhir+'eligibilityrequestmanual/'

    patient = this.base_url+'patient/api/';
    getPatient = this.patient+'patient/';
    getInsuranceSearchBeneficiary = this.patient+'patientsearchnsurance/';

    addNewPatient = this.patient+'patientinsurance/';

    getdiagnosisinformation = this.fhir+'diagnosisinformation/'
    getsupportinginfo = this.fhir+'supportinginfo/'

    drchrono_insurance = this.base_url+'drchronoinsurance/api/';

    insurance = this.drchrono_insurance+'insurance/';


    management = this.base_url+'management/';

    doctor_management = this.management+'doctor/api/';

    department = this.doctor_management+'department/';








    convertDateFormat(date){
        return moment(date).format('YYYY-MM-DD');
    }
}

export default Constants;