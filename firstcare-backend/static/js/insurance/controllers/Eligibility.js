app.controller('EligibilityController', function ($scope, $http) {
    $scope.showTable=false;
    $scope.coverage = "unknown"
    $scope.subscriber = "unknown"
    $scope.last_updated = "N/A"

    $scope.getEligibility = ()=>{
        $scope.is_loading = true;
        $scope.isLoading($scope.is_loading);
        if($scope.patient_mid === undefined || $scope.patient_mid.length === 0){
            alert("patient_id is required!!!")
        }
        else{
            $http.get(get_token).then((response)=>{
                $http.defaults.headers.post["Authorization"] = `TOKEN ${response.data.data.token}`
                $http({
                    url: insurance_eligibility_status_url,
                    method: "GET",
                    params: {patient_id: $scope.patient_mid},
                    headers:{"Authorization" : `TOKEN ${response.data.data.token}`}
                 }).then((response)=>{
                    if (response.data.data.length === 3){
                        $scope.coverage = `${response.data.data[0]['status']} Coverage [from:${response.data.data[1]['name']}]`
                        $scope.subscriber = `${response.data.data[2]['name'][0]['given'][0]} ${response.data.data[2]['name'][0]['family']} ${response.data.data[2]['birthDate']}`
                    }
                    else{
                        $scope.coverage = `${response.data.data[0]['status']} Coverage [from:${response.data.data[1]['name'][0]['given'][0]} ${response.data.data[1]['name'][0]['family']}]`
                        $scope.subscriber = `${response.data.data[1]['name'][0]['given'][0]} ${response.data.data[1]['name'][0]['family']} ${response.data.data[1]['birthDate']}`
                    }
                    var date = new Date(response.data.data[0]['meta']['lastUpdated']);
                    $scope.last_updated = date.toDateString()
                    $scope.is_loading = false;
                    $scope.isLoading($scope.is_loading);
                 },
                 (error) => {
                    $scope.is_loading = false;
                    $scope.isLoading($scope.is_loading);
                    console.log(error.data);
                  })
            })
        }
        $scope.is_loading = false;
        $scope.isLoading($scope.is_loading);
    }

    $scope.table_one_data = [
        {
            "coverage-level":"",
            "service_type":"Health Benefit Plan Coverage",
            "eligibility":"Plan: 2006-01-01",
            "notes":"Subscriber Additional ID:Group Number CARE1234",
        }
    ]
    $scope.table_two_data = [
        {
            "coverage_level":"Individual",
            "service_type":"Health Benefit Plan Coverage",
            "insurance_type":"MEDICARE PART A",
            "description":"MEDICARE PART A",
        }
    ]
})