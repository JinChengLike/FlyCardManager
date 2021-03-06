$(document).ready(function(){
    $("#creat").hide();
    username = localStorage.username;
    $.post("/getUserInfo",{
        name:username
    },function(data){
        userId = data.userid;
        localStorage.userId = userId;
        type = data.utype;
        $("#uid").text(userId);
        $("#type").text(handle_type(type));
    })
})

$(document).ready(function(){
    var html = "";
    if(localStorage.utype!=3){
        $("#callback").hide();
        $("textarea").hide();
    }
    username = localStorage.username;
    $.post("/getTodoList",{
        username : username
    },function(data){
        data = JSON.parse(data);
        for(var i=0;i<data.length;i++){
            str = data[i]
            temp = str.split(",");
            if(temp[5] == 1 || temp[5]==3){
               temp[5] =handle_status(temp[5]);
               html = html + "<tr onclick='det(this)'><td class='no'>" + temp[4] +"</td><td>" + temp[2] + "</td><td>" + temp[3] + "</td><td>" + temp[1] + "</td><td class='status'>" + temp[5] +"</td><td><a data-toggle='modal' data-target='#todo'>查看</a></td></tr>";
            }
        }
        $("tbody").html(html);
    })
})


function det(t){
      var idx = $(t).index();
      a = "td.no:eq(" + idx + ")";
      status = "td.status:eq(" + idx + ")";
      status = $(status).text();
      no_list = $(a).text();
      $.post("/getCardDetail",{
           id:no_list
      },function(data){
          $("#c-no").text(data.id);
          $("#creat-data").text(data.creattime);
          $("#do-data").text(data.todotime);
          $("#creat-name").text(data.creatname);
          $("#do-name").text(data.workname);
          $("#plane-no").text(data.planeno);
          $("#fly-no").text(data.flyno);
          $("#fix-area").text(data.fixarea);
          $("#fix-part").text(data.fixpart);
          $("#need-part").text(data.needpart);
          $("#need-tools").text(data.needtools);
          $("#time").text(data.time);
          $("#work-detail").text(data.workdetail);
          $("#preapare-notice").text(data.preparenotix);
          $("#work-notice").text(data.worknotice);
          $("#work-way").text(data.workway);

      })
}

$(document).ready(function(){
    $("#confirm-btn").click(function(){
        $.post("/confirm_over",{
            id : $("#c-no").text(),
            utype : localStorage.utype,
            uname : $("#do-name").text()
        },function(data){
            if(data.result == 0){
                alert("执行已完成");
                $("#todo").modal('hide');
                window.location.reload();
            }
            else{
                alert("执行发生错误");
            }
        })
    })
})

$(document).ready(function(){
    $("#callback").click(function(){
        contant = $("textarea").val();
        if(contant==""){
            return 0
        }
        else{
            $.post('/callBack',{
                id: $("#c-no").text(),
                contant: contant,
                username: $("#creat-name").text()
            },function(data){
                if(data.result == 0){
                    alert("反馈已提交");
                    $("#todo").modal('hide');
                    window.location.reload();
                }
                else{
                    alert("执行发生错误");
                }
            })
        }
    })
})