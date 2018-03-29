function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

//注册发送验证码
$( "#get-authcode-bt" ).one("click", function() {
    // $(this).unbind("click");
    console.log("111111")
    // console.log("====>",JSON.stringify({"email": $("#email")[0].value }))
    email =  $("#email")[0].value

    $.ajax({
        url: "auth/sms",
        method: "POST",
        data: JSON.stringify({"email": $("#email")[0].value }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){
            console.log("22222")
            console.log("data===>", data)
            $("#reg-error-ajax").empty()
            if (data.error)
                $("#reg-error-ajax").append(data.error)
            if (data.success)
                $("#reg-error-ajax").empty()
                $("#reg-error-ajax").append(data.success)
                // $("#authcode")[0].value = data.authcode
        },
        failure: function(errMsg) {
            console.log("errMsg ==>", errMsg)
            alert(errMsg);
        }
    });
})



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

    // $('.dropdown-item').click(function () {
    //     $('.dropdown-item').removeClass('active');
    //     $(this).addClass('active')
    // })
});

//加载后自动执行
$(function() {

    // 设置图口高度，此处让 footer 自动填高
    // $(window).resize(function() {
    //     $('div:last').height($(window).height() - $('div:last').offset().top);
    // });
    // $(window).resize();

    // 修改所有外链接的打开方式：在浏览器的新窗口中打开
    $(document.links).filter(function() {
        return this.hostname != window.location.hostname;
    }).attr('target', '_blank');

});


$(document).ready(function() {

 // var docHeight = $(window).height();
 // var footerHeight = $('footer').height();
 // var footerTop = $('footer').position().top + footerHeight;
 //
 // if (footerTop < docHeight) {
 //  $('footer').css('margin-top', 10 + (docHeight - footerTop - 106) + 'px');
 // }

//  if ($(document.body).height() < $(window).height()) {
//   $('footer').attr('style', 'position: fixed!important; bottom: 0px;');
// }

    // body的padding为56,所以减去56
    if ($(window).height() > $('body').height())
        {
        var extra = $(window).height() - $('body').height() - 56;
        $('footer').css('margin-top', extra);
        }
});
