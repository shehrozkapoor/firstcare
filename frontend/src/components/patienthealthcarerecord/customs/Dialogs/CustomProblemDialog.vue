<template>
    <Dialog v-model:visible="display" position="top">
        <template #header>
            <h3>{{header}}</h3>
        </template>
        <CustomDataTable :multipleSelect="false" :table_columns="table_columns" :table_data="table_data" title="Problem"
            class="border-1 border-solid border-indigo-100 p-3" />

        <div class="mt-3 border-1 border-solid border-indigo-100 p-3">
            <div class="formgrid grid">
                <div class="col-8 grid">
                    <div class="col-4">
                        <div class="field col">
                            <label for="">Problem</label>
                            <CustomInput placeholder="Problem" class="w-full inline" />
                        </div>
                    </div>
                    <div class="col-2 mt-5">
                        <CustomSearchDialog header="search problem" :display="search_display"/>
                        <Button icon="pi pi-search" :loading="isLoading" @click="search_display=!search_display"/>
                    </div>
                    <div class="col-6">
                        <div class="field col">
                            <label for="responsible-provider">Responsible Provider</label>
                            <CustomInput placeholder="Responsible Provider" class="w-full" />
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="field col">
                            <label for="responsible-provider">Display As</label>
                            <CustomInput placeholder="Display As" class="w-full" />
                        </div>
                    </div>
                    <div class="field col-4">
                        <div class="col">
                            <label for="responsible-provider">At:Age</label>
                            <CustomInput placeholder="At:Age" class="w-full" />
                            <CustomSelect class="w-full" :items="items" />
                        </div>
                    </div>
                    <div class="field col-4">
                        <label for="responsible-provider">onSet:<span class="text-primary">Date</span></label>
                        <CustomInput class="w-full" type="date" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Confirmation</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Classification</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Status</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Cancel Reason</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Ranking</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Ranking</label>
                        <CustomSelect class="w-full" :items="items" />
                    </div>
                    <div class="field col-3">
                        <div class="col">
                            <label for="responsible-provider">Resolved At:Age</label>
                            <CustomInput placeholder="At:Age" class="w-full" />
                            <CustomSelect class="w-full" :items="items" />
                        </div>
                    </div>
                    <div class="field col-3">
                        <label for="responsible-provider">Resolved Date</label>
                        <CustomInput class="w-full" type="date" />
                    </div>
                </div>
                <div class="field col-4">
                    <label for="comments">Comments</label>
                    <Textarea v-model="value" rows="5" cols="30" class="w-full" />
                    </div>
            </div>
        </div>

        <template #footer>
            <Button label="Ok" icon="pi pi-check" autofocus />
            <Button label="Ok Add New" icon="pi pi-check" autofocus />
            <Button label="Add Problem And Diagnosis" icon="pi pi-check" autofocus />
            <Button label="cancel" icon="pi pi-times" class="p-button-text p-button-danger" @click="HideDialog" />
        </template>
    </Dialog>
</template>

<script>
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomSearchDialog from '@/components/patienthealthcarerecord/customs/Dialogs/CustomSearchDialog.vue'
export default {
    name: "CustomProblemDialog",
    components: {
        CustomDataTable,
        CustomInput,
        CustomSelect,
        CustomSearchDialog
    },
    props: ['display', "header"],
    computed: {
        HideDialog() {
            return !this.display
        }
    },
    data() {
        return {
            items: [1, 2, 3],
            search_display:false,
            table_data: [{
                "name-of-problem": "Acute UTI",
                "on-set-date": "03/24/2022",
                "life-cycle-st": "Resolved",
                "responsible-provider": "Test Provider",
            }],
            table_columns: [{
                    'field': "name-of-problem",
                    "header": "Name Of Problem"
                },
                {
                    'field': "on-set-date",
                    "header": "Onset Date"
                },
                {
                    'field': "life-cycle-st",
                    "header": "Life Cycle St"
                },
                {
                    'field': "responsible-provider",
                    "header": "Responsible Provider"
                },
            ],
        }
    }
}
</script>