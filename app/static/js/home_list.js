function handle_type(utype){
    var a;
    if(utype = 1){
        localStorage.utype = 1;
        a = "工单管理员";
        $("#show").hide();
        $("#doing").hide();
    }
    else if(utype = 2){
        localStorage.utype = 2;
        a = "仓库管理员";
    }
    else if(utype =3){
        localStorage.utype = 3;
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


$(document).ready(function(){
    var html = ""
    username = localStorage.username;
    $.post("/getUserTodo",{
        name:username
    },function(data){
        data = JSON.parse(data);
        for(var i = 0;i < data.length;i++){
            str = data[i]
            temp = str.split(",");
            if(localStorage.utype == 1){
                html = html + "<dd>【"+ temp[4] + "】工卡收到反馈</dd>";
            }
            else if(localStorage.utype == 2){
                html = html + "<dd>【"+ temp[4] + "】工卡需要准备航材</dd>";
            }
            else if(localStorage.utype == 3){
                html = html +"<dd>【"+ temp[4] + "】工卡等待执行</dd>";
            }
        }
        $("dl").html(html);
    })
})




