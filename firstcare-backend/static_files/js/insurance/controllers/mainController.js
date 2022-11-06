app.controller('myCTRL', function ($scope, $http, $compile) {
    $('.except_grand_total').hide();
  
    $scope.account_recieveale_click_Class = 1;
    $scope.product_click_Class = 1;
    $scope.fee_schedule_click_Class = 1;
    $scope.fee_schedule_add_click_Class = 1;
    $scope.billing_log_click_Class = 1;
    $scope.is_loading = true;
  
    $scope.search_place_holder = 'CPT/HCPCS/Custom Procedure';
  
  
    $scope.isLoading = (status) => {
      if (status == true) {
        $('.inner_main_div').css({
          "opacity": '0.2',
          'pointer-events': 'none'
        });
      } else {
        $('.inner_main_div').css({
          "opacity": '1',
          'pointer-events': 'all'
        });
      }
    }
  
    $scope.logout = () => {
      $scope.is_loading = true;
      $scope.isLoading($scope.is_loading);

      $http.get(get_token)
        .then((response) => {
          var token = response.data.data.token;
          $http.post(logout_url)
            .then((response) => {
              $scope.is_loading = false;
              $scope.isLoading($scope.is_loading);
              location.reload();
            }, (error) => {
              console.log(error.data);
            });
        }, (error) => {
          console.log(error.data);
        })
    }
  
  
    $scope.grand_total = (id) => {
      $('.except_grand_total').hide();
      $('.card').show();
    }
  
    $scope.excpet_grand_total = (id) => {
      $('.except_grand_total').show();
      $('.card').hide();
    }
  
    $scope.addTableRow = () => {
      var childs = angular.element('.batch-add-tbody')
      var lenght_num = document.querySelector('.batch-add-tbody').children.length;
      var element = document.createElement('tr');
      element.setAttribute('id', lenght_num + 1);
      element.innerHTML = `<td>${lenght_num+1}</td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td>
          <select name="" id="" class="select">
              <option value="">Unknown</option>
              <option value="">Automated Clearing House (ACH)</option>
              <option value="">Cash Concentration/Disbursement plus Addenda (CCD+)
                  (ACH)</option>
              <option value="">Corporate Trade Exchange (CTX) (ACH)</option>
              <option value="">Check</option>
              <option value="">Federal Reserve Funds/Wire Transfer - Nonrepetitive
              </option>
              <option value="">vPayment</option>
              <option value="">Non-Payment Data</option>
          </select>
      </td>
      <td><input type="number" value=0.00></td>
      <td><input type="date"></td>
      <td class="text-center" ng-click="removeTableRow($event)"><i class="bi bi-trash-fill text-danger"></i></td>`;
  
      childs.append($compile(element)($scope));
    }
    $scope.removeTableRow = (event) => {
      event.target.parentElement.parentElement.remove();
    }
  
    $scope.account_recievavle_click = function (item) {
      $scope.account_recieveale_click_Class = item;
    }
  
    $scope.product_click = function (item) {
      $scope.product_click_Class = item;
    }
  
    $scope.fee_schedule_click = function (item) {
      $scope.fee_schedule_click_Class = item;
      if (item == 1) {
        $scope.search_place_holder = 'CPT/HCPCS/Custom Procedure';
      } else if (item == 2) {
        $scope.search_place_holder = 'ICD-9 code';
      } else {
        $scope.search_place_holder = 'ICD-10 code';
      }
    }
  
    $scope.fee_schedule_add_click = function (item) {
      $scope.fee_schedule_add_click_Class = item;
    }
  
    $scope.adjustment_master_click = function (item) {
      $scope.adjustment_master_click_Class = item;
    }
  
    $scope.adjustment_master_add_click = function (item) {
      $scope.adjustment_master_add_click_Class = item;
    }
  
    $scope.billing_log_click = function (item) {
      $scope.billing_log_click_Class = item;
    }
  
  });