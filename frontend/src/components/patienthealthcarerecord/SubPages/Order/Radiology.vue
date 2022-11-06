<template>
    <div class="grid p-2">
        <CustomTableTree  class="w-full" title="Radiology"/>
    </div>
</template>

<script>
import CustomTableTree from '@/components/patienthealthcarerecord/customs/CustomTableTree.vue'
export default {
    name: "Radiology",
    components:{
        CustomTableTree
    }
}
</script>