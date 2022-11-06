<template>
    <div class="h-screen w-full shadow-6 m-0 p-0">
        <Tree :value="nodes" selectionMode="single" v-model:selectionKeys="selectedNodeKey" @node-selection="nodeSelection" class="w-full h-screen"></Tree>
    </div>
</template>

<script>
export default {
    name:"CustomSideBarFolder",
    components:{
    },
    props:['selectedNodeKey','nodeSelection'],
    data(){
        return{
            nodes:[
        {
            "key": "0",
            "label": "Management",
            "data": "Management Folder",
            "icon": "pi pi-fw pi-folder",
            "children": [
                {
                "key": "0-0",
                "label": "26-03-2022 2:59 PM",
                "data": "Work Folder",
                "icon": "pi pi-fw pi-file",
            },
            ]
        },
        {
            "key": "1",
            "label": "Imaging",
            "data": "Imaging Folder",
            "icon": "pi pi-fw pi-folder",
            "children": [
                {
                "key": "1-0",
                "label": "26-03-2022 2:59 PM",
                "data": "Work Folder",
                "icon": "pi pi-fw pi-file",
            },
            ]
        }

    ]
        }
    }
}
</script>