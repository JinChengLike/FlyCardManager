import MySQLdb


class login_model():
    def __init__(self,username,passwords):
        self.username = username
        self.passwords = passwords
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

    def _insert(self):
        sql = "insert into user (username,password) values ('" + self.username + "','" + self.passwords + "');"
        return sql

    def login_callback(self):
        sql = self._sql()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        if rs[2] == self.passwords:
            cur.close()
            self.conn.close()
            return 0
        else:
            cur.close()
            self.conn.close()
            return 1

    def register_callback(self):
        sql = self._insert()
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