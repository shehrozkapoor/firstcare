import render from 'quill-render'
import Quill from './src/Quill.vue'

export default {
    install: function (Vue, options) {
        Vue.component('quill', Quill);

        render.format.inline.underline = function($) {
            return $('<u>');
        };

        Vue.filter('quill', function(value) {
            return render(value.ops);
        });

        Vue.filter('quill-preview', function(value, limit) {
            const text = value.ops.map(function(op) {
                return op.insert
            }).join(' ')

            if (typeof limit !== 'undefined' && text.length > limit) {
                return text.substring(0, parseInt(limit, 10)) + '...'
            }

            return text
        });
    },
}
