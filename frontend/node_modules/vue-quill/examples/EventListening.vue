<template>
    <div>
        <h1>Chrono date parsing</h1>
        <p>
            This component listens for text changes in quill and uses the
            <a href="https://github.com/wanasit/chrono">Chrono</a>
            library for natural language date parsing.
        </p>
        <quill :content.sync="content" :formats="formats"></quill>
        <div v-for="date in dates">{{ date }}</div>
    </div>
</template>

<script>
    import chrono from 'chrono-node'

    export default {
        data() {
            return {
                dates: [],

                content: {
                    ops: [],
                },

                formats: [
                    {
                        name: 'time',
                        options: {
                            attribute: 'time',
                        },
                    },
                ]
            }
        },
        events: {
            'text-change'(editor, delta, source) {
                if (source === 'user') {
                    const dates = chrono.parse(editor.getText())

                    this.dates = dates.map((date) => {
                        editor.formatText(date.index, date.index + date.text.length, 'time', date.start.date())
                        return date.start.date()
                    })
                }
            },
        },
    }
</script>
