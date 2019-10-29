
$(document).ready(function() {

  $('#myform').on('submit', function (e) {
  	
    e.preventDefault();

    var userInput = $('#user_input');
    var textInput = $('#user_input').val() + "";

    displayQuestion(textInput);

    $('#loading').show();
  	
  	$.ajax({
  		type: "POST",
  		url: "/question",
  		data: userInput,

  	}).done(function(response) {
      $('#map').hide();
      userInput.val('');

      displayAnswer(textInput, response['address'], response['wikinfo'], response['error']);

  		var lat = parseFloat(response['lat']);
  		var lng = parseFloat(response['lng']);
  		var name = response['name'];
  		initMap(lat, lng, name);

      $('#loading').hide();
      $('#map').fadeIn(2000);
  	});

  });

});


function displayQuestion(textInput){
  var userName = "Vous : ";
  $('#chatbox ul').append('<li class="message">' + userName + textInput + '</li>');
}


// Display messages in the chatbox
function displayAnswer(textInput, addressMess, infoMess, error){
  var botName = "GrandPy : ";

  if (error == 0) {
    $('#chatbox ul').append('<li class="message">' + botName + addressMess + '</li>');
    $('#chatbox ul').append('<li class="message">' + botName + infoMess + '</li>');
  }

  else if (error == 1) {

  }

  else if (error == 2) {

  }

}

// init GMaps and Marker
function initMap(lat, lng, name){
	var myLatLng = {lat: lat, lng: lng};
	var map = new google.maps.Map(document.getElementById('map'), {
		center: myLatLng,
		zoom:15
	});
	var marker = new google.maps.Marker({
		position: myLatLng,
		map: map,
		title: name
	});
}
