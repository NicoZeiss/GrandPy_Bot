
$(document).ready(function() {

  $('#myform').on('submit', function (e) {
  	
    e.preventDefault();

    var userInput = $('#user_input');
    var textInput = $('#user_input').val() + "";
    var scrollMess = document.getElementById("chatbox");

    displayQuestion(textInput);
    scrollMess.scrollTop = scrollMess.scrollHeight;

    var loadIc = document.getElementById("loading");
    loadIc.style.visibility = "visible";
  	
  	$.ajax({
  		type: "POST",
  		url: "/question",
  		data: userInput,

  	}).done(function(response) {

      userInput.val('');

      displayAnswer(textInput, response['address_message'], response['wiki_message'], response['error'], response['error_message'], response['wiki_datas']['link']);
      scrollMess.scrollTop = scrollMess.scrollHeight;

      var objDiv = document.getElementById("chatbox");
      objDiv.scrollTop = objDiv.scrollHeight;

  		if (response['error'] == 0) {
        var lat = parseFloat(response['gmap_datas']['lat']);
        var lng = parseFloat(response['gmap_datas']['lng']);
        var name = response['gmap_datas']['name'];
        initMap(lat, lng, name);
        $('#map').hide();
        $('#map').fadeIn(2000);
    }

      loadIc.style.visibility = "hidden";
      
  	});

  });

});


function displayQuestion(textInput){
  var userName = "Vous : ";
  $('#chatbox ul').append('<li class="message">' + '<span class="names">' + userName + '</span>' + textInput + '</li>');
}


// Display messages in the chatbox
function displayAnswer(textInput, addressMess, infoMess, error, err_mess, link){
  var botName = "GrandPy : ";
  
  if (error == 0) {
    $('#chatbox ul').append('<li class="message">' + '<span class="names">' + botName + '</span>' + addressMess + '</li>');
    $('#chatbox ul').append('<li class="message">' + '<span class="names">' + botName + '</span>' + infoMess + '</li>');
    $('#chatbox ul').append('<li class="message">' + '<span class="names">' + botName + '</span>' + "Pour sen savoir plus, " + '<a href="' + link + '">Wikipedia</a>' + '</li>');
  }
  else if (error != 0) {
    $('#chatbox ul').append('<li class="message">' + '<span class="names">' + botName + '</span>' + err_mess + '</li>');
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
