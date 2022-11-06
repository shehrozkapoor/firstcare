<template>
    <router-link :to="link" class="tabs">{{name}}</router-link>
</template>

<script>
export default {
    name:"CustomTabs",
    props:['name',"link"]
}
</script>