<template>
	<div class="grid layout-dashboard">
		<div class="col-12 md:col-6 lg:col-3">
			<div class="overview-box card">
				<div class="overview-box-value">90</div>
				<div class="overview-box-title">TASKS</div>
				<img src="layout/images/dashboard/graph-tasks.svg" alt="roma"/>
				<div class="overview-box-status">
					+8.9% <i class="pi pi-arrow-circle-up"></i>
				</div>
			</div>
		</div>
		<div class="col-12 md:col-6 lg:col-3">
			<div class="overview-box card">
				<div class="overview-box-value">1259</div>
				<div class="overview-box-title">PURCHASES</div>
				<img src="layout/images/dashboard/graph-purchases.svg" alt="roma"/>
				<div class="overview-box-status">
					+67.2% <i class="pi pi-arrow-circle-up"></i>
				</div>
			</div>
		</div>
		<div class="col-12 md:col-6 lg:col-3">
			<div class="overview-box card">
				<div class="overview-box-value">21</div>
				<div class="overview-box-title">ISSUES</div>
				<img src="layout/images/dashboard/graph-issues.svg" alt="roma"/>
				<div class="overview-box-status">
					+3.0% <i class="pi pi-arrow-circle-up"></i>
				</div>
			</div>
		</div>
		<div class="col-12 md:col-6 lg:col-3">
			<div class="overview-box card">
				<div class="overview-box-value">42</div>
				<div class="overview-box-title">MESSAGES</div>
				<img src="layout/images/dashboard/graph-messages.svg" alt="roma"/>
				<div class="overview-box-status">
					+12.5% <i class="pi pi-arrow-circle-up"></i>
				</div>
			</div>
		</div>

		<div class="col-12 md:col-8 lg:col-8">
			<div class="card card-w-title">
				<h5>Statistics</h5>
				<Chart type="line" :data="chartData" :options="chartOptions"/>
			</div>
		</div>

		<div class="col-12 md:col-4 lg:col-4">
			<div class="timeline card card-w-title">
				<h5>Timeline</h5>
				<ul>
					<li>
						<i class="pi pi-image"></i>
						<span class="timeline-event-title">Uploaded Images</span>
						<span class="timeline-event-time">15m</span>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
						<div class="grid">
							<div class="col-6">
								<img src="layout/images/dashboard/image-1.jpg" alt="roma"/>
							</div>
							<div class="col-6">
								<img src="layout/images/dashboard/image-2.jpg" alt="roma"/>
							</div>
						</div>
					</li>
					<li>
						<i class="pi pi-star-fill"></i>
						<span class="timeline-event-title">Favorites</span>
						<span class="timeline-event-time">1h</span>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. </p>
					</li>
					<li>
						<i class="pi pi-users"></i>
						<span class="timeline-event-title">Meeting</span>
						<span class="timeline-event-time">2h</span>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. </p>
					</li>
					<li>
						<i class="pi pi-money-bill"></i>
						<span class="timeline-event-title">Payment Received</span>
						<span class="timeline-event-time">3h</span>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. </p>
					</li>
				</ul>
			</div>
		</div>

		<div class="col-12 xl:col-6">
			<div class="expenses card card-w-title">
				<h5>Expenses</h5>
				<div class="chart">
					$5500
				</div>
				<div class="grid expenses-legend">
					<div class="col-12 lg:col-4">
						<i class="pi pi-circle-on"></i>
						<span class="expenses-title">Printer: Color Cartridge</span>
						<div class="expenses-price">$420</div>
						<span class="legend-status">23+ more than last month</span>
					</div>
					<div class="col-12 lg:col-4">
						<i class="pi pi-circle-on"></i>
						<span class="expenses-title">Printer: B&amp;W Cartridge</span>
						<div class="expenses-price">$680</div>
						<span class="legend-status">60+ more than last month</span>
					</div>
					<div class="col-12 lg:col-4">
						<i class="pi pi-circle-on"></i>
						<span class="expenses-title">Coffee Capsules</span>
						<div class="expenses-price">$150</div>
						<span class="legend-status">8% less than last month</span>
					</div>
				</div>

				<div class="expenses-footer">
					<a href="#">View more details >></a>
				</div>
			</div>
		</div>
		<div class="col-12 xl:col-6">
			<div class="card card-w-title">
				<h5>Schedule</h5>
				<FullCalendar :events="events" :options="options"/>
			</div>
		</div>

		<div class="col-12 lg:col-6 xl:col-4">
			<div class="card card-w-title tasks">
				<h5>Tasks</h5>
				<p>You have <span class="task-highlight">completed</span> 3 tasks out of 6.</p>
				<ProgressBar :value="50" :showValue="false"/>
				<ul>
					<li>
						<Checkbox name="task" value="reports" v-model="tasksCheckbox"/>
						<span>Sales Reports</span>
						<span class="task-badge-open">Open</span>
					</li>
					<li>
						<Checkbox name="task" value="pay" v-model="tasksCheckbox"/>
						<span>Pay Invoices</span>
						<span class="task-badge-open">Open</span>
					</li>
					<li>
						<Checkbox name="task" value="dinner" v-model="tasksCheckbox"/>
						<span>Birthday Party</span>
						<span class="task-badge-open">Open</span>
					</li>
					<li>
						<Checkbox name="task" value="meeting" v-model="tasksCheckbox"/>
						<span>Client Meeting</span>
						<span class="task-badge-closed">Closed</span>
					</li>
					<li>
						<Checkbox name="task" value="theme" v-model="tasksCheckbox"/>
						<span>New Themes</span>
						<span class="task-badge-closed">Closed</span>
					</li>
					<li>
						<Checkbox name="task" value="ticket" v-model="tasksCheckbox"/>
						<span>Flight Ticket</span>
						<span class="task-badge-closed">Closed</span>
					</li>
				</ul>
			</div>
		</div>

		<div class="col-12 lg:col-6 xl:col-4">
			<div class="card card-w-title resolution-center ui-fluid">
				<h5>Resolution Center</h5>

				<InputText type="text" placeholder="Username"/>

				<InputText type="text" placeholder="Email"/>

				<Textarea :rows="5"  placeholder="Message"/>

				<div class="resolution-button-bar">
					<Button type="button" label="Send" icon="pi pi-envelope"></Button>
					<Button type="button" label="Save" icon="pi pi-plus" class="p-button-secondary"></Button>
				</div>
			</div>
		</div>

		<div class="col-12 xl:col-4">
			<div class="card card-w-title team">
				<h5>Team</h5>
				<ul>
					<li>
						<img src="layout/images/avatar-1.png" alt="roma-layout"/>
						<div class="team-box">
							<span class="team-member">John Swisher Welch</span>
							<span class="team-member-account">@jswisher</span>
						</div>
						<a href="#">
							<i class="pi pi-paperclip"></i>
						</a>
						<a href="#">
							<i class="pi pi-comment"></i>
						</a>
						<a href="#">
							<i class="pi pi-share-alt"></i>
						</a>
					</li>
					<li>
						<img src="layout/images/avatar-2.png" alt="roma-layout"/>
						<div class="team-box">
							<span class="team-member">Bernd Pfefferberg</span>
							<span class="team-member-account">@pfefferberg</span>
						</div>
						<a href="#">
							<i class="pi pi-paperclip"></i>
						</a>
						<a href="#">
							<i class="pi pi-comment"></i>
						</a><a href="#">
						<i class="pi pi-share-alt"></i>
					</a>
					</li>
					<li>
						<img src="layout/images/avatar-3.png" alt="roma-layout"/>
						<div class="team-box">
							<span class="team-member">Chinaza Akachi</span>
							<span class="team-member-account">@chinazzza_</span>
						</div>
						<a href="#">
							<i class="pi pi-paperclip"></i>
						</a>
						<a href="#">
							<i class="pi pi-comment"></i>
						</a>
						<a href="#">
							<i class="pi pi-share-alt"></i>
						</a>
					</li>
					<li>
						<img src="layout/images/avatar-4.png" alt="roma-layout"/>
						<div class="team-box">
							<span class="team-member">Luka Miller</span>
							<span class="team-member-account">@luk4mr</span>
						</div>
						<a href="#">
							<i class="pi pi-paperclip"></i>
						</a>
						<a href="#">
							<i class="pi pi-comment"></i>
						</a>
						<a href="#">
							<i class="pi pi-share-alt"></i>
						</a>
					</li>
					<li>
						<img src="layout/images/avatar-5.png" alt="roma-layout"/>
						<div class="team-box">
							<span class="team-member">Arlene Welch</span>
							<span class="team-member-account">@arlene</span>
						</div>
						<a href="#">
							<i class="pi pi-paperclip"></i>
						</a>
						<a href="#">
							<i class="pi pi-comment"></i>
						</a>
						<a href="#">
							<i class="pi pi-share-alt"></i>
						</a>
					</li>
				</ul>
			</div>
		</div>

		<div class="col-12 xl:col-8">
			<div class="card card-w-title live-support">
				<h5>Live Support</h5>
				<ul>
					<li class="message-from">
						<div class="grid">
							<div class="col-fixed">
								<img src="layout/images/avatar-1.png" alt="roma-layout"/>
							</div>
							<div class="col">
								<div class="chat-message">Lorem ipsum dolor sit amet, consectetur adipiscing
									elit.
									Nam ac euismod justo, eget blandit purus.
								</div>
							</div>
						</div>
					</li>
					<li class="message-to">
						<div class="grid">
							<div class="col">
								<div class="chat-message">Mauris malesuada quis risus ut consequat.
									Maecenas ornare nunc risus, pulvinar euismod mi pellentesque eget.
								</div>
							</div>
							<div class="col-fixed">
								<img src="layout/images/avatar-1.png" alt="roma-layout"/>
							</div>
						</div>
					</li>
					<li class="message-from">
						<div class="grid">
							<div class="col-fixed">
								<img src="layout/images/avatar-2.png" alt="roma-layout"/>
							</div>
							<div class="col">
								<div class="chat-message">Lorem ipsum dolor sit amet, consectetur adipiscing
									elit.
									Nam ac euismod justo, eget blandit purus.
								</div>
							</div>
						</div>
					</li>
				</ul>

				<div class="new-message">
					<div class="grid grid-nogutter">
						<div class="col">
							<InputText id="input" type="text" placeholder="Write a message.."/>
						</div>
						<div class="col-fixed">
							<Button type="button" label="Send"></Button>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="col-12 xl:col-4">
			<div class="card user-card">
				<div class="user-card-header"></div>

				<div class="user-card-content">
					<img src="layout/images/avatar.png" alt="roma-layout"/>

					<Button icon="pi pi-cog" @click="toggle"/>
					<Menu :model="menuItems" :popup="true" ref="menu" appendTo="body"/>

					<div class="user-card-name">
						<span>Maria Llescas</span>
					</div>

					<div class="user-detail">
						<div class="grid">
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Tasks</div>
									<div class="user-detail-box-detail">3 open</div>
									<i class="pi pi-list"></i>
									<ProgressBar :value="60" :showValue="false"/>
								</div>
							</div>
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Revenue</div>
									<div class="user-detail-box-detail">+20%</div>
									<i class="pi pi-dollar"></i>
									<ProgressBar :value="80" :showValue="false"/>
								</div>
							</div>
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Payments</div>
									<div class="user-detail-box-detail">24 New</div>
									<i class="pi pi-money-bill"></i>
									<ProgressBar :value="60" :showValue="false"/>
								</div>
							</div>
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Clients</div>
									<div class="user-detail-box-detail">+80%</div>
									<i class="pi pi-users"></i>
									<ProgressBar :value="50" :showValue="false"/>
								</div>
							</div>
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Sales</div>
									<div class="user-detail-box-detail">3 open</div>
									<i class="pi pi-money-bill"></i>
									<ProgressBar :value="60" :showValue="false"/>
								</div>
							</div>
							<div class="col-4">
								<div class="user-detail-box">
									<div class="user-detail-box-name">Tasks</div>
									<div class="user-detail-box-detail">3 open</div>
									<i class="pi pi-chart-bar"></i>
									<ProgressBar :value="60" :showValue="false"/>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="col-12 xl:col-8">
			<div class="card card-w-title global-sales ui-fluid">
				<h5>Global Sales</h5>
				<DataTable :value="products" responsiveLayout="scroll" :rows="5" style="margin-bottom: 20px" :paginator="true">
					<Column>
						<template #header>
							Logo
						</template>
						<template #body="slotProps">
							<span class="p-column-title">Image</span>
							<img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" width="50" />
						</template>
					</Column>
					<Column field="code" header="Code" :sortable="true">
						<template #body="slotProps">
							<span class="p-column-title">Code</span>
							{{slotProps.data.code}}
						</template>
					</Column>
					<Column field="name" header="Name" :sortable="true">
						<template #body="slotProps">
							<span class="p-column-title">Name</span>
							{{slotProps.data.name}}
						</template>
					</Column>
					<Column field="category" header="Category" :sortable="true">
						<template #body="slotProps">
							<span class="p-column-title">Category</span>
							{{slotProps.data.category}}
						</template>
					</Column>
					<Column field="price" header="Price" :sortable="true">
						<template #body="slotProps">
							<span class="p-column-title">Price</span>
							{{formatCurrency(slotProps.data.price)}}
						</template>
					</Column>
					<Column>
						<template #header>
							View
						</template>
						<template #body>
							<Button icon="pi pi-search" class="mr-2 mb-1"></Button>
							<Button icon="pi pi-times" class="p-button-danger mb-1"></Button>
						</template>
					</Column>
				</DataTable>
			</div>
		</div>

		<div class="col-12 xl:col-4">
			<div class="card weather">
				<div class="weather-header">
					<img src="layout/images/dashboard/weather.png" alt="roma-layout"/>
				</div>
				<div class="weather-content">
					<div class="weather-city">Antalya</div>
					<div class="weather-status">24&#176; C <i class="pi pi-map-marker"></i></div>
					<div class="weather-detail">Feels like 26&#176; Low 14 &#176; High 28 &#176;</div>
					<a href="#">Change Location</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import dayGridPlugin from '@fullcalendar/daygrid';
	import timeGridPlugin from '@fullcalendar/timegrid';
	import interactionPlugin from '@fullcalendar/interaction';

	export default {
		data() {
			return {
				chartData: {
					labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
					datasets: [
						{
							label: 'Sales',
							data: [12, 19, 3, 5, 2, 3, 9],
							borderColor: [
								'#0F97C7',
							],
							borderWidth: 3,
							borderDash: [5, 5],
							fill: false,
							pointRadius: 3,
							tension: .4
						}, 
						{
							label: 'Income',
							data: [1, 2, 5, 3, 12, 7, 15],
							backgroundColor: [
								'rgba(187,222,251,0.2)',
							],
							borderColor: [
								'#578697',
							],
							borderWidth: 3,
							fill: true,
							tension: .4
						},
						{
							label: 'Expenses',
							data: [7, 12, 15, 5, 3, 13, 21],
							borderColor: [
								'#1BA7AF',
							],
							borderWidth: 3,
							fill: false,
							pointRadius: [4, 6, 4, 12, 8, 0, 4],
							tension: .4
						},
						{
							label: 'New Users',
							data: [3, 7, 2, 17, 15, 13, 19],
							borderColor: [
								'#E2841A',
							],
							borderWidth: 3,
							fill: false,
							tension: .4
						}
					]
				},
				chartOptions: {
					responsive: true,
					hover: {
						mode: 'index'
					},
					scales: {
						x: {
							display: true,
							title: {
								display: true,
								text: 'Month'
							}
						},
						y: {
							display: true,
							title: {
								display: true,
								text: 'Value'
							}
						}
					}
				},
				options: {
					plugins:[dayGridPlugin, timeGridPlugin, interactionPlugin],
					initialDate : '2023-01-01',
					headerToolbar: {
						left: 'prev,next',
						center: 'title',
						right: 'dayGridMonth,timeGridWeek,timeGridDay'
					},
					editable: true,
					selectable:true, 
					selectMirror: true, 
					dayMaxEvents: true
				},
				events: null,
				tasksCheckbox: [],
				products: null,
				selectedProducts: null,
				menuItems: [
					{
						label: 'Save', icon: 'pi pi-fw pi-check'
					},
					{
						label: 'Update', icon: 'pi pi-fw pi-refresh'
					},
					{
						label: 'Delete', icon: 'pi pi-fw pi-trash'
					}
				],
			}
		},
		methods: {
			toggle(event) {
				this.$refs.menu.toggle(event);
			},
			formatCurrency(value) {
				return value.toLocaleString('en-US', {style: 'currency', currency: 'USD'});
			}
		}
	}
</script>

<style scoped>
::v-deep(.fc .fc-col-header-cell-cushion),
::v-deep(.fc-daygrid-dot-event .fc-event-time),
::v-deep(.fc-daygrid-dot-event .fc-event-title),
::v-deep(.fc .fc-daygrid-day-number),
::v-deep(.fc .fc-daygrid-more-link) {
	color: var(--text-color);
}

::v-deep(.fc-header-toolbar) {
    display: flex;
    flex-wrap: wrap;
}
</style>
