<template>
    <v-container>
        <v-row>
            <v-col cols="2">
                <p class="graph-text">Temperature</p>
            </v-col>
            <v-col cols="10">
                <CustomGraph />
            </v-col>
        </v-row>
    </v-container>
    <v-container>
        <v-row>
            <v-col cols="2">
                <p class="graph-text">Respiration</p>
            </v-col>
            <v-col cols="10">
                <CustomGraph />
            </v-col>
        </v-row>
    </v-container>
    <v-container>
        <v-row>
            <v-col cols="2">
                <p class="graph-text">Heart Rate</p>
            </v-col>
            <v-col cols="10">
                <CustomGraph />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import CustomGraph from '@/components/Custom/CustomGraph.vue'

export default {
    name:"Graph",
    components:{
        CustomGraph
    }
}
</script>