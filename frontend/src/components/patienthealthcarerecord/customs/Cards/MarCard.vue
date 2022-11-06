<template>
    <Card :class="color">
        <template #title>
            {{title}}
        </template>
        <template #content>
            {{content}}
        </template>
    </Card>
</template>

<script>
export default {
    name:"MarCard",
    props:['title','content','color']
}
</script>