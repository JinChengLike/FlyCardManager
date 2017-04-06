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
    }
    return a;
}