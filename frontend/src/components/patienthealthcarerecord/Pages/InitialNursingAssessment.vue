<template>
    <v-container>
        <v-row class="m-0">
            <v-col cols="12">
                <label for="">Admission Details</label>
                <v-divider></v-divider>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <label for="">Category</label>
                <CustomInput value="mdh default" placeholder="category" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="1">
                <label for="">Company</label>
            </v-col>
            <v-col cols="4">
                <CustomInput value="mdh default Company" placeholder="company" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Nationality</label>
            </v-col>
            <v-col cols="4">
                <CustomInput placeholder="nationality" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="1">
                <label for="">Mobile No</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="mobile No" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Floor</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Wt/Ht/Age</label>
            </v-col>
            <v-col cols="1">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="1">
                <label for="">Room</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Bed</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Gender</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Blood Group</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="1">
                <label for="">Specialty</label>
            </v-col>
            <v-col cols="4">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Doctor</label>
            </v-col>
            <v-col cols="4">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="2">
                <label for="">Contact person In Case Of Emergency.</label>
            </v-col>
            <v-col cols="4">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
            <v-col cols="1">
                <label for="">Diagnosis</label>
            </v-col>
            <v-col cols="4">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" />
            </v-col>
        </v-row>
        <v-row class="m-0">
            <v-col cols="12">
                <label for="">Arrival Details</label>
                <v-divider></v-divider>
            </v-col>
        </v-row>
        <v-row class="m-0">
            <v-col cols="1">
                <label for="">Arrival Time</label>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="Floor" class="auto-input-select-measurement" type="datetime-local"/>
            </v-col>
            <v-col cols="1">
                <label for="">Mood of Arrival</label>
            </v-col>
            <v-col cols="2">
                <v-radio-group>
                    <v-radio label="WheelChair" value="WheelChair"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="2">
                <v-radio-group>
                    <v-radio label="stretcher" value="stretcher"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="2">
                <v-radio-group>
                    <v-radio label="Other" value="Other"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="2">
                <CustomInput placeholder="mood of arrival" class="auto-input-select-measurement" type="text"/>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="2">
                <label for="">Transport with</label>
            </v-col>
            <v-col cols="1">
                <v-checkbox-group>
                    <v-checkbox label="Oxygen" value="Oxygen"></v-checkbox>
                </v-checkbox-group>
            </v-col>
            <v-col cols="1">
                <v-checkbox-group>
                    <v-checkbox label="Monitor" value="Monitor"></v-checkbox>
                </v-checkbox-group>
            </v-col>
            <v-col cols="1">
                <v-checkbox-group>
                    <v-checkbox label="IV" value="IV"></v-checkbox>
                </v-checkbox-group>
            </v-col>
            <v-col cols="1">
                <v-checkbox-group>
                    <v-checkbox label="Other" value="Other"></v-checkbox>
                </v-checkbox-group>
            </v-col>
            <v-col cols="5">
                <CustomInput placeholder="transport with" class="auto-input-select-measurement" type="text"/>
            </v-col>
        </v-row>

        <v-row class="m-0">
            <v-col cols="2">
                <label for="">Admitted Form</label>
            </v-col>
            <v-col cols="1">
                <v-radio-group>
                    <v-radio label="Er" value="Er"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="1">
                <v-radio-group>
                    <v-radio label="Clinic" value="Clinic"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="1">
                <v-radio-group>
                    <v-radio label="Other" value="Other"></v-radio>
                </v-radio-group>
            </v-col>
            <v-col cols="5">
                <CustomInput placeholder="Admitted form" class="auto-input-select-measurement" type="text"/>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="3">
                <label for="">Introduction to clinician</label>
            </v-col>
            <v-col cols="3">
                <CustomSelect :items="items" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <CustomDataTable :table_columns="table_columns" :table_data="table_data" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CustomInput from '@/components/Custom/CustomInput.vue'
import CustomSelect from '@/components/Custom/CustomSelect.vue'
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'

export default {
    name:"InitialNursingAssessment",
    components:{
        CustomInput,
        CustomSelect,
        CustomDataTable,
    },
    data(){
        return{
            items:['1',2,4],
            table_columns:[
                {
                    'field':'id',
                    'header':'ID'
                },
                {
                    'field':'description',
                    'header':'Description'
                },
            ],
            table_data:[
                {
                    id:"1",
                    description:"testing",
                }
            ]
        }
    }
}
</script>