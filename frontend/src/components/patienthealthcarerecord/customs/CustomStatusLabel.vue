<template>
    <div class="">
        <span :class="color" class="border-1 border-600 w-2 p-2 mr-2 ">{{title}}</span>
        <label for="">{{label}}</label>
    </div>
</template>

<script>
export default {
    name:"CustomStatusLabel",
    props:['title','label','color']
}
</script>