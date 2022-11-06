import { createStore } from 'vuex'
import axios from 'axios'
import Constants from './constants'
import router from "../router/index"
import moment  from 'moment'


var constants = new Constants();

export default createStore({
  state: {
    patients: [],
    appointDropdown:true,
    login:false,
    login_message:null,
    token:null,
    billing_patient_total_balance:0,
    patientAppointments:[],
    payment_types:[],
    payment_methods:[],
    appointment_table_payments:[],
    selectedPatient:null,
    toast_message:null,
    toast_title:null,
    toast_severity:null,
    displaytoast:false
  },
  getters: {
  },
  mutations: {
    updatePatient(state,payload){
      let responseList = []
      for (let index = 0; index < payload.data.length; index++) {
        responseList.push(String(payload.data[index]['patient_id']))
      }
      state.patients = responseList
    },
    changeAppointmentDropdownStatus(state,payload){
      console.log(payload)
      state.patientAppointments = payload
      if(payload.length === 0){
        state.appointDropdown = true
      }
      else{
        state.appointDropdown = false
      }
    },
    login(state){
      state.login=true
      router.push({name:'patient-management'})
    },
    getToken(state){
      const token =  localStorage.getItem('user');
      if (token?.length ===0 || token===null){
        router.push({name:'login'})
      }
      else{
        state.token=token;
      }
    },
    logout(){
      localStorage.removeItem('user');
      router.push({name:'login'})
    },
    changeSelectedPatient(state,payload){
      state.selectedPatient=payload
    },
    changeToastData(state,payload){
      state.toast_severity = payload.severity;
      state.toast_message= payload.message;
      state.toast_title= payload.title;
      state.displaytoast = true;
      setTimeout(()=>{
        state.displaytoast = false;
      },5000)
    }
  },
  actions: {
    async getSpecificPatient({commit,state},patient_id){
      console.log(patient_id)
      axios(
        {
        method:"GET",
        url: constants.searchPatient,
        headers: {
          'Authorization': `Token ${state.token}`
        },
        params:{
          "patient_id":patient_id
        }
      })
      .then((response)=>{
        commit("updatePatient",response.data)
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async Login({commit,state},payload){
      axios({
        method:"POST",
        url: constants.login,
        data:{
          "username":payload.username,
          "password":payload.password
        }
      })
      .then((response)=>{
        localStorage.setItem('user', response.data.key);
        state.login_message="Login Successful!!"
        commit("login");
      })
      .catch((error)=>{
        state.login_message="Invalid username or password!!"
        console.log(error)
      })
    },
    async getAllPatientAppointment({commit,state},payload){
      axios({
        method:"GET",
        url: constants.appointment,
        headers:{
          'Authorization': `Token ${state.token}`
        },
        params:{
          "patient_id": payload
        }
      }).then((response) =>{
        let resp = response.data.data;
        console.log(resp)
        let response_list = [];
        for (let index = 0; index < resp.length; index++) {
          const element = resp[index];
          let datetime = moment(element.date_time).format('MM-DD-YYYY HH:MM:SS')
          response_list.push({id:resp[index]['id'],appointment:datetime})
        }
        commit('changeAppointmentDropdownStatus',response_list)
        commit('changeSelectedPatient',payload)
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async getAllPaymentType({state,commit}){
      axios({
        method:"GET",
        url:constants.paymenttype,
        headers:{
          "Authorization": `Token ${state.token}`
        }
      })
      .then((response)=>{
        state.payment_types=response.data.data
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async getAllPaymentMethod({state,commit}){
      axios({
        method:"GET",
        url:constants.paymentmethod,
        headers:{
          "Authorization": `Token ${state.token}`
        }
      })
      .then((response)=>{
        console.log(response.data.data)
        state.payment_methods=response.data.data
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async getAllAppointPayments({state,commit},payload){
      axios({
        method:"GET",
        url:constants.AppointmentPayment,
        headers:{
          "Authorization": `Token ${state.token}`
        },
        params:{
          "appointment_id":payload.id
        }
      })
      .then((response) => {
        let resp = response.data.data;
        for (let index = 0; index < resp.length; index++) {
          const element = resp[index];
          state.billing_patient_total_balance += element.amount;
          state.appointment_table_payments.push({
            code:element.id,
            balance: element.amount,
            type:element.type.name
          })
        }
        console.log(state.appointment_table_payments)
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async addAppointmentPayment({state,commit},payload){
      axios({
        method:'POST',
        url:constants.AppointmentPayment,
        headers:{
          "Authorization": `Token ${state.token}`
        },
        data:{
          "payment_date":payload.payment_date,
          "appointment_id":payload.appointment_id.id,
          "type_id":payload.type_id.id,
          "method_id":payload.method_id.id,
          "note":payload.note,
          "amount":payload.amount
        }
      })
      .then((response)=>{
        const element = response.data.data;
        state.billing_patient_total_balance += element.amount;
          state.appointment_table_payments.push({
            code:element.id,
            balance: element.amount,
            type:element.type.name
          })
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    async SubmitBillingForm({state,commit},payload){
      axios({
        method:'POST',
        url:constants.billing,
        headers:{
          "Authorization": `Token ${state.token}`
        },
        data:{
          'patient_id':state.selectedPatient,
          'icd_version':payload.icd_version,
          'status':payload.status,
          'pre_authorization_approval':payload.pre_authorization_approval,
          'refferal_num':payload.refferal_num,
          'appointment':payload.appointment_id.id
        }
      })
      .then((response)=>{
        commit('changeToastData',{'message':"Billing Saved",'title':'Successful!!','severity':'success'})
        console.log(response.data)
      })
      .catch((error)=>{
        console.log(error.response.data.message)
        commit('changeToastData',{'message':error.response.data.message,'title':'Error!!','severity':'error'})
      })
    }
  },
  modules: {
  }
})
