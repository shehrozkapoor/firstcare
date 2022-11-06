<template>
    <div>
        <h1>Basic Quill Editor</h1>
        <quill :content.sync="content"></quill>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                content: {
                    ops: [],
                },
            }
        },
    }
</script>
