from app import app
from flask import render_template, jsonify, request
from app import login_model, getUser


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


@app.route('/register',methods=['POST'])
def check_register():
    username = request.form["username"]
    passwords = request.form["password"]
    new_register = login_model.login_model(username=username, passwords=passwords)
    check_result = new_register.register_callback()
    res = jsonify({'result': check_result})
    return res


@app.route('/getUserInfo',methods=["POST"])
def getUserInfo():
    username = request.form["name"]
    new_getUser = getUser.getUser(username=username)
    userid,uname,utype = new_getUser.getUserInfo_CallBack()
    res = jsonify({'userid': userid, "uname": uname, "utype": utype})
    return res