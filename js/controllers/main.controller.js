angular.module('todoapp', [])
    .controller('TodoListController', ["$http", function($http){
        self = this;

        self.currentItemTitle = "";
        self.maxTodoId = 0;

        self.todos = [];
        $http.get('js/list_samples.json')
            .success(function(data){
                self.todos = data.lists[0].todos;
                self.maxTodoId = self.findMaximumTodoId();
            });

        // implement item removal
        self.removeTodo = function(todoId){
            self.todos.forEach(function(item, index, arr){
                if(arr[index].todo_id === todoId){
                    self.todos.splice(index, 1);
                }
            });
            self.maxTodoId = self.findMaximumTodoId();
        };

        self.addTodo = function(){
            if (!self.currentItemTitle){
                return;
            }
            self.todos.push({
                todo_id: ++self.maxTodoId,
                todo_title: self.currentItemTitle
            });
            self.currentItemTitle = "";
        };

        self.findMaximumTodoId = function(){
            if (self.todos.length === 0){
                return 0;
            }
            maxValue = self.todos[0].todo_id;
            for(var i=0; i<self.todos.length;++i){
                if (self.todos[i].todo_id > maxValue){
                    maxValue = self.todos[i].todo_id;
                }
            }
            return maxValue;

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