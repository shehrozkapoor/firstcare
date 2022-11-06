<template>
    <div class="p-fluid">
        <div class="card">
            <DataTable :value="data" editMode="cell" @cell-edit-complete="onCellEditComplete"
                class="editable-cells-table w-full" responsiveLayout="scroll" showGridlines>
                <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field">
                    <template #editor="{ data, field }">
                        <Textarea v-model="data[field]" autofocus rows="5" cols="30" />
                        </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>



<script>
export default {
    name: "CustomDataTableEditor",
    data() {
        return {
            editingRows: [],
            columns: [{
                    field: "schedule",
                    header: "Schedule"
                },
                {
                    field: "10/27/2015 0000-2359",
                    header: "10/27/2015 0000-2359"
                },
                {
                    field: "10/26/2015 0000-2359",
                    header: "10/26/2015 0000-2359"
                },
                {
                    field: "10/25/2015 0000-2359",
                    header: "10/25/2015 0000-2359"
                },
                {
                    field: "10/24/2015 0000-2359",
                    header: "10/24/2015 0000-2359"
                },
                {
                    field: "10/23/2015 0000-2359",
                    header: "10/23/2015 0000-2359"
                },
            ],
            products1: null,
            products2: null,
            products3: null,
            data: [
                {
                    "schedule": "Captopril 25mg,Oral,TAb,Tedac,Start 04/02/15 12:00:00,Stop 05/02/16 8:00:00",
                    "bg":"primary",
                    "10/27/2015 0000-2359": "@0800",
                    "10/26/2015 0000-2359": "@1200",
                    "10/25/2015 0000-2359": "@0800",
                    "10/24/2015 0000-2359": "@0800",
                    "10/23/2015 0000-2359": "@0900",
                },
                {
                    "schedule": "Captopril 25mg,Oral,TAb,Tedac,Start 04/02/15 12:00:00,Stop 05/02/16 8:00:00",
                    "10/27/2015 0000-2359": "@0800",
                    "10/26/2015 0000-2359": "@1200",
                    "10/25/2015 0000-2359": "@0800",
                    "10/24/2015 0000-2359": "@0800",
                    "10/23/2015 0000-2359": "@0900",
                },
                {
                    "schedule": "Captopril 25mg,Oral,TAb,Tedac,Start 04/02/15 12:00:00,Stop 05/02/16 8:00:00",
                    "10/27/2015 0000-2359": "@0800",
                    "10/26/2015 0000-2359": "@1200",
                    "10/25/2015 0000-2359": "@0800",
                    "10/24/2015 0000-2359": "@0800",
                    "10/23/2015 0000-2359": "@0900",
                },
                {
                    "schedule": "Captopril 25mg,Oral,TAb,Tedac,Start 04/02/15 12:00:00,Stop 05/02/16 8:00:00",
                    "10/27/2015 0000-2359": "@0800",
                    "10/26/2015 0000-2359": "@1200",
                    "10/25/2015 0000-2359": "@0800",
                    "10/24/2015 0000-2359": "@0800",
                    "10/23/2015 0000-2359": "@0900",
                },
            ]
        }
    },
    methods: {
        onCellEditComplete(event) {
            let {
                data,
                newValue,
                field
            } = event;
            console.log(newValue)
            console.log(data)
            switch (field) {

                default:
                    if (newValue.trim().length > 0)
                        data[field] = newValue;
                    else
                        event.preventDefault();
                    break;
            }
            console.log(newValue)
            console.log(data)
        },
        isPositiveInteger(val) {
            let str = String(val);
            str = str.trim();
            if (!str) {
                return false;
            }
            str = str.replace(/^0+/, "") || "0";
            var n = Math.floor(Number(str));
            return n !== Infinity && String(n) === str && n >= 0;
        },
        onRowEditSave(event) {
            let {
                newData,
                index
            } = event;

            this.products2[index] = newData;
        }
    },
}
</script>

<style lang="scss" scoped>
::v-deep(.editable-cells-table td.p-cell-editing) {
    padding-top: 0;
    padding-bottom: 0;
}
::v-deep(.primary){
    background-color: blue;
}
</style>