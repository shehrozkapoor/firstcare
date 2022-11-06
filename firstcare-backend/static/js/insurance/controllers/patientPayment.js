app.controller('PatientPaymentController', function ($scope, $http) {

  $scope.dataTableOptions = {};
  $scope.patient_payment_sub_data = [];

  $scope.simple_btn_patient_payment = (event) => {
    if (event.target.value === 'on') {
      event.target.value = 'off';
    } else {
      event.target.value = 'on';
    }
    document.querySelector('.simpleBtnStatus').innerText = event.target.value;
  }

  $scope.condensed_btn_patient_payment = (event) => {
    if (event.target.value === 'on') {
      event.target.value = 'off';
      $('.simple-btn').show();
    } else {
      event.target.value = 'on';
      $('.simple-btn').hide();
    }
    document.querySelector('.condensedBtnStatus').innerText = event.target.value;
  }

  $scope.hide_simple_condensed_btn = () => {
    $('.simple-condensed-btn').hide();
    $('.except-balance-body').show();
    $('.balance-body').hide();
  }


  $scope.show_simple_condensed_btn = () => {
    $('.simple-condensed-btn').show();
    $('.except-balance-body').show();
    $('.balance-body').hide();
  }


  $('.balance-body').hide();
  $scope.show_balance = (event) => {
    $('.except-balance-body').hide();
    $('.balance-body').show();
  }

  $scope.getTableData = (from_date, to_date, from_range, to_range) => {
    $scope.is_loading = true;
    $scope.isLoading($scope.is_loading);
    $scope.patient_payment_sub_data = [];

    $http.get(get_token)
      .then(
        (response) => {
          $http({
            method: "GET",
            url: insurance_patient_payment_url,
            headers: {
              'Authorization': `Token ${response.data.data.token}`
            },
            params: {
              "from_date": from_date == undefined ? undefined : from_date.toLocaleString().split(',')[0],
              "to_date": to_date == undefined ? undefined : to_date.toLocaleString().split(',')[0],
              "from_range": from_range == undefined ? undefined : from_range,
              "to_range": to_range == undefined ? undefined : to_range,
            }
          }).then((response) => {
            $scope.is_loading = false;
            $scope.isLoading($scope.is_loading);
            $scope.table_data = response.data.data;
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

  $scope.getSubData = (id) => {
    $scope.is_loading = true;
    $scope.isLoading($scope.is_loading);

    $http.get(get_token)
      .then(
        (response) => {
          $http({
              method: "GET",
              url: insurance_patient_payment_sub_data_url,
              headers: {
                'Authorization': `Token ${response.data.data.token}`
              },
              params: {
                "id": id
              }
            })
            .then((response) => {
                $scope.is_loading = false;
                $scope.isLoading($scope.is_loading);
                $scope.patient_payment_sub_data = response.data;
                $scope.patient_info = response.data.patient
                $scope.billing_id = response.data.patient.id
              }

              , (error) => {
                $scope.is_loading = false;
                $scope.isLoading($scope.is_loading);
                console.log(error.data)
              })
        },
        (error) => {
          $scope.is_loading = false;
          $scope.isLoading($scope.is_loading);
          console.log(error.data)
        }
      )
  }
  $scope.selectInput = () => {
    let table_rows = $('#patient-payment-sub-table tbody tr input');
    for (let row = 0; row < table_rows.length; row += 1) {
      if (table_rows[row].checked == false) {
        table_rows[row].checked = true;
      } else {
        table_rows[row].checked = false;
      }
    }
  }
  $scope.printSelected = () => {
    let table_rows = $('#patient-payment-sub-table tbody tr input');
    let div_element = document.createElement('div');
    div_element.innerHTML = `
      <div style="display: flex;flex-direction: row;justify-content: space-between;">
      <h3>Nadaa</h3>
      <h3>Payment Receipt</h3>
      </div>
      <hr>
      `;
    let table_element = document.createElement('table');
    let table_header = document.createElement('thead');
    table_header.innerHTML = `
        <tr style="text-align:left;">
        <th style="width:200px;">Patient</th>
        <th style="width:200px;">Amount Paid</th>
        <th style="width:200px;">Payment Type</th>
        <th style="width:200px;">Payment Date</th>
        <th style="width:200px;">Appointment</th>
        </tr>
      `;
    table_element.appendChild(table_header);
    var table_body = document.createElement('tbody');
    for (let row = 0; row < table_rows.length; row += 1) {
      if (table_rows[row].checked == true) {
        var parent_element = table_rows[row].parentElement.parentElement;
        var parent_element_childrens = parent_element.children;
        let innerEle = document.createElement('tr');
        innerEle.innerHTML = `
          <td style="width:200px;">${parent_element.id}</td>
          <td style="width:200px;">${parent_element_childrens[8].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[6].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[2].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[4].innerText}</td>
          `;
        table_body.append(innerEle);
      }
    }
    table_element.appendChild(table_body);
    div_element.appendChild(table_element);
    var generator = window.open();
    var layoutText = div_element;
    generator.document.write(layoutText.innerHTML);
    generator.document.close();
    generator.print();
    generator.close();
  }

  $scope.printSingleReciept = (event) => {
    var parent_element = event.currentTarget.parentElement.parentElement;
    let div_element = document.createElement('div');
    div_element.innerHTML = `
      <div style="display: flex;flex-direction: row;justify-content: space-between;">
      <h3>Nadaa</h3>
      <h3>Payment Receipt</h3>
      </div>
      <hr>
      `;
    let table_element = document.createElement('table');
    let table_header = document.createElement('thead');
    table_header.innerHTML = `
        <tr style="text-align:left;">
        <th style="width:200px;">Patient</th>
        <th style="width:200px;">Amount Paid</th>
        <th style="width:200px;">Payment Type</th>
        <th style="width:200px;">Payment Date</th>
        <th style="width:200px;">Appointment</th>
        </tr>
      `;
    table_element.appendChild(table_header);
    var table_body = document.createElement('tbody');
    var parent_element_childrens = parent_element.children;
    let innerEle = document.createElement('tr');
    innerEle.innerHTML = `
          <td style="width:200px;">${parent_element.id}</td>
          <td style="width:200px;">${parent_element_childrens[8].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[6].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[2].innerText}</td>
          <td style="width:200px;">${parent_element_childrens[4].innerText}</td>
          `;
    table_body.append(innerEle);
    table_element.appendChild(table_body);
    div_element.appendChild(table_element);
    var generator = window.open();
    var layoutText = div_element;
    generator.document.write(layoutText.innerHTML);
    generator.document.close();
    generator.print();
    generator.close();
  }
  $scope.exportToCsv = () => {
    var selected = []
    let table_rows = $('#patient-payment-sub-table tbody tr input');
    for (let row = 0; row < table_rows.length; row += 1) {
      if (table_rows[row].checked == true) {
        selected.push(table_rows[row].id);
      }
      if (selected.length == 0) {
        alert('cannot export empty data');
      } else {
        $http.get(get_token)
          .then(
            (response) => {
              $http({
                method: "GET",
                url: insurance_patient_payment_export_to_csv_url,
                headers: {
                  'Authorization': `Token ${response.data.data.token}`
                },
                params: {
                  "payment-id": selected.toString(),
                  "billing-id": $scope.billing_id,
                }
              }).then((response) => {
                downloadURI(base_url + response.data.url, response.data.file_name + '.csv');
              }, (error) => {
                console.log(error.data);
              })
            },
            (error) => {
              console.log(error.data);
            }
          )
      }
    }
  }


  $scope.getTableData($scope.from_date, $scope.to_date, $scope.from_range, $scope.to_range);

});