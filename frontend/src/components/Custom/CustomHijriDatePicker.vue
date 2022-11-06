<template>
  <div>
    <date-picker v-model="date" :locale="'ar-sa'" :calendar="'hijri'"/>
  </div>
</template>

<script>
import VueDatetimeJs from 'vue-datetime-js'
export default {
  data(){
    return {
      date: ''
    }
  },
  components: {
    datePicker: VueDatetimeJs
  }
}
</script>