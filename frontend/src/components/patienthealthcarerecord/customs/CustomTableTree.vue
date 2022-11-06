<template>
    <div class="grid p-2">
        <div class="col-12">
            <div class="grid col-12">
                <div class="p-inputgroup col-6">
                    <InputText placeholder="search..." v-model="search_input"/>
                    <Button icon="pi pi-search" class="p-button-primary" />
                </div>
                <div class="col-6">
                    <Button label="Submit" class="float-right"></Button>
                </div>
            </div>
            <DataTable :value="data" v-model:selection="selectedProduct" selectionMode="single" dataKey="id">
                <Column :header="title" class="w-full">
                <template #body>
                    <Tree :value="nodes" selectionMode="single" v-model:selectionKeys="selectedKey"></Tree>
                </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>

<script>
export default {
    name: "Laboratory",
    props:['title'],
    data() {
        return {
            search_input:'',
            selectedProduct: null,
            selectedKey:null,
            nodes:[
                {
                        "key": "0",
                        "label": "Documents",
                        "data": "Documents Folder",
                        "icon": "pi pi-fw pi-inbox",
                        "children": [{
                                "key": "0-0",
                                "label": "Work",
                                "data": "Work Folder",
                                "icon": "pi pi-fw pi-cog",
                                "children": [{
                                    "key": "0-0-0",
                                    "label": "Expenses.doc",
                                    "icon": "pi pi-fw pi-file",
                                    "data": "Expenses Document"
                                }, {
                                    "key": "0-0-1",
                                    "label": "Resume.doc",
                                    "icon": "pi pi-fw pi-file",
                                    "data": "Resume Document"
                                }]
                            },
                            {
                                "key": "0-1",
                                "label": "Home",
                                "data": "Home Folder",
                                "icon": "pi pi-fw pi-home",
                                "children": [{
                                    "key": "0-1-0",
                                    "label": "Invoices.txt",
                                    "icon": "pi pi-fw pi-file",
                                    "data": "Invoices for this month"
                                }]
                            }
                        ]
                    }
            ],
            data: [{
                    "brand": "Volkswagen",
                    "year": 2012,
                    "color": "Orange",
                    "vin": "dsad231ff",
                },
                {
                    "brand": "Audi",
                    "year": 2011,
                    "color": "Black",
                    "vin": "gwregre345"
                },
                {
                    "brand": "Renault",
                    "year": 2005,
                    "color": "Gray",
                    "vin": "h354htr"
                },
                {
                    "brand": "BMW",
                    "year": 2003,
                    "color": "Blue",
                    "vin": "j6w54qgh"
                },
                {
                    "brand": "Mercedes",
                    "year": 1995,
                    "color": "Orange",
                    "vin": "hrtwy34"
                },
                {
                    "brand": "Volvo",
                    "year": 2005,
                    "color": "Black",
                    "vin": "jejtyj"
                },
                {
                    "brand": "Honda",
                    "year": 2012,
                    "color": "Yellow",
                    "vin": "g43gr"
                },
                {
                    "brand": "Jaguar",
                    "year": 2013,
                    "color": "Orange",
                    "vin": "greg34"
                },
                {
                    "brand": "Ford",
                    "year": 2000,
                    "color": "Black",
                    "vin": "h54hw5"
                },
                {
                    "brand": "Fiat",
                    "year": 2013,
                    "color": "Red",
                    "vin": "245t2s"
                }
            ]
        }
    },
}
</script>