<template>
    <AutoComplete v-model="selectedItem" :suggestions="filteredItems" @complete="searchItems($event)" :placeholder="placeholder" class="w-full" @item-select="getAllPatientAppointment(selectedItem)" :dropdown="true"/>
</template>

<script>
import {mapState,mapActions,mapMutations} from 'vuex'

export default {
    name:"CustomAutoComplete",
    props:['placeholder'],
	methods: {
        ...mapActions(['getSpecificPatient','getAllPatientAppointment']),
        ...mapMutations(['changeAppointmentDropdownStatus']),
		searchItems(event) {
            let query = event.query;
            let filteredItems = [];
            this.getSpecificPatient(query);
            setTimeout(()=>{
                for(let i = 0; i < this.patients.length; i++) {
                let item = this.patients[i];
                if (item.toLowerCase().indexOf(query.toLowerCase()) === 0) {
                    filteredItems.push(item);
                }
            }
            this.filteredItems = filteredItems;
            },2000)
        },
	},
    computed:{
        ...mapState(['patients'])
    },
    data() {
        return {
            filteredItems: null,
            selectedItem: null,
        }
    }
}
</script>