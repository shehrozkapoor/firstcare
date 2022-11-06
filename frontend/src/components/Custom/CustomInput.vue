<template>
    <input :type="type??'text'" class="custom-input" :value="value??''" :disabled="disabled??false" :placeholder="placeholder">
</template>

<script>
export default{
    name:"CustomInput",
    props:['value','disabled','placeholder','type']
}

</script>
