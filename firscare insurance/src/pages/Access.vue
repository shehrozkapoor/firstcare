<template>
	<div class="exception-body accessdenied">
		<div class="exception-panel">
			<div class="exception-content">
				<img src="layout/images/pages/icon-access.svg" alt="roma"/>
				<h1>Access Denied</h1>
				<p>You do not have the necessary permissons.</p>

				<Button label="Go To Dashboard" icon="pi pi-arrow-left" @click="goDashboard" />
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		methods: {
			goDashboard(){
				this.$router.push({ path: '/' });
			}
		}
	}
</script>

<style scoped>

</style>
