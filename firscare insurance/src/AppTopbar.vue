<template>
	<div class="layout-topbar">
			<button class="p-link layout-right-panel-button layout-topbar-icon" id="menu-button"
					@click="onRightMenuButtonClick">
				<i class="pi pi-ellipsis-v"></i>
			</button>

			<button class="p-link layout-menu-button layout-topbar-icon" @click="onMenuButtonClick">
				<i class="pi pi-bars"></i>
			</button>

			<router-link to="/" class="p-link layout-topbar-logo">
				<img id="topbar-logo" src="layout/images/logo-roma-white.svg" alt="roma-vue"/>
			</router-link>

			<span class="layout-topbar-search">
                <i class="pi pi-search"></i>
                <input type="text" placeholder="Enter your search term"/>
            </span>

			<ul class="topbar-menu">
				<li :class="['user-profile', {'active-topmenuitem fadeInDown': activeTopbarItem === 'profile'}]">
					<button class="p-link" v-if="!this.inlineUser"
							@click="$emit('topbar-item-click',{originalEvent:$event,item:'profile'})">
						<img src="layout/images/avatar.png" alt="roma-layout"/>
						<div class="layout-profile-userinfo">
							<span class="layout-profile-name">Arlene Welch</span>
							<span class="layout-profile-role">Design Ops</span>
						</div>
					</button>
					<transition name="layout-submenu-container">
						<ul class="fadeInDown" v-show="activeTopbarItem === 'profile'">
							<li role="menuitem">
								<button class="p-link">
									<i class="pi pi-fw pi-user"></i>
									<span>Profile</span>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<i class="pi pi-fw pi-cog"></i>
									<span>Settings</span>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<i class="pi pi-fw pi-envelope"></i>
									<span>Messages</span>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<i class="pi pi-fw pi-bell"></i>
									<span>Notifications</span>
								</button>
							</li>
						</ul>
					</transition>
				</li>


				<li :class="[{'active-topmenuitem fadeInDown': activeTopbarItem === 'settings'}]">
					<button class="p-link layout-topbar-icon"
							@click="$emit('topbar-item-click',{originalEvent:$event,item:'settings'})">
						<i class="topbar-icon pi pi-fw pi-bell"></i>
					</button>
					<transition name="layout-submenu-container">
						<ul class="fadeInDown" v-show="activeTopbarItem === 'settings'">
							<li role="menuitem">
								<button class="p-link">
									<img src="layout/images/avatar-1.png" alt="roma-vue"/>
									<div class="topbar-menu-info">
										<span class="topbar-menu-name">Bithika Abhedananda</span>
										<span class="topbar-menu-role">User interface review is done.</span>
									</div>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<img src="layout/images/avatar-2.png" alt="roma-vue"/>
									<div class="topbar-menu-info">
										<span class="topbar-menu-name">Dai Jiang</span>
										<span class="topbar-menu-role">Uh, we have sort of a problem here.</span>
									</div>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<img src="layout/images/avatar-3.png" alt="roma-vue"/>
									<div class="topbar-menu-info">
										<span class="topbar-menu-name">Karlien Nijhuis</span>
										<span class="topbar-menu-role">You apparently didn’t put the thing</span>
									</div>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<img src="layout/images/avatar-4.png" alt="roma-vue"/>
									<div class="topbar-menu-info">
										<span class="topbar-menu-name">Tom Chun</span>
										<span class="topbar-menu-role">Please check the files</span>
									</div>
								</button>
							</li>
							<li role="menuitem">
								<button class="p-link">
									<img src="layout/images/avatar-5.png" alt="roma-vue"/>
									<div class="topbar-menu-info">
										<span class="topbar-menu-name">Maria Trofimova</span>
										<span class="topbar-menu-role">Meeting reports attached.</span>
									</div>
								</button>
							</li>
						</ul>
					</transition>
				</li>
			</ul>
	</div>
</template>

<script>
	export default {
		emits: ['menubutton-click', 'topbar-menubutton-click', 'topbar-item-click', 'right-menubutton-click'],
		props: {
			topbarMenuActive: Boolean,
			activeTopbarItem: String,
			inlineUser: Boolean,
		},
		methods: {
			onMenuButtonClick(event) {
				this.$emit('menubutton-click', event);
			},
			onTopbarMenuButtonClick(event) {
				this.$emit('topbar-menubutton-click', event);
			},
			onRightMenuButtonClick(event) {
				this.$emit('right-menubutton-click', event);
			}
		}
	}
</script>
