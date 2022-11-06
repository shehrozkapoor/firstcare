import { createApp } from 'vue'
import App from './App.vue'
import 'vuetify/styles'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import '@/assets/style/main.css'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ColumnGroup from 'primevue/columngroup'     //optional for column grouping
import Row from 'primevue/row'
import InputText from 'primevue/inputtext'
import Chart from 'primevue/chart'
import Toolbar from 'primevue/toolbar'
import Button from 'primevue/button'
import SplitButton from 'primevue/splitbutton'
import Dialog from 'primevue/dialog'
import PrimeVue from 'primevue/config'
import Textarea from 'primevue/textarea'
import Checkbox from 'primevue/checkbox'
import TabMenu from 'primevue/tabmenu'
import Divider from 'primevue/divider'
import FileUpload from 'primevue/fileupload'
import Calendar from 'primevue/calendar'
import Datepicker from 'vue3-datepicker'
import AutoComplete from 'primevue/autocomplete'
import TieredMenu from 'primevue/tieredmenu'
import Tree from 'primevue/tree'
import Card from 'primevue/card'
import Chips from 'primevue/chips'
import Dropdown from 'primevue/dropdown'
import Toast from 'primevue/toast'
import ToastService from 'primevue/toastservice'
import Message from 'primevue/message'

import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"

import "primeflex/primeflex.css"


loadFonts()

const app = createApp(App)
app.use(router)
app.use(store)
app.use(vuetify)
app.use(PrimeVue)
app.use(ToastService)
app.component("DataTable",DataTable)
app.component("Column",Column)
app.component("ColumnGroup",ColumnGroup)
app.component("Row",Row)
app.component("InputText",InputText)
app.component("Chart",Chart)
app.component("Toolbar",Toolbar)
app.component("Button",Button)
app.component("SplitButton",SplitButton)
app.component("Dialog",Dialog)
app.component("Textarea",Textarea)
app.component("Checkbox",Checkbox)
app.component("TabMenu",TabMenu)
app.component("p-Divider",Divider)
app.component("FileUpload",FileUpload)
app.component("Calendar",Calendar)
app.component("Datepicker",Datepicker)
app.component("AutoComplete",AutoComplete)
app.component("TieredMenu",TieredMenu)
app.component('QuillEditor', QuillEditor)
app.component('Tree', Tree)
app.component('Card', Card)
app.component('Chips', Chips)
app.component('Dropdown', Dropdown)
app.component('Toast', Toast)
app.component('Message', Message)



app.mount('#app')


