import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class LocationServices{
    async getAllLocations() {
        var resp = await axios({
          url:constants.department,
          headers:{
            "Authorization": constants.token
          }
          });
          return resp.data;
      }

}