# -*- coding:utf-8 -*-
import MySQLdb
import json

class TodoList():
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

    def _sqlList(self):
        sql = "select * from todo where username = '" + self.username + "';"
        return sql

    def _cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def getTodoList(self):
        sql = self._sqlList()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchall()
        cur.close()
        self.conn.close()
        a = []
        for row in rs:
            a.append("%s,%s,%s,%s,%s,%s" % row)
        return json.dumps(a)

