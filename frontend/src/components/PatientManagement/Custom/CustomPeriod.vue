<template>
    <div class="col-2 pt-3 pl-3 font-bold">
        <label for="status">Period</label>
    </div>
    <div class="col-5">
        <Calendar class="w-full" v-model="start_date" placeholder="start date" />
    </div>
    <div class="col-5">
        <Calendar class="w-full" v-model="end_date" placeholder="end date" />
    </div>
</template>

<script>
import moment from 'moment'

export default {
    name:"CustomPeriod",
    data(){
        return{
            start_date: moment().format('MM-DD-YYYY'),
            end_date:'',
        }
    }
}
</script>