<template>
  <hot-table :data="data" :rowHeaders="rowHeaders" :settings="hotSettings" :colHeaders="colHeaders"></hot-table>
</template>

<script>
  import { HotTable } from '@handsontable/vue3';
  import { registerAllModules } from 'handsontable/registry';

  // register Handsontable's modules
  registerAllModules();

  export default{
    name:"Handsontable",
    props:['colHeaders','rowHeaders','data','dropdownMenu','filter','rowHeaderWidth','colWidths'],
    data() {
      return {
        hotSettings: {
        height: 'auto',
        licenseKey: 'non-commercial-and-evaluation',
        dropdownMenu: this.dropdownMenu??false,
        filters: this.filter??false,
        rowHeaderWidth: this.rowHeaderWidth??'auto',
        colWidths:this.colWidths??'auto',
      },
        data: this.data

      };
    },
    components: {
      HotTable,
    }
  }
</script>
