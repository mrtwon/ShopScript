import DatabaseQuery
import DatabaseLogicAdminPanel
import sqlite3

class DBBuyDataClass:
    db = DatabaseQuery.MainDatabaseQuery()
    queryCreate = "CREATE TABLE buyData(qiwi integer, bitcoin text)"
    queryQiwiData = "SELECT qiwi FROM buyData"
    queryBitcoinData = "SELECT btc FROM buyData"
    queryUpdateQiwi = "UPDATE buyData SET qiwi = '{}'"
    queryUpdateBitcoin = "UPDATE buyData SET btc = '{}'"
    queryInsertQiwi = "INSERT INTO buyData(qiwi) VALUES('{}')"
    queryInsertBitcoin = "INSERT INTO buyData(bitcoin) VALUES({})"
    queryAlreadyQiwi = "SELECT qiwi FROM buyData"
    queryAlreadyBitcoin = "SELECT btc FROM buyData"
    def qiwiDataURL(self):
        query = self.queryQiwiData
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return row[0][0]
        return False
    def qiwiData(self):
        query = self.queryQiwiData
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            return row[0][0]
        return "Данных нет"
    def bitcoinData(self):
        query = self.queryBitcoinData
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            return row[0][0]
        return "Данных нет."
    def allDataBuy(self):
        qiwi = self.qiwiData()
        bitcoin = self.bitcoinData()
        answer = "&#129297 Список реквизитов &#129297\nQiwi : <b>{}</b>\nBitcoin: <b>{}</b>".format(
            qiwi,bitcoin)
        return answer
    def isAlreadyQiwi(self):
        query = self.queryAlreadyQiwi
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def isAlreadyBitcoin(self):
        query = self.queryAlreadyBitcoin
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def updateQiwi(self, message,newQiwiData):
        dbAdmin = DatabaseLogicAdminPanel.DBAdminPanelClass()
        if not 'qiwi.com' in newQiwiData:
            newQiwiData = "qiwi.com/n/{}".format(newQiwiData)
        query = self.queryUpdateQiwi.format(newQiwiData)
        if not 'https://' in newQiwiData:
            newQiwiData = "https://"+newQiwiData
        if(not self.isAlreadyQiwi()):
            query = self.queryInsertQiwi.format(newQiwiData)
        self.db.queryDB(query)
        return "✅ Новая ссылка на оплату: {}".format(newQiwiData)
    def updateBitcoin(self, message, newBitcoinData):
        dbAdmin = DatabaseLogicAdminPanel.DBAdminPanelClass()
        if (int(dbAdmin.checkRights(message.from_user.id)) == 2):
            return "У вас нет прав на такие вещи :("
        query = self.queryUpdateBitcoin.format(newBitcoinData)
        if(not self.isAlreadyBitcoin()):
            query = self.queryInsertBitcoin.format(newBitcoinData)
        self.db.queryDB(query)
        return "✅ Новый bitcoin адрес: <b>{}</b>".format(newBitcoinData)