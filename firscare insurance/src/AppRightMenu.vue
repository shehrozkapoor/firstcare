<template>
	<transition name="layout-right-panel">
	<div :class="panelClass" @click="onRightMenuClick" v-show="rightPanelMenuActive">
		<TabView>
			<TabPanel header="Status">
				<div class="status-title">
					<span>Datacenter Status</span>
					<i class="pi pi-download"></i>
				</div>
				<div>
					<ProgressBar :value="88" :showValue="false"/>
				</div>
				<div class="status-content">
					<span class="percentage-1">65</span><span class="percentage-2">/88</span> Servers Online
				</div>

				<div class="status-title">
					<span>Performance Status</span>
					<i class="pi pi-clock"></i>
				</div>
				<div>
					<ProgressBar :value="65" :showValue="false"/>
				</div>
				<div class=" status-content">
					<span class=" percentage-1">4</span>
					<span class=" percentage-2">/5</span>
					Active Pipeline
				</div>

				<div class=" status-title">
					<span>Drivers on Way</span>
					<i class=" pi pi-cloud"></i>
				</div>
				<div>
					<ProgressBar :value="35" :showValue="false"/>
				</div>
				<div class=" status-content">
					<span class=" percentage-1">12</span>
					<span class=" percentage-2">/40</span>
					Drivers
				</div>

				<div class=" status-title">
					<span>Datacenter Status</span>
					<i class=" pi pi-map-marker"></i>
				</div>
				<div>
					<ProgressBar :value="85" :showValue="false"/>
				</div>
				<div class=" status-content">
					<span class=" percentage-1">65</span><span class=" percentage-2">/88</span>
					Servers Online
				</div>
			</TabPanel>

			<TabPanel header="Messages">
				<div class="messages-title">
					<span>November 13, 2018</span>
				</div>
				<div class="messages-content grid col">
					<div class="time col-4">00:00 GMT+03:00</div>
					<div class="message-1 col-8">All systems reporting at 100%</div>
				</div>

				<div class="messages-title">
					<span>November 12, 2018</span>
				</div>
				<div class="messages-content grid col">
					<span class="time col-4">00:00 GMT+03:00</span>
					<span class="message-1 col-8">All systems reporting at 100%</span>
				</div>

				<div class="messages-title">
					<span>November 7, 2018</span>
				</div>
				<div class="messages-content grid col">
					<span class="time col-4">09:23 GMT+03:00</span>
					<span class="message-1 col-8">Everything operating normally.</span>

					<span class="time col-4">08:58 GMT+03:00</span>
					<span class="message-2 col-8">We're investigating delays inupdates to PrimeFaces.org.</span>

					<span class="time col-4">08:50 GMT+03:00</span>
					<span class="message-2 col-8">We are investigating reports of elevated error rates.</span>
				</div>
			</TabPanel>
		</TabView>
	</div>
	</transition>
</template>

<script>
	export default {
		emits: ['rightmenu-click'],
		props: {
			rightPanelMenuActive: Boolean
		},
		methods: {
			onRightMenuClick(event){
				this.$emit('rightmenu-click', event);
			}
		},
		computed: {
			panelClass(){
				return ['layout-right-panel', {
					'layout-right-panel-active': this.rightPanelMenuActive
				}]
			}
		},
		name: "AppRightMenu"
	}
</script>

<style scoped>

</style>
