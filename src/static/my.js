// $("#register-btn").click(function () {
//
//     email = $("#email")[0].value
//     username = $("#username")[0].value
//     password = $("#password")[0].value
//
//     $.ajax({
//         url: "register",
//         method: "POST",
//         // The key needs to match your method's input parameter (case-sensitive).
//         // data: JSON.stringify({"email":email, "password":password }),
//         data: {"username":username, "email":email, "password":password },
//         // contentType: "application/x-www-form-urlencoded",
//         // dataType: "json",
//         success: function(data){
//             // $("#signup-error").empty()
//             // if (data.error) {
//             //     $("#signup-error").append(data.error)
//             // }
//             // else {
//             //     window.location = "/auth/signin"
//             // }
//                 window.location = "login"
//
//         },
//         failure: function(errMsg) {
//             alert(errMsg);
//         }
//     });
// })

// $('#file-button').click(function(){
//   var files = $('#InputFile').prop('files');
//
//   var data = new FormData();
//   data.append('file', files[0]);
//
//   $.ajax({
//       url: '/upload',
//       type: 'POST',
//       data: data,
//       cache: false,
//       processData: false,
//       contentType: false
//   });
// });


$(document).ready(function(){
  // $('#userinfo_d').click(function(){
    // user
    if($('#is_admin').val() == "True"){
      $('#is_admin').prop('checked', 'checked');
    }else{
      $('#is_admin').removeProp('checked');
    }
    if($('#is_lock').val() == "True"){
      $('#is_lock').prop('checked', 'checked');
    }else{
      $('#is_lock').removeProp('checked');
    }
    // article
    // console.log("==>", $('#is_public').val())
    if($('#is_public').val() == "True"){
      $('#is_public').prop('checked', 'checked');
    }else{
      $('#is_public').removeProp('checked');
    }
  // });
});
