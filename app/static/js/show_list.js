$(document).ready(function(){
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
    username = localStorage.username;
    $.post("/getTodoList",{
        username : username
    },function(data){
        data = JSON.parse(data);
        for(var i=0;i<data.length;i++){
            str = data[i]
            temp = str.split(",");
            html = html + "<tr onclick='det(this)'><td class='no'>" + temp[4] +"</td><td>" + temp[2] + "</td><td>" + temp[3] + "</td><td>" + temp[1] + "</td><td>" + temp[5] +"</td><td><a data-toggle='modal' data-target='#todo'>查看</a></td></tr>";
        }
        $("tbody").html(html);
    })
})


function det(t){
      var idx = $(t).index();
      a = "td.no:eq(" + idx + ")";
      no_list = $(a).text();
      $.post("/getCardDetail",{
           id:no_list
      },function(data){
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
