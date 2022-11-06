<template>
	<div class="login-body">
		<div class="card login-panel p-fluid">
			<div class="login-panel-content">
				<div class="grid">
					<div class="col-12 sm:col-6 md:col-6 logo-container">
						<img src="layout/images/logo-roma.svg" alt="roma"/>
						<span class="guest-sign-in">Welcome, please use the form to sign-in FirstCare</span>
					</div>
					<div class="col-12 username-container">
						<label>Username</label>
						<div class="login-input">
							<InputText id="input" type="text" />
						</div>
					</div>
					<div class="col-12 password-container">
						<label>Password</label>
						<div class="login-input">
							<InputText type="password" />
						</div>
					</div>
					<div class="col-6 rememberme-container">
						<Checkbox v-model="checked" :binary="true"/>
						<label> Remember me</label>
					</div>

					<div class="col-6 mt-1 forgetpassword-container">
						<a href="#" class="forget-password">Forget Password</a>
					</div>

					<div class="col-12 sm:col-6">
						<Button label="Sign In" icon="pi pi-check" @click="goDashboard"/>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				checked: false
			}
		},
		methods: {
			goDashboard(){
				this.$router.push({ path: '/' });
			}
		}
	}
</script>

<style scoped>

</style>
