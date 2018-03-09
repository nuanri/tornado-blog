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
