import sqlite3
class MainDatabaseQuery:
    filename = "sqlitedb.db"
    def queryAndAnswerDB(self, query):
        conn = sqlite3.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row
    def queryDB(self,query):
        print(query)
        conn = sqlite3.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()