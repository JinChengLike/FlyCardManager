$(document).ready(function(){
    username = localStorage.username;
    $("#uname").text(username);
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
                html = html + "<dd>【"+ temp[4] + "】工卡收到反馈 <a data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
            else if(localStorage.utype == 2){
                html = html + "<dd>【"+ temp[4] + "】工卡需要准备航材 <a data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
            else if(localStorage.utype == 3){
                html = html +"<dd>【"+ temp[4] + "】工卡等待执行 <a data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
        }
        $("dl").html(html);
    })
})




