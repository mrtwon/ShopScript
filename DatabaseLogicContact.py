import DatabaseQuery

class DBContactClass:

    db = DatabaseQuery.MainDatabaseQuery()
    querySelect = "SELECT * FROM contact"
    queryDelete = "DELETE FROM contact"
    queryInsert = "INSERT INTO contact VALUES('{}')"

    def show(self):
        query = self.querySelect
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            return "☎️ Контакты оператора: "+row[0][0]
        return "Контактов нет."

    def delete(self):
        query = self.queryDelete
        self.db.queryDB(query)

    def add(self, contact):
        self.delete()
        query = self.queryInsert.format(contact)
        self.db.queryDB(query)
        return "✅ Новый адрес оператора {}".format(contact)