# FlyCardManager
航班维修工卡系统

权限说明
1.工卡创建员
2.仓库管理员  仅一人
3.工卡执行员

步骤说明
0.工卡已创建，待仓库管理员确认执行
1.仓库管理员已确认，执行中
2.仓库管理员已准备完成，待执行员确认执行
3.执行员已确认，执行中
4.执行员执行完毕
6.执行员报反馈给了创建员，待创建员修改


待优化点
代码冗余问题，例如应当建立一个父类定义数据库相关创建，每一个执行类继承，可以增强代码复用能力


接口说明见views.py文件注释

设计技术
前端：HTML5+CSS+Javascript+Jquery+AJAX+Bootstrap
后端：Python + Mysql + flask

环境搭建：
1.安装python2.7
2.安装pip
3.安装python依赖pip install flask 和 MySQLdb
4.安装pycharm
5.安装mysql，并将用户名，密码，以及数据库名写入各个接口文件中


文件用途
框架文件
static 前端静态css+js文件
templates html模版文件 两个文件夹不要动！！！涉及flask框架
__init__.py app文件夹的初始化文件
views.py 路由文件，所有接口路由以及接口方法都在这个文件架中
run.py 运行文件

其余文件都是接口功能文件
call.py 实现问题反馈接口功能
card_models.py 工卡创建接口功能
cardSearch.py 工卡详情获取接口功能
confirm.py 执行确认或完成确认接口功能
getMargin.py 工具、航材余量获取
getUser.py 主页加载时，获取用户信息
login_model.py 注册登录接口功能
TodoList.py 主页获取待办事项功能
updateC.py 创建者根据反馈修改工卡并让工卡重新进入流程

功能流程
管理员创建-》仓库管理员确认-》仓库管理员执行-》操作员确认-》操作员执行-》工卡完成
    ^                                                  |
    |-----------------------------------------------问题反馈