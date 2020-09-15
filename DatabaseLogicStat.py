import DatabaseQuery
import sqlite3
class DBStat:
    db = DatabaseQuery.MainDatabaseQuery()
    queryCreate = "CREATE TABLE stateUser(id integer, joinbuy integer)"
    queryJoinAlready = "SELECT * FROM stateUser WHERE id = {}"
    queryUpdateJoin = "INSERT INTO stateUser VALUES({},0)"
    queryJoinState = "SELECT id FROM stateUser"
    queryAllUser = "SELECT id FROM stateUser WHERE id NOT IN (SELECT id FROM admin)"
    def joinAlready(self, id):
        query = self.queryJoinAlready.format(id)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0

    def joinUpdate(self, id):
        query = self.queryUpdateJoin.format(id)
        self.db.queryDB(query)
    def join(self, id):
        if not self.joinAlready(id):
            self.joinUpdate(id)
    def joinStat(self):
        query = self.queryJoinState
        row = self.db.queryAndAnswerDB(query)
        return len(row)
    def listUser(self):
        row = self.db.queryAndAnswerDB(self.queryAllUser)
        list = []
        for id in row:
            list.append(id[0])
        return list