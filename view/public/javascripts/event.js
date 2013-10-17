angular.module("wedding", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider.when("/countdown", {
            templateUrl: "/html/countdown.html"
        });

        $routeProvider.when("/lottery", {
            templateUrl: "/html/lottery.html"
        });
    })

    .controller("BodyCtrl", function ($scope) {
        $scope.listenKeyPress = function ($event) {
            $scope.$broadcast("KeyPressed", $event.keyCode);
        };
    })

    .controller("AsideCtrl", function ($scope) {
        $scope.modules = [
            {"id": "qanda", "text": "Q&A"},
            {"id": "countdown", "text": "count down"},
            {"id": "statistics", "text": "statistics"},
            {"id": "lottery", "text": "lottery"}
        ];

        $scope.selected = 0;

        $scope.select = function (index) {
            $scope.selected = index;
        };
    })

    .controller("CountdownCtrl", function ($scope, $timeout) {
        $scope.duration = 300;

        $scope.format = function (duration) {

            var min = parseInt(duration / 60),
                sec = duration % 60;

            if (min < 10) {
                min = "0" + min;
            }

            if (sec < 10) {
                sec = "0" + sec;
            }

            return min + ":" + sec;
        };

        $scope.start = function () {
            $scope.disabled = true;

            if ($scope.duration !== 0) {
                $timeout(function () {
                    $scope.duration = $scope.duration - 1
                    $scope.start();
                }, 1000);
            } else {
                $scope.done = true;
            }
        };
    })

    .controller("LotteryCtrl", function ($scope, $timeout) {
        $scope.winners = [];
        $scope.numbers = ["18016000168", "13661894823", "13564292353", "12345678901"],
        $scope.current = _.first($scope.numbers);

        $scope.lottery = function ($event) {
            $scope.pause = false;
            $scope.disabled = true;

            var max = $scope.numbers.length - 2;
            max = max < 0 ? 0 : max;

            $scope.timer = $timeout(function () {
                $scope.current = _.without($scope.numbers, $scope.current)[_.random(0, max)];
                $scope.lottery();
            }, 100);
        };

        $scope.$on("KeyPressed", function (event, msg) {
            if (Number(msg) === 13) {
                $scope.pause = !$scope.pause;

                if ($scope.pause) {
                    $timeout.cancel($scope.timer);
                    $scope.winners.push($scope.current);
                    $scope.numbers = _.without($scope.numbers, $scope.current);
                    $scope.disabled = false;
                } else {
                    $scope.pause = false;
                    $scope.lottery();
                }
            }
        });
    });