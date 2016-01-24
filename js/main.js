$(document).ready(function(){
    var createTaskButton = $('#createTask');

    createTaskButton.on('click', function(e){
        taskInput = $('.todo-input-text');
        taskString = taskInput.val();
        
        if(taskString !== ''){
            var taskList = $('#task-list');

            var taskEntry = $('<li class="row task-entry"></li>');
            var checkedColumn = $('<input type="checkbox" class="col-xs-1">');         
            var titleColumn = $('<div class="task-title col-xs-10">' + taskString + '</div>');
            
            checkedColumn.change(function(e){
                titleColumn.toggleClass('deleted-text');
            });
            
            var deleteColumn = $('<span class="glyphicon glyphicon-trash pull-right task-delete"></span>');

            deleteColumn.on('click', function(e){
                deleteTarget = deleteColumn.parent();
                deleteTarget.hide(250, function(){
                    deleteTarget.remove();
                });
            });

            taskEntry.append(checkedColumn);
            taskEntry.append(titleColumn);
            taskEntry.append(deleteColumn);

            taskList.append(taskEntry);

            clearInput(taskInput);
        } 
        
        else {  
            $("#alertEmptyField").removeClass('hide');
            setTimeout(function(){
                $("#alertEmptyField").hide(250);
            }, 1500);
            // show method is called BEFORE the previous .hide() method. 
            $("#alertEmptyField").show(0);                 
        }
    });

});

var clearInput = function(input){
    input.val('');
};

var deleteTask = function(taskId){
    // it would be great to implement deletion this way;
};
