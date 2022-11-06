<template>
	<div class="grid">
		<div class="col-3">
			<Button label="New Pre-Autherization" @click="$router.push({name:'add-pre-autherization'}) " class="p-text-button p-button-success" icon="pi pi-plus"/>
		</div>
		<div class="col-12">
			<div class="card">
				<Toast />
				<h5>Pre-Autherization Request</h5>
				<DataTable  :paginator="true" class="p-datatable-gridlines" :rows="10" dataKey="id" :rowHover="true" 
					:loading="loading" :filters="filters" responsiveLayout="scroll"
					>
					<template #header>
                        <div class="flex justify-content-end flex-column sm:flex-row">
                            <span class="p-input-icon-left mb-2">
                                <i class="pi pi-search" />
                                <InputText placeholder="Keyword Search" style="width: 100%"/>
                            </span>
                        </div>
                    </template>
                    <template #empty>
                        No Pre-Autherization Request Found.
                    </template>
                    <template #loading>
                        Loading Pre-Autherization Requests...
                    </template>
                    <Column field="id" header="Date Ordered" style="min-width:12rem">
                        <template>
                            
                        </template>
                    </Column>
                    <Column header="Type" field="account_id" style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    <Column header="Sub Type" field="patient" style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    <Column style="min-width:12rem">
                        <template >
							<div class="flex flex-row justify-content-evenly">
							<Button class="p-button-raised p-button-rounded p-button-success" :id="data.id" icon="pi pi-send" v-tooltip="'Send Eligibility Request'"  :disabled="eligibility_request[index]==true" />
							<Button class="p-button-raised p-button-rounded p-button-warning" :id="data.id" icon="pi pi-refresh"  v-tooltip="'Resend Eligibility Request'" :disabled="eligibility_response[index]==true" />
							</div>
                        </template>
                    </Column>
				</DataTable>
			</div>
		</div>		
	</div>
</template>

<script>
	
</script>

<style scoped lang="scss">
@import '../../assets/demo/styles/badges.scss';

::v-deep(.p-datatable-frozen-tbody) {
	font-weight: bold;
}

::v-deep(.p-datatable-scrollable .p-frozen-column) {
	font-weight: bold;
}

::v-deep(.p-progressbar) {
	height: .5rem;
	background-color: #D8DADC;

	.p-progressbar-value {
		background-color: #607D8B;
	}
}
.custom-error .p-tooltip-text {
    background-color: var(--pink-800);
    color: rgb(255, 255, 255);
}
.custom-error.p-tooltip-right .p-tooltip-arrow {
    border-right-color: var(--pink-800);
}
</style>
