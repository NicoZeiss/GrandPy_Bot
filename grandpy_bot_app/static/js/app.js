
$(document).ready(function() {

  $('#myform').on('submit', function (e) {
  	e.preventDefault();

  	var user_input = $('#user_input');
  	$('#loading').show();
  	
  	$.ajax({
  		type: "POST",
  		url: "/question",
  		data: user_input,

  	}).done(function(response) {
  		$('#loading').hide();
  		user_input.val('');
  		var lat = parseFloat(response['lat']);
  		var lng = parseFloat(response['lng']);
  		var name = response['name'];
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