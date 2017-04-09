from app import app
from flask import render_template, jsonify, request
from app import login_model, getUser, card_models, TodoList, cardSearch, confirm, getMargin, call, updateC


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/list_main')
def list_main():
    return render_template("home.html")


@app.route('/show')
def show():
    return render_template("show.html")


@app.route('/creat')
def creat():
    return render_template("creat.html")


@app.route('/doing')
def doing():
    return render_template("doing.html")


@app.route('/login', methods=['POST'])
def check_login():
    username = request.form["username"]
    passwords = request.form["password"]
    new_login = login_model.login_model(username=username, passwords=passwords)
    check_result = new_login.login_callback()
    res = jsonify({'result': check_result})
    return res


@app.route('/register', methods=['POST'])
def check_register():
    username = request.form["username"]
    passwords = request.form["password"]
    new_register = login_model.login_model(username=username, passwords=passwords)
    check_result = new_register.register_callback()
    res = jsonify({'result': check_result})
    return res


@app.route('/getUserInfo', methods=["POST"])
def getUserInfo():
    username = request.form["name"]
    new_getUser = getUser.getUser(username=username)
    userid, uname, utype = new_getUser.getUserInfo_CallBack()
    res = jsonify({'userid': userid, "uname": uname, "utype": utype})
    return res


@app.route('/getUserTodo', methods=["POST"])
def getUserTodo():
    username = request.form["name"]
    new_getTodo = getUser.getUser(username=username)
    res = new_getTodo.getTodo()
    return res


@app.route('/saveCardInfo', methods=["POST"])
def saveCardInfo():
    username = request.form["username"]
    doData = request.form["doData"]
    workName = request.form["workName"]
    workTime = request.form["workTime"]
    planeType = request.form["planeType"]
    planeNo = request.form["planeNo"]
    fixArea = request.form["fixArea"]
    fixPart = request.form["fixPart"]
    needPart = request.form["needPart"]
    needTools = request.form["needTools"]
    workDetail = request.form["workDetail"]
    prepareNotice = request.form["prepareNotice"]
    workNotice = request.form["workNotice"]
    workWay = request.form["workWay"]
    new_save = card_models.Card_Model(username, doData, workName, workTime, planeType, planeNo, fixArea, fixPart,
                                      needPart, needTools, workDetail, prepareNotice, workNotice, workWay)
    result = new_save.SaveCardInfo()
    res = jsonify({"result": result})
    return res


@app.route('/getTodoList', methods=["POST"])
def getTodoList():
    username = request.form["username"]
    new_TodoList = TodoList.TodoList(username)
    res = new_TodoList.getTodoList()
    return res


@app.route('/getCardDetail', methods=["POST"])
def getCardDetail():
    id = request.form["id"]
    new_search = cardSearch.CardSearch(id)
    result = new_search.getDetail()
    res = jsonify(
        {"id": result[0], "creatname": result[1], "creattime": result[2], "todotime": result[3], "workname": result[4],
         "time": result[5], "planeno": result[6], "flyno": result[7], "fixarea": result[8], "fixpart": result[9],
         "needpart": result[10], "needtools": result[11], "workdetail": result[12], "preparenotix": result[13],
         "worknotice": result[14], "workway": result[15]})
    return res


@app.route('/confirm_do', methods=["POST"])
def confirm_do():
    id = request.form["id"]
    type = request.form["utype"]
    name = request.form["uname"]
    new_confirm = confirm.Confirm(id, type, name)
    result = new_confirm.confirm_do()
    res = jsonify({"result": result})
    return res


@app.route('/confirm_over', methods=["POST"])
def confirm_over():
    id = request.form["id"]
    type = request.form["utype"]
    name = request.form["uname"]
    new_confirm = confirm.Confirm(id, type, name)
    result = new_confirm.confirm_over()
    res = jsonify({"result": result})
    return res


@app.route('/getMarginList', methods=["GET"])
def getMarginList():
    new_getMargin = getMargin.Margin().getMarginList()
    res = new_getMargin
    return res


@app.route('/callBack', methods=["POST"])
def callBack():
    id = request.form["id"]
    contant = request.form["contant"]
    username = request.form["username"]
    new_callBack = call.Call(id, contant, username).insert()
    result = new_callBack
    res = jsonify({"result": result})
    return res


@app.route('/getCall', methods=["POST"])
def getCall():
    id = request.form["id"]
    new_getCall = call.getCall(id).getCall()
    res = jsonify({"result": new_getCall})
    return res


@app.route('/updateCardInfo', methods=["POST"])
def updateCard():
    id = request.form["id"]
    username = request.form["username"]
    doData = request.form["doData"]
    workName = request.form["workName"]
    workTime = request.form["workTime"]
    planeType = request.form["planeType"]
    planeNo = request.form["planeNo"]
    fixArea = request.form["fixArea"]
    fixPart = request.form["fixPart"]
    needPart = request.form["needPart"]
    needTools = request.form["needTools"]
    workDetail = request.form["workDetail"]
    prepareNotice = request.form["prepareNotice"]
    workNotice = request.form["workNotice"]
    workWay = request.form["workWay"]
    new_updateCard = updateC.Card_Up(id, username, doData, workName, workTime, planeType, planeNo, fixArea,
                                     fixPart, needPart, needTools, workDetail, prepareNotice, workNotice, workWay)
    result_1 = new_updateCard.UpdateCardInfo()
    result_2 = new_updateCard.UpdateTodoUser()
    result_3 = new_updateCard.DeleteCall()
    if (result_1 == 0 and result_2 == 0 and result_3 == 0):
        result = 0
    else:
        result = 1
    res = jsonify({"result": result})
    return res
