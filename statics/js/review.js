/**
 * Created by quynv on 14/03/2016.
 */
$(document).on('click', '#new-review', function(){
    var url = '/reviews/new/';
    $('#save-review').data('url', url);
    $('#modal-review').find('.modal-content').load(url, function(){
        $('#modal-review').openModal();
    });
});

$(document).on('click', '#save-review', function(){
    var url = $(this).data('url');
    $('#modal-review').find('.modal-content').load(url,{
        csrfmiddlewaretoken:$('#review-form').data('csrf'),
        review:$('#review-form').find('textarea').val(),
        rating:$('input[name=rating]:checked', '#review-form').val(),
        book:$('#modal-review').data('id')
    }, function(){
        $('#review-container').load('/reviews/' +$('#modal-review').data('id')+'/view/');
    });
});

$(document).on('click', '.delete-review', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf_token = $(this).data('csrf');
    var container = $(this).parents('.review-item');
    $.ajax({
       url: '/reviews/delete/',
       data: {csrfmiddlewaretoken: csrf_token, id: id},
       method: 'post',
       dataType: 'json',
       success: function(data){
            if(data.success == 1){
                container.remove();
            } else {
                alert("An error occurred while trying to delete this review.\nPlease try again later.");
            }
       },
       error: function (xhr, ajaxOptions, thrownError) {
            alert("An error occurred while trying to delete this review.\nPlease try again later.");
       }
    });
});

$(document).on('click', '.edit-review', function(){
    var id = $(this).data('id');
    var url = '/reviews/' + id + '/edit/'
    $('#save-review').data('url', url);
    $('#modal-review').find('.modal-content').load(url, function(){
        $('#modal-review').openModal();
    });
});