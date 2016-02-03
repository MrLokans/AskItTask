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
                console.log("Input is empty!");
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

    }])

    .directive('todoList', function(){

        return {
            restrict: 'E',
            controller: "TodoListController",
            controllerAs: "todo",
            templateUrl: 'templates/todo-list.html',

            link: function(scope, element, attrs, ctrl) {
                var taskAddBtn = element.find('#create-task-btn');
                var taskInput = element.find('.todo-input-text');


                taskAddBtn.on('click', function(){
                    
                    if(ctrl.currentItemTitle === '') {  
                        element.find("#alertEmptyField").removeClass('hide');
                        setTimeout(function(){
                            element.find("#alertEmptyField").hide(250);
                        }, 1500);
                        // show method is called BEFORE the previous .hide() method. 
                        element.find("#alertEmptyField").show(0);                 
                    } else {
                        ctrl.addTodo();
                    }
                });

                taskAddBtn.on('keypress', function(e){
                    console.log(e);
                    if(e.keyCode === 13){
                        ctrl.addTodo();
                    } else {
                        console.log(e);
                    }
                });
            }
        }
    })
    .directive('todoLeftMenu', function(){
        return {
            restrict: 'E',
            controller: "MenuListController",
            controllerAs: "menu",
            templateUrl: 'templates/todo-left-menu.html'
        }

    });

