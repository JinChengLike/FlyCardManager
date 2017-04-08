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


$(document).ready(function() {
    $("#save").click(function() {
        $.post("/saveCardInfo",{
            username : localStorage.username,
            doData : $("#do-data").val(),
            workName : $("#work-name").val(),
            workTime : $("#work-time").val(),
            planeType : $("#plane-type").val(),
            planeNo : $("#plane-no").val(),
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
                alert("保存成功");
            }
        })
    })
})


$(document).ready(function() {
    $("#check").click(function(){
        var html="";
        $.get('/getMarginList',function(data){
            data = JSON.parse(data);
            material = data[0];
            tools = data[1];
            for(var i=0;i<material.length;i++){
                str = material[i]
                temp = str.split(",");
                html = html + "<label>" + temp[0] + "  " + temp[1] + "</label>&nbsp;&nbsp;";
            }
            $("#material-num").html(html);
            html = "";
            for(var i=0;i<tools.length;i++){
                str = tools[i]
                temp = str.split(",");
                html = html + "<label>" + temp[0] + "  " + temp[1] + "</label>&nbsp;&nbsp;";
            }
            $("#tools-num").html(html);
        })
        $("#showModel").modal('show');
    })
 })
