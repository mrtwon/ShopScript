import DatabaseQuery
import sqlite3
import random
class MainDBClass:
    db = DatabaseQuery.MainDatabaseQuery()
    queryCreateTable = "CREATE TABLE usrCode(id integer,refcode integer,enterkey integer)"
    queryCreateTableForSave = "CREATE TABLE usrData(id integer, useRef integer)"

    queryInsertKey = "INSERT INTO usrCode VALUES({},{},0)"
    queryInsertSaveRef = "INSERT INTO usrData VALUES({},{})"
    queryUpdate = "UPDATE usrCode SET enterkey = {} WHERE refcode = {}"

    queryStateRefCode = "SELECT useRef FROM usrData"
    queryCheckKey = "SELECT refcode FROM usrCode WHERE id = {}"
    queryCheckCountEnterKeyCode = "SELECT enterkey FROM usrCode WHERE refcode = {}"
    queryCheckCountEnterbyRefcode = "SELECT enterkey FROM usrCode WHERE refcode = {}"
    queryCheckRef = "SELECT * FROM usrCode WHERE refcode = {}"
    queryCheckUseRefCode = "SELECT * FROM usrData WHERE id = {} and useRef = {}"
    queryScam = "SELECT * FROM usrCode WHERE id = {} and refcode = {}"
    def createTable(self):
        query = self.createTable
        self.db.queryDB(query)
    def generateValueKey(self): #Генерация чисел для рефералки
        return random.randint(5000,55000)
    def isAlreadyKey(self, id): #Есть ли у пользователя реф код
        query = self.queryCheckKey.format(id)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def isUseRefCode(self,id,key): #Активировался ли этот реф код пользователем раньше
        query = self.queryCheckUseRefCode.format(id, key)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0
    def SaveActivateRefCode(self,id,key): # Сохранить активированный реф код
        query = self.queryInsertSaveRef.format(id, key)
        self.db.queryDB(query)
    def add (self, id): #Функция для выдачи пользователю его реф кода
                        #Если его нет - создается
        if(self.isAlreadyKey(id)):
            return self.showUserRefCode(id)
        key = self.generateValueKey()
        query = self.queryInsertKey.format(id,key)
        self.db.queryDB(query)
        return self.showUserRefCode(id)
    def UpdateEnterCode(self, key): # Обновить кол-во активаций у реф кода
        count = self.showMyRefEnter_REFCODE(key)
        count += 1
        query = self.queryUpdate.format(count, key)
        self.db.queryDB(query)

    def checkScam(self, id, ref):
        query = self.queryScam.format(id, ref)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0

    def update(self,id,key): #Функция для активации реф кода
        if self.checkScam(id, key):
            return "Вы не можете активировать свой код"
        if(not self.checkRef(key)):
            return "Такого кода не существует"
        if self.isUseRefCode(id,key):
            return "Данный код уже активирован"
        self.UpdateEnterCode(key)
        self.SaveActivateRefCode(id, key)
        return "Спасибо за активация кода ! Ждите призы :) "
    def checkRef(self,key): #Проверка на существование реф кода
        query = self.queryCheckRef.format(key)
        print(query)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0

    def showUserRefCode(self,id): # Вывод реф кода по id юзера
        query = self.queryCheckKey.format(id)
        row = self.db.queryAndAnswerDB(query)
        return row[0][0]
    def showMyRefEnter_ID(self,id): #Кол-во активаций реф кода у юзера(по id)
        conn = sqlite3.connect("sqlitedb.db")
        MY_REFCODE = self.showUserRefCode(id)
        query = self.queryCheckCountEnterKeyCode.format( MY_REFCODE )
        row = self.db.queryAndAnswerDB(query)
        return row[0][0]
    def showMyRefEnter_REFCODE(self,refcode):#Кол-во активаций реф кода у юзера(по реф коду)
        conn = sqlite3.connect("sqlitedb.db")
        query = self.queryCheckCountEnterbyRefcode.format(refcode)
        row = self.db.queryAndAnswerDB(query)
        return row[0][0]
    def countActivate(self):
        query = self.queryStateRefCode
        row = self.db.queryAndAnswerDB(query)
        return len(row)