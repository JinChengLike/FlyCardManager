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
                html = html + "<dd class='c-id'>【"+ temp[4] + "】工卡收到反馈 <a id='"+temp[4]+"' onclick='look(this)' data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
            else if(localStorage.utype == 2){
                html = html + "<dd class='c-id'>【"+ temp[4] + "】工卡需要准备航材 <a id='"+temp[4]+"' onclick='look(this)' data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
            else if(localStorage.utype == 3 && temp[5]!=4){
                html = html +"<dd class='c-id'>【"+ temp[4] + "】工卡等待执行 <a id='"+temp[4]+"' onclick='look(this)' data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
        }
        $("dl").html(html);
    })
})


$(document).ready(function(){
    $("#confirm").click(function(){
        $.post("/updateCardInfo",{
            id : $("#card-id").text(),
            username : localStorage.username,
            doData : $("#do-data").val(),
            workName : $("#do-name").val(),
            workTime : $("#time").val(),
            planeType : $("#plane-no").val(),
            planeNo : $("#fly-no").val(),
            fixArea : $("#fix-area").val(),
            fixPart : $("#fix-part").val(),
            needPart : $("#need-part").val(),
            needTools : $("#need-tools").val(),
            workDetail : $("#work-detail").val(),
            prepareNotice : $("#prepare-notice").val(),
            workNotice : $("#work-notice").val(),
            workWay : $("#work-way").val()
        },function(data){
            if(data.result == 0){
                alert("修改已完成，已提交给工作人员");
                $("#todo").modal('hide');
            }
            else{
                alert("执行发生错误");
            }
        })

    })
})


function look(t){
      var id = $(t).attr('id');
      if(localStorage.utype!=1){
        $("#confirm").hide();
      }
      $("#card-id").text(id);
      if(localStorage.utype==1){
        $.post("/getCall",{
            id:id
        },function(data){
            alert(data.result);
        })
      }
      $.post("/getCardDetail",{
         id:id
      },function(data){
          $("#creat-data").val(data.creattime);
          $("#do-data").val(data.todotime);
          $("#creat-name").val(data.creatname);
          $("#do-name").val(data.workname);
          $("#plane-no").val(data.planeno);
          $("#fly-no").val(data.flyno);
          $("#fix-area").val(data.fixarea);
          $("#fix-part").val(data.fixpart);
          $("#need-part").val(data.needpart);
          $("#need-tools").val(data.needtools);
          $("#time").val(data.time);
          $("#work-detail").val(data.workdetail);
          $("#prepare-notice").val(data.preparenotix);
          $("#work-notice").val(data.worknotice);
          $("#work-way").val(data.workway);
      })

}