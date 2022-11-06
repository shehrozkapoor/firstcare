<template>
    <form action="">
        <div class="grid col-12">
            <div class="grid col-5">
                <div class="col-3 pt-3">
                    <label for="" class="pt-2 text-base font-semibold">Start Date</label>
                </div>
                <div class="col-9">
                    <Calendar v-model="start_date" class="w-full" :required="true" />
                </div>
            </div>
            <div class="grid col-5">
                <div class="col-3 pt-3">
                    <label for="" class="pt-2 text-base font-semibold">End Date</label>
                </div>
                <div class="col-9">
                    <Calendar v-model="end_date" class="w-full" :required="true" />
                </div>
            </div>
            <div class="col-2">
                <Button label="Search" type="submit" />
            </div>
        </div>
    </form>
    <div class="toolbar">
        <Toolbar>
            <template #start>
                <Button label="Add" icon="pi pi-plus" class="mr-2 p-button-success" @click="dialog_visible=!dialog_visible" />
                <Dialog header="Add New MAR" v-model:visible="dialog_visible"
                    :breakpoints="{'960px': '75vw', '640px': '100vw'}" :style="{width: '50vw'}" position="top">
                    <div class="grid">
                        <div class="col-12">
                            <Textarea v-model="schedule_input" :autoResize="true" class="w-full"
                                placeholder="Enter Schedule.." rows="10" />
                            </div>
                        <div class="col-12">
                            <Calendar v-model="schedule_date" placeholder="select date" class="w-full" selectionMode="multiple" />
                        </div>
                        <div class="col-12">
                            <Chips v-model="schedule_time" placeholder="Enter time" class="w-full"/>
                        </div>

                    </div>
                    <template #footer>
                        <Button label="Cancel" @click="dialog_visible=!dialog_visible" />
                        <Button label="Submit" autofocus @click="getChipsData"/>
                    </template>
                </Dialog>
            </template>
            <template #end>
                <Button class="p-button-warning">Update Data</Button>
            </template>
        </Toolbar>
    </div>
    <CustomDataTableEditor />
</template>

<script>
import MarCard from '@/components/patienthealthcarerecord/customs/Cards/MarCard.vue'
import CustomStatusLabel  from '@/components/patienthealthcarerecord/customs/CustomStatusLabel.vue'
import CustomDataTableEditor from '@/components/Custom/CustomDataTableEditor.vue'
export default {
    name:"Summary",
    components:{
        MarCard,
        CustomStatusLabel,
        CustomDataTableEditor
    },
    data(){
        return{
            value:'',
            dialog_visible:false,
            schedule_date:'',
            schedule_time:'',
            schedule_input:'',
            start_date:"",
            end_date:"",
        }
    },
    methods:{
        getChipsData(){
            console.log(this.schedule_date)
            console.log(this.schedule_time)
        }
    }
}
</script>