var getApp = angular.module('getApp', []);

getApp.controller('getController', function($scope, $http) {

    $scope.user = {};

    $scope.submitForm = function() {

        $http({
            method  : 'GET',
            url     : '../api/hypotenuse',
            params  : $scope.user,
            headers : {'Content-Type': 'application/json'}
        })
            .success(function(data) {
                $scope.result = data.result.toFixed(2);
            })
            .error(function(data) {
                $scope.result = data.message;
            });
    };
});