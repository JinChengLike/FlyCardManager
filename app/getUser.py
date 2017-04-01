import MySQLdb
import json

class getUser():
    def __init__(self, username):
        self.username = username
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

    def _sql(self):
        sql = "select * from user where username = '" + self.username + "';"
        return sql

    def _todo_sql(self):
        sql = "select * from todo where username = '" + self.username + "';"
        return sql

    def getUserInfo_CallBack(self):
        sql = self._sql()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        userid = rs[0]
        uname = rs[1]
        utype = rs[3]
        cur.close()
        self.conn.close()
        return userid, uname, utype

    def getTodo_CallBack(self):
        sql = self._todo_sql()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchall()
        cur.close()
        self.conn.close()
        return rs

    def getTodo(self):
        aa = getUser(self.username)
        f = aa.getTodo_CallBack()
        a = []
        for row in f:
            a.append("%s,%s,%s,%s,%s,%s" % row)
        return json.dumps(a)
