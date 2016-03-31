/**
 * 추후 기능 추가를 위해 생성해 둠
 */
var app = angular.module("jellyBlog",['slickCarousel']);
app.controller("MainCtrl", [
    '$scope',
    '$http',
    function($scope, $http) {
        $scope.notes = [];

        $scope.slickConfig = {
            enabled: true,
            autoplay: false,
            draggable: false,
            method: {},
            event: {
                beforeChange: function (event, slick, currentSlide, nextSlide) {
                },
                afterChange: function (event, slick, currentSlide, nextSlide) {
                }
            }
        };

        $scope.noteInit = function () {
            $http
                .get("/api/notes/")
                .then(function successCallback(response) {
                    $scope.notes = response.data;
                });
        };
    }
]);
