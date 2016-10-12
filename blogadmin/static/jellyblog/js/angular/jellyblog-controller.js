/**
 * 액티브 기능설정을 위하여 만들어 둠 전체적인 수정 필요
 */


app.controller("NavActiveController",['$scope','$location',ActiveController]);

function ActiveController($scope, $location) {
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
};
