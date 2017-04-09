import MySQLdb


class Call():
    def __init__(self, id, content, username):
        self.id = str(id)
        self.content = content
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
        sql = "insert into callback values (" + self.id + ",'" + self.content + "');"
        return sql

    def _updatesql(self):
        sql = "update todo set status = 6,username = '" + self.username + "' where detail='" + self.id + "';"
        return sql

    def _delSql(self):
        sql = "delete from callback where id =" + self.id + ";"
        return sql

    def insert(self):
        sql = self._sql()
        u_sql = self._updatesql()
        cur = self._cursor()
        try:
            cur.execute(sql)
            cur.execute(u_sql)
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


class getCall():
    def __init__(self, id):
        self.id = str(id)
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
        sql = "select content from callback where id=" + self.id + ";"
        return sql

    def getCall(self):
        sql = self._sql()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        cur.close()
        self.conn.close()
        return rs[0]


if __name__ == "__main__":
    a = getCall(5).getCall()
    print a[0]