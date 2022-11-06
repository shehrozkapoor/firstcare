

class Constants{
    // development
    base_url:string = "http://127.0.0.1:8000/";
    // production
    // base_url:string = "http://20.115.112.82:8000/";


    // patient
    patient:string = this.base_url+"patient/api/";
    searchPatient:string =  this.patient+'searchpatient/'
    // login
    login:string = this.base_url+'api/accounts/auth/login/';

    // getToken
    get_token:string = this.base_url+'api/accounts/getToken/';

    // management
    management:string = this.base_url+'management/';
    // schedule
    schedule:string = this.management+'schedule/api/';
    // appointment
    appointment:string = this.schedule+'appointment/';

    billing_base:string = this.base_url+'billing/api/';

    paymenttype:string = this.billing_base+'paymenttype/';
    paymentmethod:string = this.billing_base+'paymentmethod/';
    AppointmentPayment:string = this.billing_base+'payment/';
    billing:string = this.billing_base+'billing/';


}

export default Constants;