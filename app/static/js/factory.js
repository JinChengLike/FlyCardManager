function handle_type(utype){
    var a;
    if(utype == 1){
        localStorage.utype = 1;
        a = "工单管理员";
        $("#show").hide();
        $("#doing").hide();
    }
    else if(utype == 2){
        localStorage.utype = 2;
        a = "仓库管理员";
        $("#creat").hide()
    }
    else if(utype == 3){
        localStorage.utype = 3;
        a = "施工者";
        $("#creat").hide()
    }
    return a;
}


function handle_status(status){
    if(status==0){
        return "航材待准备"
    }
    else if(status==1){
        return "航材准备中"
    }
    else if(status==2){
        return "工卡待执行"
    }
    else if(status==3){
        return "工卡执行中"
    }
    else if(status==4){
        return "工卡已完成"
    }
    else if(status==6){
        return "工卡反馈中"
    }
}