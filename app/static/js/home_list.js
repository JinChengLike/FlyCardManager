function handle_type(utype){
    var a;
    if(utype = 1){
        a = "工单管理员";
        $("#show").hide();
        $("#doing").hide();
    }
    else if(utype = 2){
        a = "仓库管理员";
    }
    else if(utype =3){
        a = "施工者";
    }
    return a;
}


$(document).ready(function(){
    username = localStorage.username;
    $("#username").text(username);
    $.post("/getUserInfo",{
        name:username
    },function(data){
        userId = data.userid;
        type = data.utype;
        $("#uid").text(userId);
        $("#type").text(handle_type(type));
    })
})





