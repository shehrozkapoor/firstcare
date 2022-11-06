<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <label for="">Date Time</label>
                <CustomInput type="datetime-local" />
                <v-btn class="ml-2">Show All</v-btn>
            </v-col>
            <v-col cols="12">
                <v-table fixed-header>
                    <thead>
                        <tr>
                            <th class="text-left" width="300">
                                Categories
                            </th>
                            <th class="text-left" width="600">
                                Criteria
                            </th>
                            <th class="text-left">
                            </th>
                            <th class="text-left">
                                Score
                            </th>
                            <th class="text-left">
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Aut temporibus voluptatem.
                                <br>
                                Facilis voluptas rerum sunt
                                <br>
                                voluptatem perferendis autem
                                <br>
                                voluptates.</td>
                            <td>test 2</td>
                            <td>test 2</td>
                            <td>test 2</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Aut temporibus voluptatem.
                                <br>
                                Facilis voluptas rerum sunt
                                <br>
                                voluptatem perferendis autem
                                <br>
                                voluptates.</td>
                            <td>test 2</td>
                            <td>test 1</td>
                            <td>test 2</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>Aut temporibus voluptatem.
                                <br>
                                Facilis voluptas rerum sunt
                                <br>
                                voluptatem perferendis autem
                                <br>
                                voluptates.</td>
                            <td>test 2</td>
                            <td>test 1</td>
                            <td>test 2</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>Aut temporibus voluptatem.
                                <br>
                                Facilis voluptas rerum sunt
                                <br>
                                voluptatem perferendis autem
                                <br>
                                voluptates.</td>
                            <td>test 2</td>
                            <td>test 1</td>
                            <td>test 2</td>
                        </tr>
                    </tbody>
                </v-table>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import CustomInput from '@/components/Custom/CustomInput.vue'
export default {
    name:"CriticalCarePainObservationTool",
    components:{
        CustomInput,
    }
}
</script>