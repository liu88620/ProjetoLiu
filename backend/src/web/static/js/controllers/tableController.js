app.controller("tableController", function($scope, $window, $timeout, users_service){

    $scope.users = [];
    $scope.isLoading = true;
    $window.onload = function(){
        users_service.getUsers().
            success(function(result){
                $timeout(function(){
                    $scope.users = result;
                    $scope.isLoading = false;
                },2000);
            });
    }

    $scope.addUser = function(){
        $scope.users.push({'nome': $scope.nome, 'email': $scope.email, 'google_id': $scope.google_id})
        users_service.addUser($scope.nome, $scope.email, $scope.google_id)
    }
    $scope.removeUser = function(user, index){
        $scope.users.splice(index, 1)
        users_service.removeUser(user.email);
    }

});