$(document).ready(function() {
  // Refreshes the form.
  $('#refresh').click(function() {
    // Erases HTML already existing in the form.
    $('#request').html("");
    // Adds table header back after being deleted.
    $('#request').append(
      '<tr>' +
      '<th>ID</th>' +
      '<th>Title</th>' +
      '<th>Description</th>' +
      '<th>Target Completion</th>' +
      '<th>Client</th>' +
      '<th>Category</th>' +
      '<th>Priortiy</th>' +
      '<th>Date Submited</th>' +
      '</tr>'
    );
    $.get('/getservice', function(data){
      $.each(data, function(key, value){
        // Converts ranks numeric value into ranks name.
        var priority = value.rank.toString();

        if(priority === '3'){
          priority = 'low';
        }else if (priority === '2'){
          priority = 'medium';
        }else {
          priority = 'high';
        }

        $('#request').append(

          '<tr>' +
          '<td>'+ value.id + '</td>' +
          '<td>'+ value.title + '</td>' +
          '<td>'+ value.description + '</td>' +
          '<td>'+ value.target + '</td>' +
          '<td>'+ value.client + '</td>' +
          '<td>'+ value.category + '</td>' +
          '<td>'+ priority + '</td>' +
          '<td>'+ value.date + '</td>' +
          '</tr>'

        );
      });
    });
  });

  // Queries the database on page load.
    $.get('/getservice', function(data){
      console.log(data);
      $.each(data, function(key, value){

        // Converts ranks numeric value into ranks name.
        var priority = value.rank.toString();
        if(priority === '3'){
          console.log(true);
          priority = 'low';
        }else if (priority === '2'){
          priority = 'medium';
        }else {
          priority = 'high';
        }

        $('#request').append(
          '<tr>' +
          '<td>'+ value.id + '</td>' +
          '<td>'+ value.title + '</td>' +
          '<td>'+ value.description + '</td>' +
          '<td>'+ value.target + '</td>' +
          '<td>'+ value.client + '</td>' +
          '<td>'+ value.category + '</td>' +
          '<td>'+ priority + '</td>' +
          '<td>'+ value.date + '</td>' +
          '</tr>'
        );
      });
    });

    // Auto Refresh
    $('#btn').click(function() {
      // Adds a slight delay so the request isn't initialized before the data posts to the db...Not the best solution.
      setTimeout(function(){
      // Erases HTML already existing in the form.
      $('#request').html("");
      // Adds table header back after being deleted.
      $('#request').append(
        '<tr>' +
        '<th>ID</th>' +
        '<th>Title</th>' +
        '<th>Description</th>' +
        '<th>Target Completion</th>' +
        '<th>Client</th>' +
        '<th>Category</th>' +
        '<th>Priortiy</th>' +
        '<th>Date Submited</th>' +
        '</tr>'
      );
      $.get('/getservice', function(data){
        $.each(data, function(key, value){
          // Converts ranks numeric value into ranks name.
          var priority = value.rank.toString();

          if(priority === '3'){
            priority = 'low';
          }else if (priority === '2'){
            priority = 'medium';
          }else {
            priority = 'high';
          }

          $('#request').append(

            '<tr>' +
            '<td>'+ value.id + '</td>' +
            '<td>'+ value.title + '</td>' +
            '<td>'+ value.description + '</td>' +
            '<td>'+ value.target + '</td>' +
            '<td>'+ value.client + '</td>' +
            '<td>'+ value.category + '</td>' +
            '<td>'+ priority + '</td>' +
            '<td>'+ value.date + '</td>' +
            '</tr>'

          );
        });
      });
    }, 100);
    });


});
