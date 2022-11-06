app.controller('billingSummaryController', function ($scope, $http) {
  $scope.is_loading = true;
  $scope.isLoading($scope.is_loading);
  $http.get(get_token).then((response) => {
      $http({
          method: 'GET',
          url: insurance_billing_url,
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${response.data.data.token}`
          }
        })
        .then((response) => {
          var month_to_date = parseFloat(response.data['month-to-date']['total-income']);
          var previous_month = parseFloat(response.data['previous-month']['total-income']);
          var quater_to_date = parseFloat(response.data['current-quater']['total-income']);
          var previous_quater = parseFloat(response.data['previous-quater']['total-income']);
          var year_to_date = parseFloat(response.data['year-to-date']['total-income']);


          var billing_summary_var = document.getElementById('billing_summary_chart').getContext('2d');
          var billing_summary_chart = new Chart(billing_summary_var, {
            type: 'bar',
            data: {
              labels: ['Month to Date', 'Last Month', 'Quater to date', 'Last Quater', 'Year to Date'],
              datasets: [{
                label: '# total amount',
                data: [month_to_date, previous_month, quater_to_date, previous_quater, year_to_date],
                backgroundColor: [
                  'rgb(29, 141, 29)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                ],
                borderColor: [
                  'rgb(29, 141, 29)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1
              }, ]
            },
            options: {
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
          });
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
        }, (error) => {
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
          console.log(error.data);
        });
    },
    (error) => {
      $scope.is_loading = false;
      $scope.isLoading($scope.is_loading);
      console.log(error.data);
    })
});