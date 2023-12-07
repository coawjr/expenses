import pymysql

class expensesDAO:
    def __init__(self):
        self.sql = 'A'

    def alpine(self):
        db = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '1682619412460523',
        database = 'expenses',
        )
        return(db)

    def insert_sql(self,sql):
        self.sql = sql
        d = self.alpine()
        cursor = d.cursor()
        cursor.execute(self.sql)
        d.commit()
