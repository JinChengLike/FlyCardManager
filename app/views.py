from app import app
from flask import render_template, jsonify, request
from app import login_model, getUser, card_models


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
    userid,uname,utype = new_getUser.getUserInfo_CallBack()
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
    userid = request.form["userId"]
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
    new_save = card_models.Card_Model(userid,doData,workName,workTime,planeType,planeNo,fixArea,fixPart,needPart,needTools,workDetail,prepareNotice,workNotice,workWay)
    result = new_save.SaveCardInfo()
    res = jsonify({"result":result})
    return res
