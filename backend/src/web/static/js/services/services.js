app = angular.module("world-anime", []);

app.factory('users_service', function($http){
    return {
      getUsers: function(){
          return $http.get('/users_rest/get_all_users/')
      },
      addUser: function(nome, email, google_id){
          return $http.jsonp('/users_rest/add_user/'
              + '?name=' + nome + '&email=' + email + '&google_id=' + google_id)
      },
      removeUser: function(email){
          return $http.jsonp('/users_rest/remove_user/'
              + '?email=' + email)
      }
    };

});
