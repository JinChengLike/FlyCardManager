# -*- coding:utf-8 -*-
import MySQLdb
import time


class Card_Up():
    def __init__(self, id, username, doData, workName, workTime, planeType, planeNo, fixArea, fixPart, needPart,
                 needTools,
                 workDetail, prepareNotice, workNotice, workWay):
        self.id = str(id)
        self.username = username
        self.doData = doData
        self.workName = workName
        self.workTime = workTime
        self.planeType = planeType
        self.planeNo = planeNo
        self.fixArea = fixArea
        self.fixPart = fixPart
        self.needPart = needPart
        self.needTools = needTools
        self.workDetail = workDetail
        self.prepareNotice = prepareNotice
        self.workNotice = workNotice
        self.workWay = workWay
        self.creatdata = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.conn = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="jackjin820",
            db="flymanage",
            charset='utf8'
        )

    def _cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def _saveSql(self):
        temp = "update card set dodata ='" + self.doData + "',workname='" + self.workName + "',worktime='" + self.workTime + "',planetype='"
        temp = temp + self.planeType + "',planeno='" + self.planeNo + "',fixarea='" + self.fixArea + "',fixpart='" + self.fixPart + "',needpart='"
        temp = temp + self.needPart + "',needtools='" + self.needTools + "',workdetail='" + self.workDetail + "',preparenotice='"
        sql = temp + self.prepareNotice + "',worknotice='" + self.workNotice + "',workway='" + self.workWay + "' where id =" + self.id + ";"
        return sql

    def _sqltodo(self):
        sql = "update todo set username = 'chain', creattime ='" + self.creatdata + "',todotime='" + self.doData + "',status=0 where detail='" + self.id + "';"
        return sql

    def _delsql(self):
        sql = "delete from callback where id=" + self.id + ";"
        return sql

    def UpdateCardInfo(self):
        sql = self._saveSql()
        cur = self._cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return 0
        except Exception as e:
            print e
            self.conn.rollback()
            cur.close()
            return 1

    def UpdateTodoUser(self):
        sqltodo = self._sqltodo()
        cur = self._cursor()
        try:
            cur.execute(sqltodo)
            self.conn.commit()
            cur.close()
            return 0
        except Exception as e:
            print e
            self.conn.rollback()
            cur.close()
            return 1

    def DeleteCall(self):
        delsql = self._delsql()
        cur = self._cursor()
        try:
            cur.execute(delsql)
            self.conn.commit()
            cur.close()
            self.conn.close()
            return 0
        except Exception as e:
            print e
            self.conn.rollback()
            cur.close()
            self.conn.close()
            return 1