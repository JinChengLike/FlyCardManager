import MySQLdb


class CardSearch():
    def __init__(self, id):
        self.id = id
        self.conn = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="jackjin820",
            db="flymanage",
            charset='utf8'
        )

    def _searchDetail(self):
        sql = "select * from card where id = '" + str(self.id) + "';"
        return sql

    def _cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def getDetail(self):
        sql = self._searchDetail()
        cur = self._cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        cur.close()
        self.conn.close()
        return rs


if __name__=="__main__":
    a = CardSearch(5)
    r =a.getDetail()
    print r