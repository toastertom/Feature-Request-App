$(document).ready(function() {

  $('form').on('submit', function(event) {

    $.ajax({
      data : {
        title : $('#title').val(),
        description : $('#description').val(),
        target : $('#target').val(),
        client : $('#client').val(),
        category : $('#category').val()
        // priority = $('#priority').val()
      },
      type : 'POST',
      url : '/postservice'
    })
    .done(function(response) {
      if (response) {
        console.log(response);

      }
      else{
        console.log('fail');
      }
    });

    event.preventDefault();

  });


});
