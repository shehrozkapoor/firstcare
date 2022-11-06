# firstcare-frontend
## Project setup
```
npm install
```
### Compiles and hot-reloads for development
```
npm run serve
```
### Compiles and minifies for production
```
npm run build
```

<!-- all the codes are in src folder -->
### Technologies or libraries used....
1. vue3
2. vuex (state management)
3. vuetify
4. primeVue
5. momentJs (datetime)
6. Handsontable **(for datatable and also used the primevue datatables)**

### project structure
###### path

- src
    - components
        - Custom (all the components that are reuseable in all other components)
        - patienthealthcarerecord (all the components that are for the patient healthcare record)
            - customs (all the custom components that are only used in patient healthcare record)
            - Pages (all the pages of patient healthcare record)
            - SubPages (sub-pages that are used in patient healthcare record)
        - PatientManagement (all the components that are used for the patient management)
            - Custom (all the custom components that are only used in patient management)
            - Pages (all the pages of patient management)

**__description__**
__if you can see the above project structure it a hierarchical structure or a tree structure.__


### plugins
###### Vuetify3 is used as a plugin and the all the configuration are present in plugin folder

**Note: __ Vuetify3 is on the beta testing and it is not fully compatible with vue3 so that why we shifted in the primeVue__**

###### primeVue is used as a plugin and most of the components are using primeVue

all the configurations are present in main.ts file

**PrimeVue(are the builtin components) has another plugin PrimeFlex(which is used for the alignments and styling of the components)**
so don't mix both. both have different libraries and different configurations


## Deployment
[... see the django project all the information is present in that readme file.](https://github.com/aloalqma/firstcare.git).

## How to Deploy a new build
```
1. npm run build
2. git push
3. login to the server
4. git pull
5. npm run build **(Note:this should be in the production server not local)**
6. sudo systemctl restart nginx
```