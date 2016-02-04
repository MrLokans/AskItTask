$(document).ready(function(){
    var createTaskButton = $('#create-task-btn');
    var inputText = $('input.todo-input-text');
    
    inputText.on('keydown', function(event){
        if(event.which == 13){
            verifyToDo();
        }
    });

    createTaskButton.on('click', verifyToDo);

});

var verifyToDo = function(){
    taskInput = $('.todo-input-text');
    taskString = taskInput.val();
    
    if(taskString === '') {  
        $("#alertEmptyField").removeClass('hide');
        setTimeout(function(){
            $("#alertEmptyField").hide(250);
        }, 1500);
        // show method is called BEFORE the previous .hide() method. 
        $("#alertEmptyField").show(0);                 
    }
};

var clearInput = function(input){
    input.val('');
};

