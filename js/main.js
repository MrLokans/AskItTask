$(document).ready(function(){
    var createTaskButton = $('#createTask');

    createTaskButton.on('click', function(e){
        taskInput = $('.todo-input-text');
        taskString = taskInput.val();
        
        if(taskString != ''){
            var taskList = $('#task-list');

            var taskEntry = $('<li class="row task-entry"></li>');
            var checkedColumn = $('<input type="checkbox" class="col-xs-1">');         
            var titleColumn = $('<div class="task-title col-xs-10">' + taskString + '</div>');
            
            checkedColumn.change(function(e){
                if(checkedColumn.prop("checked")){
                    titleColumn.addClass('deleted-text');
                }
                else{
                    titleColumn.removeClass('deleted-text');
                }
            });
            
            var deleteColumn = $('<span class="glyphicon glyphicon-trash pull-right task-delete"></span>');

            deleteColumn.on('click', function(e){
                deleteColumn.parent().remove();
            });

            taskEntry.append(checkedColumn);
            taskEntry.append(titleColumn);
            taskEntry.append(deleteColumn);

            taskList.append(taskEntry);

            clearInput(taskInput);
        }
        
        else{  
            $("#alertEmptyField").removeClass('hide');
            setTimeout(function() { $("#alertEmptyField").addClass('hide'); }, 1500);
        }
    });

});

var clearInput = function(input){
    input.val('');
};

var deleteTask = function(taskId){
    // it would be great to implement deletion this way;
};
