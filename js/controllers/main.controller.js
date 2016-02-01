angular.module('todoapp', [])
    .controller('TodoListController', ["$http", function($http){
        self = this;

        self.currentItemTitle = "";

        self.todos = $http.get('js/list_samples.json')
            .success(function(data){
                self.todos = data[0].todos;
            });

        // implement item removal
        self.removeTodo = function(todoId){

        };

        self.addTodo = function(){
            // How do we deal with IDs?
            console.log("Calling");
            self.todos.push({
                todo_id: 1,
                todo_title: self.currentItemTitle
            });
            
        };
}]);