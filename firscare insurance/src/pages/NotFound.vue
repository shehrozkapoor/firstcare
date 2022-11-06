<template>
	<div class="exception-body notfound">
		<div class="exception-panel">
			<div class="exception-content">
				<img src="layout/images/pages/icon-404.svg" alt="roma"/>
				<h1>Page Not Found</h1>
				<p>Requested resource is not available.</p>

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
