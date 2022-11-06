<template>
	<div class="exception-body  error">
		<div class="exception-panel">
			<div class="exception-content">
				<img src="layout/images/pages/icon-error.svg" alt="roma"/>
				<h1>Error Occured</h1>
				<p>Something went wrong.</p>

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
