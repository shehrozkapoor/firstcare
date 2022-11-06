import { Plugin } from 'vue';
import Tree from "./tree-component.vue";
declare type InstallableComponent = typeof Tree & {
    install: Exclude<Plugin['install'], undefined>;
};
declare const _default: InstallableComponent;
export default _default;
