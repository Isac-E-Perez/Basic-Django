$(document).ready(function(){
    $('.ui.dropdown') // its a selector, so needs to have a dot in the front and behind of ui (selecting by a class)
        .dropdown()

    $('.message .close')
    .on('click', function() {
        $(this)
        .closest('.message')
        .transition('fade')
        ;
    })
    ;
    
    $('#modal-btn').click(function(){
        $('.ui.modal')
        .modal('show')
        ;
    }) //id so # (class with a . like .ui.)
;
})
