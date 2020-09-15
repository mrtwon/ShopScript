import sqlite3
import DatabaseQuery
import random
import DatabaseLogicMarket
class DBProductClass:
    db = DatabaseQuery.MainDatabaseQuery()
    dbMarket = DatabaseLogicMarket.DBMarketClass()
    query = "SELECT name, cost, wight FROM product"
    queryAll = "SELECT id, name, wight, cost FROM product"
    queryInsert = "INSERT INTO product(name, cost, wight) VALUES('{}',{},'{}')"
    queryInfoByID = "SELECT * FROM product WHERE id = {}"
    queryDataBuy = "SELECT name, cost, wight FROM product WHERE id = {}"
    queryDelete = "DELETE FROM product WHERE id = {}"
    queryAllDelete = "DELETE FROM product"
    queryAllInfoByID = "SELECT name, cost, wight FROM product WHERE id = {}"
    queryNullArea = "SELECT id FROM area WHERE productID IS NULL"
    querySale = "UPDATE product SET cost = cost - (cost/100)*{}"

    def sale(self,m_cash):
        self.db.queryDB(self.querySale.format(m_cash))
    def productDeleteAll(self):
        self.db.queryDB(self.queryAllDelete)
    def productInfoForBuy(self, idProduct):
        print(idProduct)
        row = self.db.queryAndAnswerDB(self.queryAllInfoByID.format(idProduct))
        if len(row) > 0:
            return [str(row[0][0])+" "+str(row[0][2]), row[0][1]]
        return None
    def productInfo(self, id):
        query = self.queryAllInfoByID.format(id)
        row = self.db.queryAndAnswerDB(query)
        if len(row) > 0:
            return "{} {} {}₽".format(row[0][0], row[0][2], row[0][1])
        return 0
    def listDelete(self):
        row = self.db.queryAndAnswerDB(self.queryAll)
        return row
    def cost(self):
        print("activate cost_middle")
        list_p = ["Шишки HQ\n0.5/1/2\n900/1300/1900\nгр", "Гашиш EURO\n0.5/1/2/3\n750/1100/1600/2000\nгр",
                  "Гашиш Марокко\n0.5/1/3\n950/1500/2800\nгр",
                  "Амф. Белый\n1/2/3\n1100/1700/2550\nгр", "Амф. Розовый\n1/2/3\n800/1400/2200\nгр",
                  "MDMA\n1/2/3\n800/1300/1700\nтаб", "LSD Марки\n1/2/3\n1100/1650/2250\nшт",
                  "Героин\n0.5/1/2\n2800/5200/7500\nгр",
                  "Xanax USA\n10/25/50\n1300/2850/4200\nшт", "Мефедрон\n0.25/0.5/1\n1200/1900/2700\nгр",
                  "Метадон\n0.5/1/2\n1900/2800/3700\nгр"]
        return list_p
    def addProducts(self,lid):
        dc = 0
        lid = str(lid)
        if lid in '0':
            pass
        if lid in '1':
            dc += 200
        if lid in '2':
            dc += 350
        if not lid in ['0','1','2']:
            return False
        print("step1")
        list = self.cost()
        self.productDeleteAll()
        for item in list:
            print("step2")
            name = item.split('\n')[0]
            cost = item.split('\n')[2].split('/')
            gm = item.split('\n')[3]
            weight = item.split('\n')[1].split('/')
            i = 0
            while len(cost) > i:
                query = "INSERT INTO product(name, cost, wight) VALUES('{}','{}','{}')".format(
                    name, int(cost[i])+dc, weight[i] + " " + gm)
                self.db.queryDB(query)
                i += 1
        return True

    def addProductID(self,areaID, productIDs):
        query = "UPDATE area SET productID = '{}' WHERE id = {}".format(
            productIDs,areaID
        )
        self.db.queryDB(query)
    def listAreaID(self):
        answer = []
        row = self.db.queryAndAnswerDB("SELECT id FROM area")
        for i in row:
            answer.append(i[0])
        return answer
    def listAreaIDNull(self):
        answer = []
        row = self.db.queryAndAnswerDB(self.queryNullArea)
        for i in row: answer.append(i[0])
        return answer
    def listProductID(self):
        answer = []
        row = self.db.queryAndAnswerDB("SELECT id FROM product")
        for i in row:
            answer.append(i[0])
        return answer

    def randomID(self,listID):
        answer = "{}".format(random.choice(listID))
        i = 0
        count = 4
        while count > i:
            rnd = random.choice(listID)
            if str(rnd) in answer:
                continue
            answer += ",{}".format(rnd)
            i += 1
        return answer
    def randomProduct(self):
        if self.countProduct() == 0:
            return "⚠️ Нет товаров."
        if self.dbMarket.countArea() == 0:
            return "⚠️ Нет районов."
        AreaIDs = self.listAreaID()
        ProductIDs = self.listProductID()
        for item in AreaIDs:
            newIDs = self.randomID(ProductIDs)
            self.addProductID(item, newIDs)
        return "✅ Успешно."
    def randomProductForNull(self):
        if self.dbMarket.countArea() == 0:
            return "⚠️ Нет районов."
        if self.countProduct() == 0:
            return "⚠️ Нет товаров."
        AreaIDs = self.listAreaIDNull()
        ProductIDs = self.listProductID()
        for item in AreaIDs:
            newIDs = self.randomID(ProductIDs)
            self.addProductID(item, newIDs)
        return "✅ Успешно."
    def checkID(self,id):
        try:
            row = self.db.queryAndAnswerDB(self.queryInfoByID.format(id))
            return len(row) > 0
        except:
            pass
    def countProduct(self):
        query = "SELECT count(*) FROM product"
        row = self.db.queryAndAnswerDB(query)
        print(row[0][0])
        return row[0][0]
    def productShowID(self, id):
        listProduct = ""
        query = self.queryInfoByID.format(id)
        row = self.db.queryAndAnswerDB(query)
        if (len(row) > 0):
            for product in row:
                listProduct += "&#128465; {} {} ₽ - {}\n".format(product[1], product[2], product[3])
        else:
            listProduct = "Нет товара с таким IDs"
        return listProduct
    def productDataShop(self, id):
        if not self.checkID(id):
            return "Такого товара нет"
        query = self.queryDataBuy.format(id)
        row = self.db.queryAndAnswerDB(query)
        if not len(row) > 0:
            return
        list = [row[0][0], row[0][1], row[0][2]]
        return list
    def productShow(self):
        listProduct = ""
        query = self.query
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            for product in row:
                listProduct += "&#9999; {} ( {}₽ - {})\n\n".format(product[0],product[1],product[2])
        else:
            listProduct = "Товаров нет."
        return listProduct
    def productAll(self):
        listProduct = ""
        query = self.queryAll
        row = self.db.queryAndAnswerDB(query)
        if(len(row) > 0):
            for product in row:
                listProduct += "✏️ ID {} {} ( {} - {}₽)\n\n".format(product[0],product[1],product[2],product[3])
        else:
            listProduct = "Товаров нет."
        return listProduct
    def productForInlineKebord(self):
        query = self.queryAll
        row = self.db.queryAndAnswerDB(query)
        return row
    def isAlready(self):
        query = "SELECT * FROM product"
        if len(self.db.queryAndAnswerDB(query)) > 0:
            return True
        return False
    def prodcutEdit(self, info):
        try:
            if(2 > info.count('\n')):
                return "&#128219;  Не корректные данные. Воспользуйтесь примером."
            name = info.split('\n')[0]
            cost = info.split('\n')[1]
            weight = str(info.split('\n')[2])
            print("name = {} | cost = {} | weight = {} \n all = {}".format(
                  name,cost,weight,info.split('\n')))

            query = self.queryInsert.format(name, cost, weight)
            self.db.queryDB(query)
            return "&#10004; Обновите список для просмотра новой позиции товара."
        except:
            return "&#10060; Произошла ошибка. Обратитесь к разработчику."
    def productDelete(self, id):
        if not self.isAlready():
            return False
        query = self.queryDelete.format(id)
        self.db.queryDB(query)
