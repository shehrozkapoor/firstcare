<template>
	<div class="grid">
		<div class="col-12">
			<div class="card">
				<Toast />
				<h5>Pre-Autherization Transections</h5>
				<DataTable :paginator="true" class="p-datatable-gridlines" :rows="10" dataKey="id" :rowHover="true" 
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
                        No Pre-Autherization Response Found.
                    </template>
                    <template #loading>
                        Loading Pre-Autherization Responses...
                    </template>
                    <Column field="MemberCardID" header="Member Card ID" style="min-width:12rem">
                        <template>
                            
                        </template>
                    </Column>
                    <Column header="Pre-authorizationID " field="Pre-authorization ID " style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    <Column header="TransactionDate/Time" field="Transaction Date/Time" style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    <Column header="Insurance Plan" field="Insurance" style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    <Column header="Status" field="Status" style="min-width:12rem">
                        <template >
                            
                        </template>
                    </Column>
                    

                    <Column style="min-width:12rem">
                        <template >
							<div class="flex flex-row justify-content-evenly">
							<Button type="button" icon="pi pi-search" class="p-button-primart" style="margin-right: .5em"
                        label="View Details">View Details</Button>
                    <Button type="button" icon="pi pi-replay" class="p-button-primart" style="margin-right: .5em" ></Button>
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
