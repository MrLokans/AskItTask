$(document).ready(function(){
    var createTaskButton = $('#createTask');

    createTaskButton.on('click', function(e){
        taskString = $('.todo-input-text').val();

        var taskList = $('#task-list');

        var content = $('<tr></tr>');
        var checkedColumn = $('<input type="checkbox" class="col-xs-1">');
        var titleColumn = $('<div class="task-title col-xs-10">' + taskString + '</div>');
        var deleteColumn = $('<span class="glyphicon glyphicon-trash"></span>');

        taskEntry.append(checkedColumn);
        taskEntry.append(titleColumn);
        taskEntry.append(deleteColumn);

        taskList.append(taskEntry);
    });
});