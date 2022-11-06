<template>
    <select class="custom-select">
        <option :value="index" v-for="(item,index) in items" :key="index">{{item}}</option>
    </select>
</template>


<script>
export default {
    name:"CustomSelect",
    props:['items']
}
</script>