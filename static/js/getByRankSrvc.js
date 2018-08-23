$(document).ready(function() {
  // Refreshes the form.
  $('#refresh').click(function() {
    // Erases HTML already existing in the form.
    $('#request').html("");
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








});
