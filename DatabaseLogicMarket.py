import DatabaseQuery
import DatabaseLogicProduct
import sqlite3


class DBMarketClass:
    queryCreatArea = "CREATE TABLE area(id integer primary key, city text, area text)"
    query = "SELECT name FROM city"
    queryisAlreadyCity = "SELECT * FROM city WHERE name = '{}'"
    queryListArea = "SELECT area FROM area"
    queryListAreaCity = "SELECT area FROM area WHERE city = '{}'"
    queryisAlreadyArea = "SELECT * FROM area WHERE area = '{}'"
    queryInfoArea = "SELECT city, area FROM area WHERE area = '{}'"
    queryIDcity = "SELECT id FROM city WHERE name = '{}'"
    queryNameCity = "SELECT name FROM city WHERE id = {}"
    queryAddCity = "INSERT INTO city(name,many) VALUES('{}',0)"
    queryAddArea = "INSERT INTO area(city,area) VALUES('{}','{}')"
    queryAllArea = "SELECT area FROM area WHERE city = '{}'"
    queryDeleteCity = "DELETE FROM city WHERE name = '{}'"
    queryDeleteAreaByCity = "DELETE FROM area WHERE city = '{}' and area = '{}'"
    quertyDeleteAllCity = "DELETE FROM area WHERE city = '{}'"
    queryCountArea = "SELECT count(*) FROM area"
    queryGetIDsProductArea = "SELECT productID FROM area WHERE id = {}"
    queryGetInfoArea = "SELECT city, area FROM area WHERE id = {}"
    queryUpdateCash = "UPDATE city SET many = {} + (SELECT many FROM city WHERE id = {}) WHERE id = {}"
    queryConver = "SELECT cost FROM product WHERE id = {} UNION SELECT id FROM city WHERE name = (SELECT city FROM area WHERE id = {})"
    querySum = "SELECT SUM(many) FROM city"
    querySumCity = "SELECT name, many FROM city ORDER BY many DESC"
    queryAllCity = "SELECT COUNT(*) FROM city"
    db = DatabaseQuery.MainDatabaseQuery()
    def staticAllCity(self):
        list = ""
        for item in self.db.queryAndAnswerDB(self.querySumCity):
            list += "📈 <b>{}</b>:  <b>{}₽</b>\n".format(item[0],item[1])

        return list
    def sumCash(self):
        return self.db.queryAndAnswerDB(self.querySum)[0][0]
    def statisticMarket(self):
        if not int(self.db.queryAndAnswerDB(self.queryAllCity)[0][0]) > 0:
            return "Нет городов."
        answer_o = "\n🏆 За всё время: <b>{}₽</b>".format(self.sumCash())
        answer_t = "\n\nСтатистика по городам:\n\n{}".format(self.staticAllCity())
        result = answer_o+answer_t
        return result
    def addCashCity(self, ProductID, AreaID):
        result = self.converToAddCash(ProductID, AreaID)
        print("cash = {} and id city = {}".format(result[0],result[1]))
        query = self.queryUpdateCash.format(result[1], result[0], result[0])
        print(query)
        self.db.queryDB(query)

    def converToAddCash(self, ProductID, AreaID):
        row = self.db.queryAndAnswerDB(self.queryConver.format(
            ProductID, AreaID
        ))
        if len(row) > 0:
            print(row)
            return [str(row[0]).replace(',',''), str(row[1]).replace(',','')]

    def productIDsByArea(self, idArea):
        query = self.queryGetIDsProductArea.format(idArea)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0 and row[0][0] != None:
            print(row[0][0].split(','))
            return row[0][0].split(',')
        return ""

    def getInfoArea(self, AreaID):
        query = self.queryGetInfoArea.format(AreaID)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return [row[0][0], row[0][1]]
        return 0

    def countArea(self):
        row = self.db.queryAndAnswerDB(self.queryCountArea)
        return row[0][0]

    def countForStat(self):
        list = []
        queryCity = "SELECT * FROM city"
        queryArea = "SELECT * FROM area"
        row = self.db.queryAndAnswerDB(queryCity)
        row2 = self.db.queryAndAnswerDB(queryArea)
        list.append(len(row))
        list.append(len(row2))
        return list

    def listCity(self):
        list = []
        query = self.query
        row = self.db.queryAndAnswerDB(query)
        for city in row:
            list.append(city[0])
        return list

    def countCity(self):
        query = self.query
        row = self.db.queryAndAnswerDB(query)
        return len(row)

    def listArea(self):
        list = []
        query = self.queryListArea
        row = self.db.queryAndAnswerDB(query)
        if (len(row) > 0):
            for i in row:
                list.append(i[0])
        else:
            return "Нет данных."
        return list

    def isAlreadyCityCheck(self, city):
        city = city.lower()
        listCity = self.listCity()
        for item in listCity:
            if city == item.lower(): return False
        return True

    def isAlreadyCity(self, city):
        query = self.queryisAlreadyCity.format(city)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return True
        return False

    def isAlreadyArea(self, area):
        query = self.queryisAlreadyArea.format(area)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return len(row)
        return 0

    def isAlreadyAreaByCallback(self, area):
        try:
            index = area.index('|')
        except:
            return
        area = area[0:index]
        print(area)
        query = self.queryisAlreadyArea.format(area)
        row = self.db.queryAndAnswerDB(query)
        return len(row) > 0

    def indexCity(self, area):
        print("Index city nud = {}".format(area))
        answer = area[area.index('|') + 1:len(area)]
        print("Index city parse = {}".format(answer))
        return answer

    def areaInfo(self, area):
        list = []
        query = self.queryInfoArea.format(area)
        row = self.db.queryAndAnswerDB(query)
        if (len(row) > 0):
            list.append(row[0][0])
            list.append(row[0][1])
            return list

    def listAreaForCity(self, city):
        if not self.isAlreadyCity(city):
            return False
        query = self.queryListAreaCity.format(city)
        row = self.db.queryAndAnswerDB(query)
        if len(row) == 0:
            return False
        list = []
        for area in row:
            list.append(area[0])
        return list

    def getIdCity(self, city):
        query = self.queryIDcity.format(city)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return row[0][0]
        return False

    def getIdArea(self, city, area):
        print("getIdArea: city: {} area: {}".format(city, area))
        query = "SELECT id FROM area WHERE city = '{}' AND area = '{}'".format(city, area)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            print("ID area[{}] = {}".format(area, row[0][0]))
            return row[0][0]
        return 0

    def getNameCity(self, id):
        query = self.queryNameCity.format(id)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return row[0][0]
        return False

    def nudAreaName(self, area):
        return area[0:area.index('|')]

    def addCity(self, city):
        query = self.queryAddCity.format(city)
        self.db.queryDB(query)
        return "✅ Новый город: {}".format(city)

    def addArea(self, city, area):
        query = self.queryAddArea.format(city, area)
        self.db.queryDB(query)
        return "📜  Новый район для <b>{}</b>:\n\n🏙  <b>{}</b>".format(city, area)

    def addAreaList(self, city, areaList):
        print(areaList)
        areaList = areaList.split('\n')
        answerList = "📜  Новые районы для <b>{}</b>:\n\n".format(city)
        for i in areaList:
            answerList += "         🏙  <b>{}</b>\n".format(i)
        for item in areaList:
            query = self.queryAddArea.format(city, item)
            self.db.queryDB(query)
        return answerList

    def listAllArea(self, city):
        query = self.queryAllArea.format(city)
        area = self.db.queryAndAnswerDB(query)
        if not len(area) > 0:
            return "\n🏙  {}\n         🏬 Нет районов\n\n".format(city)
        list = "\n🏙  {}:\n".format(city)
        for item in area:
            list += "         🏬 {}\n".format(item[0])
        return list

    def listAll(self):
        listCity = self.listCity()
        count = len(listCity)
        if not count > 0:
            return "Нет городов"
        list = "📂 Все Территории\n📚  Полный список\n"
        print("list city = {}".format(listCity))
        for item in listCity:
            list += self.listAllArea(item)

        return list

    def deleteCity(self, city):
        query_n = self.queryDeleteCity.format(city)
        query_t = self.quertyDeleteAllCity.format(city)
        self.db.queryDB(query_n)
        self.db.queryDB(query_t)
        return True

    def deleteArea(self, city, area):
        query = self.queryDeleteAreaByCity.format(city, area)
        self.db.queryDB(query)
        return True
