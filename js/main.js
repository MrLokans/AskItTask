$(document).ready(function(){
    var createTaskButton = $('#createTask');

    createTaskButton.on('click', function(e){
        taskString = $('.todo-input-text').val();

        var taskTable =$('#taskTable');

        var row = $('<tr></tr>');
        var firstCol = $('<td><input type="checkbox"></td>');
        var secondCol = $('<td>' + taskString + '</td>');
        var thirdCol = $('<td><span class="glyphicon glyphicon-star"></span></td>');

        row.append(firstCol);
        row.append(secondCol);
        row.append(thirdCol);

        taskTable.append(row);
    });
});