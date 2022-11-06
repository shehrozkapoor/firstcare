// development
const base_url = 'http://127.0.0.1:8000/';

// production
// const base_url = 'http://20.115.112.82:8000/';



const login = base_url+'api/accounts/auth/login/';

const user_info = base_url+'api/accounts/auth/user/';

const user_type = base_url+'api/accounts/userType/';

const get_token = base_url+'api/accounts/getToken/';

const logout_url = base_url+'api/accounts/auth/logout/';

const static_url = base_url+'static/';
const custom_template_url = static_url+'custom_templates/';


// insurance billing urls
const insurance_partials_base_url = static_url+'Partials/insurance/';
const insurance_static_base_url = static_url+'insurance/';


// api urls
const insurance_api_base_url = base_url+'drchronoinsurance/api/';
const insurance_billing_url = insurance_api_base_url+'billingsummary/';
const insurance_live_claim_url = insurance_api_base_url+'liveclaimfields/';
const insurance_batch_status_change_url = insurance_api_base_url+'batchStatusChange/';
const insurance_eligibility_status_url = insurance_api_base_url+'checkeligibility/';





const insurance_patient_payment_url = insurance_api_base_url+'patientpayments/';
const insurance_patient_payment_sub_data_url = insurance_api_base_url+'patientpaymentssubdata/';
const insurance_patient_payment_export_to_csv_url = insurance_api_base_url+'exportPatientPaymentToCsv/';


const reciept_url = custom_template_url+'recipt.html';
