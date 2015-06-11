//Created by Jelly Choi on 2015-06-11.

app.controller("NavActiveController",['$scope','$location',ActiveController]);

function ActiveController($scope, $location) {
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
};
app.controller("SideActiveController",['$scope','$location',SideActiveController]);

function SideActiveController($scope, $location) {
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
};