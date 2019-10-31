
// $(document).ready(function() {

//   $('#myform').on('submit', function (e) {
  	
//     e.preventDefault();

//     var userInput = $('#user_input');
//     var textInput = $('#user_input').val() + "";

//     displayQuestion(textInput);

//     $('#loading').show();
  	
//   	$.ajax({
//   		type: "POST",
//   		url: "/question",
//   		data: userInput,

//   	}).done(function(response) {
//       $('#map').hide();
//       userInput.val('');

//       displayAnswer(textInput, response['address_message'], response['wiki_message'], response['error'], response['error_message']);

//   		var lat = parseFloat(response['gmap_datas']['lat']);
//   		var lng = parseFloat(response['gmap_datas']['lng']);
//   		var name = response['gmap_datas']['name'];
//   		initMap(lat, lng, name);

//       $('#loading').hide();
//       $('#map').fadeIn(2000);
//   	});

//   });

// });


// function displayQuestion(textInput){
//   var userName = "Vous : ";
//   $('#chatbox ul').append('<li class="message">' + userName + textInput + '</li>');
// }


// // Display messages in the chatbox
// function displayAnswer(textInput, addressMess, infoMess, error, err_mess){
//   var botName = "GrandPy : ";
  
//   if (error == 0) {
//     $('#chatbox ul').append('<li class="message">' + botName + infoMess + '</li>');
//     $('#chatbox ul').append('<li class="message">' + botName + addressMess + '</li>');
//   }
//   else if (error != 0) {
//     $('#chatbox ul').append('<li class="message">' + botName + err_mess + '</li>');
//   }

// }





$(document).ready(function() {

  $('#myform').on('submit', function (e) {
    
    e.preventDefault();

    var userInput = $('#user_input');
    
    $.ajax({
      type: "POST",
      url: "/question",
      data: userInput,

    }).done(function(response) {
      userInput.val('');

      var lat = parseFloat("48.8583");
      var lng = parseFloat("2.2944");
      var name = "salut";
      initMap(lat, lng, name);

    });

  });

});


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
