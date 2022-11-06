<template>
    <div class="grid">
        <div class="col-3">
            <SideBarWithSideChecks :routes="routes" :showTitle="false"/>
        </div>
        <div class="col-9 w-full">
            <router-view></router-view>
        </div>
    </div>
</template>


<script>
import SideBarWithSideChecks from '@/components/Custom/SideBarWithSideChecks.vue'
export default {
    name: "Order",
    data() {
        return {
            routes: [{
                    'title': 'Summary',
                    'name': 'order-summary'
                },
                {
                    'title': 'Laboratory',
                    'name': 'order-laboratory'
                },
                {
                    'title': 'Radiology',
                    'name': 'order-radiology'
                },
                {
                    'title': 'Medication',
                    'name': 'order-medication'
                }
            ]
        }
    },
    components: {
        SideBarWithSideChecks
    }
}
</script>