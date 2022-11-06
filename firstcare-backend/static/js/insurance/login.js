var myapp = angular.module('insurance.login',[]);

myapp.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
  }]);

myapp.controller('loginCtrl',($scope,$http)=>{
    $scope.login = ()=>{
        var data = {
            username:$scope.username,
            password:$scope.password
        };
        $http.post(login,data)
        .then((response)=>{
            console.log(response)
            location.reload();
            $scope.message = undefined;
        },
        (error)=>{
            $scope.message = error.data;
        })
    }
})