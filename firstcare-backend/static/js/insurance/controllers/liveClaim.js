app.controller('liveClaimController', function ($scope, $http) {
  $scope.is_loading = true;
  $scope.isLoading($scope.is_loading);
  $('#BatchStatusChangeModel').modal('hide');
  $scope.closeModel = () => {
    $('#BatchStatusChangeModel').modal('hide');
  }
  $scope.clearDates = () => {
    $scope.from_date_input = undefined;
    $scope.to_date_input = undefined;
  }

  $scope.selectedRowConfirm = (value) => {
    var selectedRowlength = $('.selected_row_tbody').children().length;
    if (value === 'CONFIRM' && selectedRowlength !== 0) {
      $('#selectRowTableConfirm').attr('disabled', false);
    } else {
      $('#selectRowTableConfirm').attr('disabled', true);
    }
  }

  $scope.statusButton = (id) => {
    $scope.selectedStatus = id;
    var selectRowsNotZero = false;
    let table_rows = $('#live-claim-fields-table tbody tr input');
    for (let row = 0; row < table_rows.length; row += 1) {
      if (table_rows[row].checked == true) {
        selectRowsNotZero = true;
        var element = document.createElement('tr');
        var getRow = table_rows[row].parentElement.parentElement
        element.setAttribute('id', getRow.children[1].innerText);
        element.innerHTML = `
          <td>${getRow.children[1].innerText}</td>
          <td>${getRow.children[2].innerText}</td>
          <td>${getRow.children[3].innerText}</td>
          `;
        $('.selected_row_tbody').append(element);
      }
    }
    if (selectRowsNotZero == false) {
      $('.selected_row_warning').show();
    } else {
      $('.selected_row_warning').hide();
    }
    $('#BatchStatusChangeModel').modal('show');
  }


  $scope.ChangeStatus = () => {
    $scope.is_loading = true;
    $scope.isLoading($scope.is_loading);
    var select_rows = $('.selected_row_tbody').children();
    var claim_ids = [];
    select_rows.each(function () {
      claim_ids.push($(this).attr("id"));
    });
    $http.get(get_token)
      .then(
        (response) => {
          var xsrf = {
            "claim-list": claim_ids,
            "claim-status": $scope.selectedStatus
          };
          $http.defaults.headers.post["Authorization"] = `TOKEN ${response.data.data.token}`
          $http.post(insurance_batch_status_change_url, xsrf).then((response) => {
            if (response.data.message == 'Successfull') {
              claim_ids.forEach(item => {
                document.getElementById(`billing_status_${item}`).innerText = response.data.status;
              });
              $('#BatchStatusChangeModel').modal('hide');
            }
          }, (error) => {
            console.log(error.data);
          })
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
        },
        (error) => {
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
          console.log(error.data);
        }
      )
  }
  $scope.selectInput = () => {
    let table_rows = $('#live-claim-fields-table tbody tr input');
    for (let row = 0; row < table_rows.length; row += 1) {
      if (table_rows[row].checked == false) {
        table_rows[row].checked = true;
      } else {
        table_rows[row].checked = false;
      }
    }
  }

  $scope.dataTableOptions = {
    scrollX: 1000,
    scrollY: 400,
    "columnDefs": [{
        "width": "10px",
        "height": "30px",
        "targets": 0
      },
      {
        "width": "150px",
        "targets": 1
      },
      {
        "width": "150px",
        "targets": 2
      },
      {
        "width": "150px",
        "targets": 3
      },
      {
        "width": "150px",
        "targets": 4
      },
      {
        "width": "150px",
        "targets": 5
      },
      {
        "width": "150px",
        "targets": 6
      },
      {
        "width": "150px",
        "targets": 7
      },
      {
        "width": "150px",
        "targets": 8
      },
      {
        "width": "150px",
        "targets": 9
      },
      {
        "width": "150px",
        "targets": 10
      },
      {
        "width": "150px",
        "targets": 11
      },
      {
        "width": "150px",
        "targets": 12
      },
      {
        "width": "150px",
        "targets": 13
      },
      {
        "width": "150px",
        "targets": 14
      },
      {
        "width": "150px",
        "targets": 15
      },
      {
        "width": "150px",
        "targets": 16
      },
      {
        "width": "150px",
        "targets": 17
      },
      {
        "width": "150px",
        "targets": 18
      },
      {
        "width": "150px",
        "targets": 19
      },
      {
        "width": "150px",
        "targets": 20
      },
      {
        "width": "150px",
        "targets": 21
      },
      {
        "width": "150px",
        "targets": 22
      },
      {
        "width": "150px",
        "targets": 23
      },
    ]
  };

  $scope.getTableData = (from_date, to_date, method) => {

    $scope.is_loading = true;
    $scope.isLoading($scope.is_loading);
    $http.get(get_token)
      .then(
        (response) => {
          $http({
            method: "GET",
            url: insurance_live_claim_url,
            headers: {
              'Authorization': `Token ${response.data.data.token}`
            },
            params: {
              "from-date": from_date == undefined ? undefined : from_date.toLocaleString().split(',')[0],
              "to-date": to_date == undefined ? undefined : to_date.toLocaleString().split(',')[0],
              "method": method
            }
          }).then((response) => {
            $scope.table_data = response.data.data;
            $scope.is_loading = false;
            $scope.isLoading($scope.is_loading);
          }, (error) => {
            $scope.is_loading = false;
            $scope.isLoading($scope.is_loading);
            console.log(error.data);
          })
        },
        (error) => {
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
          console.log(error.data);
        }
      )
  };
  $scope.getTableData();
});