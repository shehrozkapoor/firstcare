import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class CoverageServices{
    async checkCoverageBeneficiary(document_id){
        const resp = await axios({
            url:constants.check_coverage_request,
            method:"GET",
            headers:{
                "Authorization": constants.token
            },
            params:{
                document_id:document_id
            },
        })
        return resp.data;
    }
}