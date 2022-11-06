<style>
    .ql-active {
        background-color: #ccc;
    }
</style>

<template>
    <div>
        <h1>Custom Formats and Toolbars</h1>
        <p>
            This component adds a
            <a href="http://quilljs.com/docs/api/#quillprototypeaddformat">custom format</a>
            to the quill editor and overloads the default toolbar
        </p>
        <quill :content.sync="content" :formats="formats">
            <div slot="toolbar">
                <div class="ql-format-group">
                    <a class="ql-format-button ql-bold"></a>
                    <span class="ql-format-separator"></span>
                    <a class="ql-format-button ql-underline"></a>
                    <span class="ql-format-separator"></span>
                    <a class="ql-format-button ql-italic"></a>
                    <span class="ql-format-separator"></span>
                    <a class="ql-custom">Custom</a>
                </div>
            </div>
        </quill>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                content: {
                    ops: [],
                },
                formats: {
                    {
                        name: 'custom',
                        options: {
                            attribute: 'custom',
                        },
                    },
                },
            }
        },
    }
</script>
