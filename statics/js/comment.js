$(document).on('click', '.write-comment', function(){
    var review_id = $(this).data('id');
    var container = $(this).parents('.review-item').find('#comment-container-'+review_id);
    var url = '/comments/new/';
    if($('#comment-container-'+review_id+' > li:last-child').hasClass('input-comment')){
        $('#comment-container-'+review_id+' > li:last-child').remove();
    }
    $(container).append("<li class='collection-item avatar input-comment'></li>");
    $(".input-comment").load(url, function(){
        scrollToInput(review_id);
        $('.save-comment').data('url', url);
    });
});

var CURRENT = 0

$(document).on('click', '.save-comment', function(){
    var url = $(this).data('url');
    $(this).parents('.list-comment').load(url,{
        csrfmiddlewaretoken:$('#comment-area').data('csrf'),
        comment:$('#comment-area').find('textarea').val(),
        review:$(this).parents('.list-comment').data('id')
    });
});

$(document).on('click', '.edit-comment', function(){
    var comment_id = $(this).data('id');
    var review_id = $(this).parents('.list-comment').data('id');
    var container = $(this).parents('.review-item').find('#comment-container-'+review_id);
    var url = '/comments/'+comment_id+'/edit/';
    if($('#comment-container-'+review_id+' > li:last-child').hasClass('input-comment')){
        $('#comment-container-'+review_id+' > li:last-child').remove();
    }
    $(container).append("<li class='collection-item avatar input-comment'></li>");
    $(".input-comment").load(url, function(){
        scrollToInput(review_id);
        $('.save-comment').data('url', url);
    });
});

$(document).on('click', '.delete-comment', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf_token = $(this).data('csrf');
    var container = $(this).closest('.collection-item')
    if($('li:nth-last-child(-n+1)', $(this).parents('.list-comment')).hasClass('input-comment')){
        $(this).parents('.list-comment').find('.input-comment').remove();
    }
    $.ajax({
       url: '/comments/delete/',
       data: {csrfmiddlewaretoken: csrf_token, id: id},
       method: 'post',
       dataType: 'json',
       success: function(data){
            if(data.success == 1){
                container.remove();
            } else {
                alert("An error occurred while trying to delete this comment.\nPlease try again later.");
            }
       },
       error: function (xhr, ajaxOptions, thrownError) {
            alert("An error occurred while trying to delete this comment.\nPlease try again later.");
       }
    });
});

$(document).on('click', '.trigger-icon-modal', function(){
    CURRENT = $(this).parents('.list-comment').data('id');
    $('#modal-icon').find('.modal-content').load('/comments/emoticons/', function(){
        $('#modal-icon').openModal();
    });
});

$(document).on('click', '#modal-icon img', function(){
	var src = $(this).attr('src');
	var name = src.split("/").pop().split(".gif")[0];

	var textarea =  $('#comment-container-'+CURRENT).find('textarea');
	var cursorPos = $(textarea).prop('selectionStart');
    var value = $(textarea).val();
    var textBefore = value.substring(0,  cursorPos);
    var textAfter  = value.substring(cursorPos, value.length);

    $(textarea).val(textBefore + ":"+name+":" + textAfter);
});

function scrollToInput(review_id)
{
    $('html, body').animate({
        scrollTop: $("#comment-container-" + review_id).offset().top - 80
    }, 1000, function () {
        $("#comment-container-" + review_id + " textarea").focus();
    });
}