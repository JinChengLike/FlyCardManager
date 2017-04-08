# -*- coding:utf-8 -*-
import MySQLdb


class Confirm():
    def __init__(self, id, type, name):
        self.id = id
        self.type = int(type)
        self.name = name
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

    def _confirm_Sql(self):
        if self.type == 2:
            sql = "update todo set status='1' where detail='" + self.id + "';"
        else:
            sql = "update todo set status='3' where detail='" + self.id + "';"
        return sql

    def _do_sql(self):
        if self.type == 2:
            sql = "update todo set status='2',username='" + self.name + "' where detail='" + self.id + "';"
        else:
            sql = "update todo set status='4',username='" + self.name + "' where detail='" + self.id + "';"
        return sql

    def confirm_do(self):
        sql = self._confirm_Sql()
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

    def confirm_over(self):
        sql = self._do_sql()
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


