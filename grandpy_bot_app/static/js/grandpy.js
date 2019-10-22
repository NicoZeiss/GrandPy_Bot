

// var user_input = $('#user_input');
// var submit = $('#submit');

// $(document).ready(function() {
//   submit.on('click', function (e) {

//     e.preventDefault();

//     if (user_input()) {
//       $.ajax({
//         url: &SCRIPT_ROOT + '/question',
//         type: 'POST',
//         data: $('form').serialize(),

//         success: function() {
//           alert('Form was submitted')
//         };
//       });
//     }

//   });
// });

$(document).ready(function() {

  $('#myform').on('submit', function (e) {
    alert("submitted")
    e.preventDefault();
  });

});
