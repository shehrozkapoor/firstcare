<template>
    <Toolbar class="sticky top-0 font-bold text-white p-4 w-full">
        <template #start>
            <Button label="New" icon="pi pi-plus" class="mr-2" @click="model_display=!model_display"/>
            <Button label="Upload" icon="pi pi-upload" class="p-button-success mr-2"/>
            <SplitButton label="Save" icon="pi pi-check" :model="items" class="p-button-warning"></SplitButton>
        </template>

        <template #end>
            <Button icon="pi pi-search" class="mr-2" />
            <Button icon="pi pi-calendar" class="p-button-success mr-2" />
            <Button icon="pi pi-times" class="p-button-danger" />
        </template>
    </Toolbar>
    <v-container>
        <div class="mt-9">
            <router-link v-for="(item,index) in patient_list" :key="index" :to="item.link" class="tabs">{{item.name}}
            </router-link>
        </div>
        <div class="mt-5">
            <CustomDataTable :table_data="table_data" :table_columns="columns" :title='setTitle' :multipleSelect="false"/>
        </div>
    </v-container>
</template>

<script>
import CustomHeader from '@/components/Custom/CustomHeader.vue'
import CustomTabs from '@/components/Custom/CustomTabs.vue'
import CustomDataTable from '@/components/Custom/CustomDataTable.vue'
const patient_list_link = "/patient-health-care/patient-list/"


export default {
    name: "PatientList",
    components: {
        CustomHeader,
        CustomTabs,
        CustomDataTable,
    },
    created(){
        this.title = 'All Patients in ' + this.$route.params.id
    },
    computed:{
        setTitle(){
            return 'All Patients in ' + this.$route.params.id
        }
    },
    data() {
        return {
            model_display:false,
            title:null,
            patient_list: [{
                    name: 'list-1',
                    link: patient_list_link + 'list-1'
                },
                {
                    name: 'list-2',
                    link: patient_list_link + 'list-2'
                },
                {
                    name: 'list-3',
                    link: patient_list_link + 'list-3'
                },
            ],
            columns: [{
                    'field': 'id',
                    'header': 'ID'
                },
                {
                    'field': 'code',
                    'header': 'Code'
                },
                {
                    'field': 'name',
                    'header': 'Name'
                },
                {
                    'field': 'description',
                    'header': 'Description'
                },
            ],
            table_data: [{
                    "id": "1000",
                    "code": "f230fh0g3",
                    "name": "Bamboo Watch",
                    "description": "Product Description",
                    "image": "bamboo-watch.jpg",
                    "price": 65,
                    "category": "Accessories",
                    "quantity": 24,
                    "inventoryStatus": "INSTOCK",
                    "rating": 5
                },
                {
                    "id": "1001",
                    "code": "nvklal433",
                    "name": "Black Watch",
                    "description": "Product Description",
                    "image": "black-watch.jpg",
                    "price": 72,
                    "category": "Accessories",
                    "quantity": 61,
                    "inventoryStatus": "INSTOCK",
                    "rating": 4
                },
                {
                    "id": "1002",
                    "code": "zz21cz3c1",
                    "name": "Blue Band",
                    "description": "Product Description",
                    "image": "blue-band.jpg",
                    "price": 79,
                    "category": "Fitness",
                    "quantity": 2,
                    "inventoryStatus": "LOWSTOCK",
                    "rating": 3
                },
                {
                    "id": "1003",
                    "code": "244wgerg2",
                    "name": "Blue T-Shirt",
                    "description": "Product Description",
                    "image": "blue-t-shirt.jpg",
                    "price": 29,
                    "category": "Clothing",
                    "quantity": 25,
                    "inventoryStatus": "INSTOCK",
                    "rating": 5
                },
                {
                    "id": "1004",
                    "code": "h456wer53",
                    "name": "Bracelet",
                    "description": "Product Description",
                    "image": "bracelet.jpg",
                    "price": 15,
                    "category": "Accessories",
                    "quantity": 73,
                    "inventoryStatus": "INSTOCK",
                    "rating": 4
                },
                {
                    "id": "1005",
                    "code": "av2231fwg",
                    "name": "Brown Purse",
                    "description": "Product Description",
                    "image": "brown-purse.jpg",
                    "price": 120,
                    "category": "Accessories",
                    "quantity": 0,
                    "inventoryStatus": "OUTOFSTOCK",
                    "rating": 4
                },
                {
                    "id": "1006",
                    "code": "bib36pfvm",
                    "name": "Chakra Bracelet",
                    "description": "Product Description",
                    "image": "chakra-bracelet.jpg",
                    "price": 32,
                    "category": "Accessories",
                    "quantity": 5,
                    "inventoryStatus": "LOWSTOCK",
                    "rating": 3
                },
                {
                    "id": "1007",
                    "code": "mbvjkgip5",
                    "name": "Galaxy Earrings",
                    "description": "Product Description",
                    "image": "galaxy-earrings.jpg",
                    "price": 34,
                    "category": "Accessories",
                    "quantity": 23,
                    "inventoryStatus": "INSTOCK",
                    "rating": 5
                },
                {
                    "id": "1008",
                    "code": "vbb124btr",
                    "name": "Game Controller",
                    "description": "Product Description",
                    "image": "game-controller.jpg",
                    "price": 99,
                    "category": "Electronics",
                    "quantity": 2,
                    "inventoryStatus": "LOWSTOCK",
                    "rating": 4
                },
                {
                    "id": "1009",
                    "code": "cm230f032",
                    "name": "Gaming Set",
                    "description": "Product Description",
                    "image": "gaming-set.jpg",
                    "price": 299,
                    "category": "Electronics",
                    "quantity": 63,
                    "inventoryStatus": "INSTOCK",
                    "rating": 3
                },
                {
                    "id": "1010",
                    "code": "cm230f032",
                    "name": "Gaming Set",
                    "description": "Product Description",
                    "image": "gaming-set.jpg",
                    "price": 299,
                    "category": "Electronics",
                    "quantity": 63,
                    "inventoryStatus": "INSTOCK",
                    "rating": 3
                },
                {
                    "id": "1011",
                    "code": "cm230f032",
                    "name": "Gaming Set",
                    "description": "Product Description",
                    "image": "gaming-set.jpg",
                    "price": 299,
                    "category": "Electronics",
                    "quantity": 63,
                    "inventoryStatus": "INSTOCK",
                    "rating": 3
                },
                {
                    "id": "1012",
                    "code": "cm230f032",
                    "name": "Gaming Set",
                    "description": "Product Description",
                    "image": "gaming-set.jpg",
                    "price": 299,
                    "category": "Electronics",
                    "quantity": 63,
                    "inventoryStatus": "INSTOCK",
                    "rating": 3
                }
            ]
        }
    }
}
</script>


<style>
.v-main{
    margin-top: 0px!important;
}
</style>