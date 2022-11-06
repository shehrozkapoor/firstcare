<template>
<QuillEditor theme="snow" v-model:content="content" contentType="html" placeholder="Write Description Here.." ref="myQuillEditor">
    <template #toolbar >
        <Button label="Save" @click="onEditorChange" class="float-right mt-3 mr-3"></Button>
    </template>
</QuillEditor>
</template>

<script>
export default {
    name:"TestDocument",
    data(){
        return{
            content: '<h1>hello</h1><h2>hello2</h2><p><em>i am italic</em></p><p><br></p><h1><br></h1>',
        }
    },
    methods:{
        onEditorChange() {
            console.log(this.content)
      }
    }
}
</script>