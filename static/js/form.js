$(document).ready(function() {

  $('form').on('submit', function(event) {

    $.ajax({
      data : {
        title : $('#title').val(),
        description : $('#description').val(),
        target : $('#target').val(),
        client : $('#client').val(),
        category : $('#category').val(),
        rank : $('#rank').val()
      },
      type : 'POST',
      url : '/postservice'
    }).done(function(response) {
      if (response) {
        console.log(response);
        // Clears Form feilds on successful submital
        $('#form')[0].reset()
      }
      else{
        console.log('fail');
      }
    });

     event.preventDefault();


  });




});
