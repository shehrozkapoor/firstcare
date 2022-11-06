<template>
    <v-navigation-drawer permanent class="side-bar">
      <v-container class="main-container">
      <ul>
        <li class="bg-blue-400 border-primary text-xl font-bold text-white" v-show="showTitle">
          <p class="">{{title}}</p>
        </li>
        <li v-for="(route,key) in routes" :key="key">
            <Checkbox v-model="sideChecks" @change="changeSideBar" :value="route.title" class="mr-2"/>
            <router-link :to="{name:route.name}" class="sidebar-link pt-2">{{route.title}}</router-link>
        </li>
      </ul>
      </v-container>
    </v-navigation-drawer>
</template>

<script>
export default {
    name:"SideBarWithSideChecks",
    props:['routes','title','showTitle'],
    data(){
      return{
        sideChecks: []
      }
    },
    methods:{
      changeSideBar(){
        console.log(this.sideChecks)
      }
    }
}
</script>
