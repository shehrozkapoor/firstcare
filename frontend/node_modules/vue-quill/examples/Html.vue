<template>
    <div>
        <h1>Html Quill Editor</h1>
        <p>This quill element will output the contents as raw HTML</p>
        <quill :content.sync="content" ouput="html"></quill>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                content: '',
            }
        },
    }
</script>
