angular.module('todoapp', [])
    .controller('TodoListController', ["$http", function($http){
        self = this;

        self.currentItemTitle = "";

        self.todos = [];
        $http.get('js/list_samples.json')
            .success(function(data){
                self.todos = data.lists[0].todos;
            });

        // implement item removal
        self.removeTodo = function(todoId){
            self.todos.forEach(function(item, index, arr){
                if(arr[index].todo_id === todoId){
                    self.todos.splice(index, 1);
                }
            });
        };

        self.addTodo = function(){
            // How do we deal with IDs?
            console.log("Calling");
            self.todos.push({
                todo_id: 1,
                todo_title: self.currentItemTitle
            });
            self.currentItemTitle = "";

        };

    }])

    .controller('MenuListController', ["$http", function($http){
        menu = this;

        menu.lists = [];

        $http.get('js/list_samples.json')
            .success(function(data){
                menu.lists = data.lists;
            });

}]);