import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class BeneficiaryServices{
    async getAllBeneficiary() {
      var resp = await axios({
        url:constants.getPatient,
        headers:{
          "Authorization": constants.token
        }
        });
        return resp.data;
    }
    async getSearchBeneficiary(document_id,first_name,second_name,file_id,number,start_date,end_date,selectedInsuracePlan,selectedGender) {
        const res = await axios({
          url:constants.getPatient,
          headers: {
            "Authorization": constants.token
          },
          params:{
            document_id: document_id??'',
            first_name: first_name??'',
            second_name: second_name??'',
            file_id: file_id??'',
            number: number??'',
            start_date: constants.convertDateFormat(start_date)??'',
            end_date: constants.convertDateFormat(end_date)??'',
            insurance_plan: selectedInsuracePlan??'',
            gender: selectedGender??'',
          }
        });
      return res.data;
    }
    
    async addNewBeneficiary(first_name,second_name,third_name,file_id,dobH,dob,e_health_id,document_id,phone_number,emergency_phone_number,email,insurance_plan,selectDocumentType,selectresidentialType,selectNationality,selectMaritialStatus,selectGender,selectBloodGroup,selectPrefferLang){
        let _data = {
          first_name:first_name,
          second_name:second_name,
          third_name:third_name,
          file_id:file_id,
          DOB_hijri:constants.convertDateFormat(dobH),
          DOB:constants.convertDateFormat(dob),
          e_health_id:e_health_id,
          document_id:document_id,
          phone_number:phone_number,
          emergency_contact_number:emergency_phone_number,
          email:email,
          insurance_plan:insurance_plan,
          document_type:selectDocumentType,
          residency_type:selectresidentialType,
          nationality:selectNationality,
          maritail_status:selectMaritialStatus,
          gender:selectGender,
          blood_group:selectBloodGroup,
          preffered_language:selectPrefferLang
        }
        const res = await axios({
          url:constants.addNewPatient,
          method:"POST",
          headers:{
            "Authorization": constants.token
          },
          data:_data
        });
      return res.data;
    }
    async updateBeneficiary(data){
        let _data = {
          first_name:data.first_name,
          second_name:data.second_name,
          third_name:data.third_name,
          file_id:data.file_id,
          DOB_hijri:constants.convertDateFormat(data.DOB_hijri),
          DOB:constants.convertDateFormat(data.DOB),
          e_health_id:data.e_health_id,
          document_id:data.document_id,
          phone_number:data.contact_info.phone_number,
          emergency_contact_number:data.contact_info.emergency_phone_number,
          email:data.contact_info.email,
          insurance_plan:data.insurance_plan,
          document_type:data.document_type,
          residency_type:data.residency_type,
          nationality:data.nationality,
          maritail_status:data.maritail_status,
          gender:data.gender,
          blood_group:data.blood_group,
          preffered_language:data.preffered_language
        }
        console.log(`this is data:${_data}`);
        const res = await axios({
          url:constants.addNewPatient,
          method:"PUT",
          headers:{
            "Authorization": constants.token
          },
          data:_data
        });
      return res.data;
    }


    async getInsuranceSeatchBeneficiary(id){
      var resp = await axios({
        method:"GET",
        url:constants.getInsuranceSearchBeneficiary,
        params:{
          PatientKey:id
        },
        headers: {
          "Authorization": constants.token
        },
      });
      return resp.data;
    }

    async saveInsuranceSeatchBeneficiaryDetails(insurance_payload,id){
      let _data={
        insurance_payload:insurance_payload,
        document_id:id
      }
      var resp = await axios({
        method:"POST",
        url:constants.getInsuranceSearchBeneficiary,
        headers: {
          "Authorization": constants.token
        },
        data:_data
      });
      return resp.data;
    }

    async getInsuranceDetails(id){
      const resp = await axios({
        url: constants.insurance,
        method:"GET",
        headers: {
          "Authorization": constants.token
        },
        params:{
          'document_id':id
        }
      });
      return resp.data;
    }
}