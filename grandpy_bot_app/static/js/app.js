
$(document).ready(function() {

  $('#myform').on('submit', function (e) {
  	e.preventDefault();

  	var user_input = $('#myform').serialize();
  	
  	$.ajax({
  		type: "POST",
  		url: "/question",
  		data: user_input,
  		success: function(data) {
  			alert(data);
  		}
  	});
    
  });

});
