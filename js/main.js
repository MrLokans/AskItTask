$(document).ready(function(){
    var createTaskButton = $('#createTask');

    createTaskButton.on('click', function(e){
        taskString = $('.todo-input-text').val();

        var taskList = $('#task-list');

        var taskEntry = $('<li class="row task-entry"></li>');
        var checkedColumn = $('<input type="checkbox" class="col-xs-1">');
        var titleColumn = $('<div class="task-title col-xs-10">' + taskString + '</div>');
        var deleteColumn = $('<span class="glyphicon glyphicon-trash"></span>');

        deleteColumn.on('click', function(e){
            deleteColumn.parent().remove();
        });

        taskEntry.append(checkedColumn);
        taskEntry.append(titleColumn);
        taskEntry.append(deleteColumn);

        taskList.append(taskEntry);
    });

    var deleteTask = function(taskId){
        // it would be great to implement deletion this way;
    };
});