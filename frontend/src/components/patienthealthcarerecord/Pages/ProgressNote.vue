<template>
    <div>
        <Handsontable :data="handsonData1.data" :colHeaders="handsonColData" :rowHeaders="handsonData1.handsonRowData"
            :dropdownMenu="false" :filter="true" :colWidths=200 :rowHeaderWidth="auto" />
    </div>
    <div class="mt-4 progress-note-info">
        <v-layout>
            <v-row>
                <v-col>
                    <v-label>Admission No</v-label>
                    <CustomInput disabled="true" value="2133132" />
                </v-col>
                <v-col>
                    <v-label>Patient</v-label>
                    <CustomInput disabled="true" value="sabdkja" />
                </v-col>
                <v-col cols="4">
                    <v-label>Condition</v-label>
                    <CustomSelect :items="items" />
                </v-col>
                <v-col cols="4">
                    <v-label>OB. Type</v-label>
                    <CustomSelect :items="items" />
                </v-col>
                <v-col cols="4">
                    <v-label>Reason</v-label>
                    <CustomInput placeholder="Reason.."/>
                </v-col>
                <v-col cols="4">
                    <v-label cols="1">Old Notes</v-label>
                    <v-textarea cols="3" background-color="white" color="transparent" label="Notes"></v-textarea>
                </v-col>
                <v-col cols="12">
                    <v-label>Notes</v-label>
                    <v-textarea background-color="white" color="transparent" label="Notes"></v-textarea>
                </v-col>
            </v-row>
        </v-layout>
    </div>
</template>


<script>
import Handsontable from '@/components/patienthealthcarerecord/HandsonTable.vue'
import CustomHeader from '@/components/Custom/CustomHeader.vue'
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
export default {
    name: "ProgressNote",
    components: {
        Handsontable,
        CustomHeader,
        CustomInput,
        CustomSelect
    },
    data() {
        return {
            showHeader: true,
            items: ['stabe', 'unstable'],
            handsonColData: ['Assessment Date', 'Observation Type', 'Created By', 'test', 'test'],
            handsonData1: {
                handsonRowData: true,
                data: [
                    ['', '', '', '', ''],
                    ['', '', '', '', ''],
                ]
            },
        }
    }
}
</script>
