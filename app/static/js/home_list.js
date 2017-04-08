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
    if(localStorage.utype!=1){
        $("#confirm").hide();
    }
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
            else if(localStorage.utype == 3){
                html = html +"<dd class='c-id'>【"+ temp[4] + "】工卡等待执行 <a id='"+temp[4]+"' onclick='look(this)' data-toggle='modal' data-target='#login'>查看</a></dd>";
            }
        }
        $("dl").html(html);
    })
})

function look(t){
      var id = $(t).attr('id'); ;
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