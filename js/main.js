$(document).ready(function(){
    var createTaskButton = $('#create-task-btn');
    var inputText = $('input.todo-input-text');

    inputText.on('keydown', function(event){
        if(event.which == 13){
            addToDo();
        }
    });

    createTaskButton.on('click', addToDo);

});

var addToDo = function(){
    taskInput = $('.todo-input-text');
    taskString = taskInput.val();
    
    if(taskString !== ''){
        var taskList = $('#task-list');

        var taskEntry = $('<li class="task-entry"></li>');
        var checkedColumn = $('<input type="checkbox" class="col-xs-2 col-md-1 col-sm-1">');         
        var titleColumn = $('<div class="task-title col-xs-8 col-md-10 col-sm-10">' + taskString + '</div>');
        
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
}

var clearInput = function(input){
    input.val('');
};

var deleteTask = function(taskId){
    // it would be great to implement deletion this way;
};
