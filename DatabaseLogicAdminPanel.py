import sqlite3
import DatabaseLogicProduct
import DatabaseQuery
import random
import DatabaseLogicJobs
import DatabaseLogicMarket
import DatabaseLogicStat
import KeybordClass
import DatabaseLogicReferalCode


class DBAdminPanelClass:
    db = DatabaseQuery.MainDatabaseQuery()
    NS = KeybordClass.NameSpace()
    queryCreate = "CREATE TABLE admin(id integer, uname text)"
    queryCreateRefAdmin = "CREATE TABLE adminRef(key integer, rights integer)"
    queryCheckAdmin = "SELECT * FROM admin WHERE id = {}"
    queryName = "SELECT uname FROM admin WHERE id = {}"
    queryAddAdmin = "INSERT INTO admin VALUES({},'{}',{})"
    queryRightsRefCode = "SELECT rights FROM adminRef WHERE key = {}"
    queryAdminRefCode = "SELECT key FROM adminRef WHERE key = {}"
    queryCheckAdminRights = "SELECT rights FROM admin WHERE id = {}"
    queryNametoID = "SELECT id FROM admin WHERE uname = '{}'"
    queryAllAdminPush = "SELECT id FROM admin"
    queryInsertAdminRefCode = "INSERT INTO adminRef VALUES({},{})"
    queryCountAdmin = "SELECT * FROM admin"
    queryRightsName = "SELECT rights FROM admin WHERE uname = '{}'"
    queryDelete = "DELETE FROM adminRef"
    queryDeleteAdmin = "DELETE FROM admin WHERE id = {}"
    queryAlready = "SELECT * FROM admin"
    queryCheckName = "SELECT * FROM admin where uname = '{}'"
    queryAllAdmin = "SELECT id, uname, rights FROM admin"
    def isAdmin(self, id):
        query = self.queryCheckAdmin.format(id)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def isName(self, id):
        query = self.queryName.format(id)
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            return row[0][0]
        return False
    def exportDB(self):
        file = open('sqlitedb.db', 'rb')
        return file
    def checkAlready(self):
        query = self.queryAlready
        row = self.db.queryAndAnswerDB(query)
        if(len(row) == 0):
            return True
        return False
    def checkName(self,name):
        try:
            userName = str(name)
        except:
            return False
        query = self.queryCheckName.format(userName)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def addDefaultAdmin(self,message):
        id = message.from_user.id
        name = message.chat.username
        query = self.queryAddAdmin.format(id, name, 0)
        self.db.queryDB(query)
    def welcome(self, id):
        if (self.isAdmin(id)):
            return self.NS.ANSWER_ADMIN_WELCOME.format(self.isName(id))

    def stateJoinActivate(self):
        db = DatabaseLogicStat.DBStat()
        answer = db.joinStat()
        return answer

    def stateRefActivate(self):
        db = DatabaseLogicReferalCode.MainDBClass()
        answer = db.countActivate()
        return answer

    def stateAll(self):
        dbProduct = DatabaseLogicProduct.DBProductClass()
        dbJob = DatabaseLogicJobs.DBJobClass()
        dbMarket = DatabaseLogicMarket.DBMarketClass()
        statMarket = dbMarket.countForStat()
        stateJoin = self.stateJoinActivate()
        stateRefActivate = self.stateRefActivate()
        statProduct = dbProduct.countProduct()
        stateCountAdmin = len(self.db.queryAndAnswerDB(self.queryCountAdmin))
        stateJobs = dbJob.getID()
        answer = self.NS.ANSWER_ADMIN_STAT.format(stateCountAdmin, stateJoin, stateRefActivate, stateJobs,statMarket[0],statMarket[1],statProduct)
        return answer
    def generateCode(self):
        return random.randint(10000,50000)
    def generateAdminRefCode(self, rights):
        if not len(rights) > 0:
            return
        id = self.generateCode()
        self.db.queryDB(self.queryInsertAdminRefCode.format(id,rights))
        return id

    def checkRights(self, id):
        row = self.db.queryAndAnswerDB(self.queryCheckAdminRights.format(id))
        if len(row) > 0:
            return row[0][0]
        return None
    def selfRights(self, id):
        print(id)
        rights = self.checkRights(id)
        print(rights)
        if rights == 2:
            print("start two")
            return "Вы гость.\n{} уровень доступа\n\nВам доступно только чтение информации.".format(rights)
        elif rights == 1:
            print("start one")
            return "Вы модератор.\n{} уровень доступа\n\nВам доступно чтение и изменение информации. Вы модете добавить пользователя уровня Гость(2 уровень)".format(rights)
        elif rights == 0:
            print("start zero")
            return "Вы администратор проекта.\n{} уровень доступа\n\nВы имеете все права администратора, считаетесь освнователем проекта, вам доступен весь функционал.".format(rights)
        if rights == False:
            print("start false")
            return "Ошибка. Не удалось найти ваши права"
    def isAlreadyAdminRefCode(self,key):
        query = self.queryAdminRefCode.format(key)
        print(query)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def addAdmin(self,message,key):
        if(not self.isAlreadyAdminRefCode(key) or self.isAdmin(message.from_user.id)):
            return False
        else:
            queryKey = self.queryRightsRefCode.format(key)
            id = message.from_user.id
            name = message.chat.username
            rights = self.db.queryAndAnswerDB(queryKey)[0][0]
            self.db.queryDB(self.queryAddAdmin.format(id, name, rights))
            self.db.queryDB(self.queryDelete)
            return True
    def adminNametoID(self,keyName):
        query = self.queryNametoID.format(keyName)
        print("query = {}",query)
        row = self.db.queryAndAnswerDB(query)
        print("adminNamtoID return {}",row[0][0])
        if len(row) > 0:
            return row[0][0]
        return "No data"
    def adminList(self):
        query = self.queryCountAdmin
        row = self.db.queryAndAnswerDB(query)
        list = "\n"
        for i in row:
            list += "Имя {} | Уровень доступа {}\n".format(i[1], i[2])
        return list
    def adminListMinimal(self):
        query = self.queryCountAdmin
        row = self.db.queryAndAnswerDB(query)
        list = []
        print(row)
        for i in row:
            print(i[1])
            list.append(i[1])
        list.append("ОТМЕНА")
        return list
    def nameToRights(self,keyName):
        query = self.queryRightsName.format(keyName)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return row[0][0]
        return "No data"
    def deleteAdmin(self,selfid,id):
        print("мой id = {}\n id удаляемого - {}".format(selfid,id))
        rightDelete = self.checkRights(id)
        selfRight = self.checkRights(selfid)
        if selfRight == 2:
            return False
        elif selfRight == 1 and rightDelete == 2:
            self.db.queryDB(self.queryDeleteAdmin.format(id))
            return True
        elif selfRight == 0:
            self.db.queryDB(self.queryDeleteAdmin.format(id))
            return True
    def writeListAdminAll(self):
        list = []
        query = self.queryAllAdminPush
        row = self.db.queryAndAnswerDB(query)
        for item in row:
            list.append(item[0])

        return list
    def allAdmin(self):
        query = "SELECT uname, rights FROM admin"
        row = self.db.queryAndAnswerDB(query)
        if not len(row) > 0:
            return "Список пуст."
        answer = ""
        for admin in row:
            name = admin[0]
            if name == "None": name = "Нет Никнейма"
            else:
                name = "@"+admin[0]
            answer += "📂 {} - {} уровень\n".format(name,admin[1])
        return answer
    def adminList(self):
        row = self.db.queryAndAnswerDB(self.queryAllAdmin)
        if len(row) > 0:
            return row
        else:
            return 0
    def onlyAllRights(self):
        list = []
        admin = self.db.queryAndAnswerDB("SELECT id FROM admin WHERE rights = 0")
        for id in admin:
            list.append(id[0])
        return list