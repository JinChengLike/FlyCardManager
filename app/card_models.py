# -*- coding:utf-8 -*-
import MySQLdb
import time

class Card_Model():
    def __init__(self,userId,doData,workName,workTime,planeType,planeNo,fixArea,fixPart,needPart,needTools,workDetail,prepareNotice,workNotice,workWay):
        self.userId = userId
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
        self.creatdata = time.strftime('%Y-%m-%d',time.localtime(time.time()))
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
        temp = "insert into card (userid,creatdata,dodata,workname,worktime,planetype,planeno,fixarea,fixpart"
        sql = temp + ",needpart,needtools,workdetail,preparenotice,worknotice,workway) values ("
        val_temp = sql + self.userId + ",'" + self.creatdata + "','" + self.doData + "','" + self.workName + "','" + self.workTime + "','" + self.planeType + "','"
        val = val_temp + self.planeNo + "','" + self.fixArea + "','" + self.fixPart + "','" + self.needPart + "','" + self.needTools + "','" + self.workDetail + "','" + self.prepareNotice + "','" + self.workNotice + "','" + self.workWay + "');"
        print val
        return val

    def SaveCardInfo(self):
        sql = self._saveSql()
        cur = self._cursor()
        try:
            cur.execute(sql)
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
