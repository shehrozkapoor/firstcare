# vue-quill
[![npm version](https://badge.fury.io/js/vue-quill.svg)](https://badge.fury.io/js/vue-quill)

A vue component wrapping the quill editor

## Installation
```
npm install --save vue-quill
-or-
yarn add vue-quill
```

You will also need to include the following css file in your project
```html
<link href="https://cdn.quilljs.com/1.2.6/quill.snow.css" rel="stylesheet">
```

## Vue 1
For Vue 1 components use v0.1.5 or earlier

## Usage
Install the vue plugin
```js
import Vue from 'vue'
import VueQuill from 'vue-quill'

Vue.use(VueQuill)
```
### Component
```html
<quill v-model="content"></quill>
```
You may want to initialize the synced variable as a valid delta object too

```js
data() {
    return {
        content: {
            ops: [],
        },
    }
}
```

### Configuration
```html
<quill v-model="content" :config="config"></quill>
```
You can also provide a config object as described in http://quilljs.com/docs/configuration/

```js
data() {
    return {
        content: {
            ops: [],
        },
        config: {
            readOnly: true,
            placeholder: 'Compose an epic...',
        },
    }
}
```

## Options
By default, the component outputs the content as a delta object, you can pass in a prop to return raw html
```html
<quill v-model="content" output="html"></quill>
```

## Custom Formats
To add custom formats to the editor, you can pass an array of formats as a prop. The array should be in the following format
```js
formats: [
    {
        name: 'custom',
        options: {
            attribute: 'custom',
        },
    },
],
```

## Custom Keybindings
You can add custom keybindings by passing through an array in the props, the array should be in the following format
```js
keyBindings: [
    {
        key: 's',
        method: function(range) {
            this.$dispatch('save', this.editor, range)
            return false        
        },
    },
]
```

## Events
This quill component emits events when the text or selection changes on the quill editor
```html
<quill v-model="content" @selection-change="selectionChange"></quill>

<script>
methods: {
    selectionChange(editor, range) {
        if (range) {
            if (range.start !== range.end) {
                this.selectedText = editor.getText(range.start, range.end)
                editor.formatText(range, 'custom', 'hello world')
            }
        }
    },
},
```
