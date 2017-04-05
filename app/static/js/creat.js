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
            userId : localStorage.userId,
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