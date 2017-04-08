import MySQLdb
import json


class Margin():
    def __init__(self):
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

    def _getMarginTools(self):
        sql = "select * from tools;"
        return sql

    def _getMarginMateral(self):
        sql = "select * from material;"
        return sql

    def getMarginList(self):
        sql_1 = self._getMarginMateral()
        sql_2 = self._getMarginTools()
        cur = self._cursor()
        cur.execute(sql_1)
        rs_1 = cur.fetchall()
        cur.execute(sql_2)
        rs_2 = cur.fetchall()
        cur.close()
        self.conn.close()
        a = []
        for row in rs_1:
            a.append("%s,%s" % row)
        b = []
        for row in rs_2:
            b.append("%s,%s" % row)
        res = [a, b]
        return json.dumps(res)


if __name__ == "__main__":
    a = Margin().getMarginList()
    print a