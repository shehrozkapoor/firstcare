var app = angular.module('Insurance.main', ['ui.router', 'datatables']);

app.config(['$interpolateProvider', function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
}]);

app.config(function ($stateProvider, $urlRouterProvider) {

  var billingState = {
    name: 'billing-summary',
    url: '/billing-summary',
    controller: "billingSummaryController",
    templateUrl: insurance_partials_base_url + 'billingsummary.html',
  }
  var liveClaimsState = {
    name: 'liveclaims',
    url: '/live-claims',
    controller: "liveClaimController",
    templateUrl: insurance_partials_base_url + 'liveclaimfields.html'

  }
  var EligibilityState = {
    name: 'eligibility',
    url: '/eligibility',
    controller: "EligibilityController",
    templateUrl: insurance_partials_base_url + 'eligibility.html'

  }
  var patientPaymentState = {
    name: 'patient-payments',
    url: '/patient-payments',
    controller: "PatientPaymentController",
    templateUrl: insurance_partials_base_url + 'patientPayment.html'

  }
  var daySheetState = {
    name: 'day-sheet',
    url: '/day-sheet',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'daySheet.html',
  }

  var transactionsState = {
    name: 'transactions',
    url: '/transactions',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'transactions.html'

  }
  var remitanceReportsState = {
    name: 'remitance-reports',
    url: '/remitance-reports',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'remittanceReports.html'

  }

  var unmatchedERAsState = {
    name: 'unmatched-ERAs',
    url: '/unmatched-ERAs',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'unmatchedEras.html'
  }

  var accountReceivableState = {
    name: 'account-receivable',
    url: '/account-receivable',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'accountReceivable.html'

  }

  var patientStatementsState = {
    name: 'patient-statements',
    url: '/patient-statements',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'PatientStatements.html'

  }

  var productsState = {
    name: 'products',
    url: '/products',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'products.html'

  }

  var balanceState = {
    name: 'balance',
    url: '/balance',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'balance.html'

  }

  var feeScheduleState = {
    name: 'fee-schedule',
    url: '/fee-schedule',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'feeSchedule.html'

  }

  var underPaidItemsState = {
    name: 'underpaid-items',
    url: '/underpaid-items',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'underpaidItems.html'

  }

  var adjustmentMasterState = {
    name: 'adjustment-master',
    url: '/adjustment-master',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'adjustmentMaster.html'

  }

  var salesTaxState = {
    name: 'sales-tax',
    url: '/sales-tax',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'salesTax.html'

  }

  var billingLogState = {
    name: 'billing-log',
    url: '/billing-log',
    controller: "myCTRL",
    templateUrl: insurance_partials_base_url + 'BillingLog.html'

  }

  $urlRouterProvider.otherwise('/billing-summary');
  $stateProvider.state(billingState);
  $stateProvider.state(liveClaimsState);
  $stateProvider.state(EligibilityState);
  $stateProvider.state(patientPaymentState);
  $stateProvider.state(daySheetState);
  $stateProvider.state(transactionsState);
  $stateProvider.state(remitanceReportsState);
  $stateProvider.state(unmatchedERAsState);
  $stateProvider.state(accountReceivableState);
  $stateProvider.state(patientStatementsState);
  $stateProvider.state(productsState);
  $stateProvider.state(balanceState);
  $stateProvider.state(feeScheduleState);
  $stateProvider.state(underPaidItemsState);
  $stateProvider.state(adjustmentMasterState);
  $stateProvider.state(salesTaxState);
  $stateProvider.state(billingLogState);

});
