$(document).ready(function() {
    $("#btn-login").click(function() {
        $.post("/login",{
            username : $("#username").val(),
            password : $("#userpass").val()
        },
        function(data){
            if(data.result==0){
                localStorage.username = $("#username").val();
                window.location.href = "/list_main"
            }
            else{
                alert("账户密码错误");
            }
        })
    });
})




$(document).ready(function() {
    $("#btn-reg").click(function() {
        $.post("/register",{
            username : $("#uname").val(),
            password : $("#upass").val()
        },
        function(data){
            if(data.result==0){
                alert("注册成功，请重新登录");
                window.location.reload();
            }
            else{
                alert("注册失败，用户名已注册或用户名密码不规范");
            }
        })
    });
})

