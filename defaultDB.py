# -*- coding: UTF-8 -*-
createAdmin = "CREATE TABLE admin(id integer, uname TEXT, rights integer)"
createAdminRef = "CREATE TABLE adminRef(key integer, rights integer)"
createArea = "CREATE TABLE area(id integer primary key, city text, area text, productID text)"
createBuyData = "CREATE TABLE buyData(qiwi text, btc text)"
createCity = "CREATE TABLE city(id integer primary key, name text, many integer, count integer)"
createContact = "CREATE TABLE contact(id text)"
createJob = "CREATE TABLE job(id integer primary key, summery text)"
createProduct = "CREATE TABLE product(id integer primary key,name text, cost integer, wight text)"
createStat = "CREATE TABLE statUser(activate int, joinbuy)"
createState = "CREATE TABLE stateUser(id integer, joinbuy)"
createUsrCode = "CREATE TABLE usrCode(id integer, refcode integer, enterkey integer)"
createUsrData = "CREATE TABLE usrData(id integer, useRef integer)"
queryInsertContact = ["INSERT INTO contact(id) VALUES('@durov')"]
queryInsertCity = ["INSERT INTO city(name) VALUES('Санкт-Петербург')","INSERT INTO city(name) VALUES('Москва')","INSERT INTO city(name) VALUES('Екатеринбург')","INSERT INTO city(name) VALUES('Красноярск')","INSERT INTO city(name) VALUES('Новосибирск')","INSERT INTO city(name) VALUES('Нижний Новгород')",]
queryInsertArea = ["INSERT INTO area(area,city) VALUES('ст.м Ветеранов','Санкт-Петербург')","INSERT INTO area(area,city) "
                                                                                       "VALUES('ст.м Девяткино',"
                                                                                       "'Санкт-Петербург')",
              "INSERT INTO area(area,city) VALUES('ст.м Автово','Санкт-Петербург')","INSERT INTO area(area,"
                                                                                    "city) VALUES('Ленинский "
                                                                                    "проспект','Санкт-Петербург')",
              "INSERT INTO area(area,city) VALUES('ст.м Парнас','Санкт-Петербург')","INSERT INTO area(area,"
                                                                                    "city) VALUES('ст.м Пионерская',"
                                                                                    "'Санкт-Петербург')","INSERT INTO "
                                                                                                         "area(area,"
                                                                                                         "city) "
                                                                                                         "VALUES("
                                                                                                         "'ст.м "
                                                                                                         "Купчино',"
                                                                                                         "'Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст.м Озерки','Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст.м Рыбацкое','Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст.м Елизаровская','Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст. Московская','Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст.м Электросила','Санкт-Петербург')","INSERT INTO area(area,city) VALUES('ст.м Лубянка','Москва')","INSERT INTO area(area,city) VALUES('ст.м Комсомольская','Москва')","INSERT INTO area(area,city) VALUES('ст.м Спортивная','Москва')","INSERT INTO area(area,city) VALUES('ст.м Юго-Западная','Москва')","INSERT INTO area(area,city) VALUES('ст.м Митино','Москва')","INSERT INTO area(area,city) VALUES('ст.м Строгино','Москва')","INSERT INTO area(area,city) VALUES('ст. Кунцевская','Москва')","INSERT INTO area(area,city) VALUES('ст.м Киевская','Москва')","INSERT INTO area(area,city) VALUES('ст. Международная','Москва')","INSERT INTO area(area,city) VALUES('ст.м Арбатская','Москва')","INSERT INTO area(area,city) VALUES('Ленинский район','Екатеринбург')","INSERT INTO area(area,city) VALUES('Кировский район','Екатеринбург')","INSERT INTO area(area,city) VALUES('Октябрьский район','Екатеринбург')","INSERT INTO area(area,city) VALUES('Чкаловский район','Екатеринбург')","INSERT INTO area(area,city) VALUES('Железнодорожный р-н','Екатеринбург')","INSERT INTO area(area,city) VALUES('Советский район','Красноярск')","INSERT INTO area(area,city) VALUES('Свердловский район','Красноярск')","INSERT INTO area(area,city) VALUES('Октябрьский район','Красноярск')","INSERT INTO area(area,city) VALUES('Ленинский район','Красноярск')","INSERT INTO area(area,city) VALUES('Кировский район','Красноярск')","INSERT INTO area(area,city) VALUES('Железнодорожный район','Красноярск')","INSERT INTO area(area,city) VALUES('Центральный район','Красноярск')","INSERT INTO area(area,city) VALUES('Центральный район','Новосибирск')","INSERT INTO area(area,city) VALUES('Советский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Первомайский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Октябрьский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Ленинский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Кировский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Калининский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Дзержинский район','Новосибирск')","INSERT INTO area(area,city) VALUES('Автозаводский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Канавинский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Ленинский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Московский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Нижегородский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Приокский р-н','Нижний Новгород')","INSERT INTO area(area,city) VALUES('Советский р-н','Нижний Новгород')", "INSERT INTO area(area,city) VALUES('Сормовский р-н','Нижний Новгород')"]
import sqlite3
def createTable():
    conn = sqlite3.connect("sqlitedb.db")
    cursor = conn.cursor()
    cursor.execute(createAdmin)
    cursor.execute(createAdminRef)
    cursor.execute(createState)
    cursor.execute(createStat)
    cursor.execute(createArea)
    cursor.execute(createCity)
    cursor.execute(createContact)
    cursor.execute(createBuyData)
    cursor.execute(createUsrCode)
    cursor.execute(createUsrData)
    cursor.execute(createJob)
    cursor.execute(createProduct)
    conn.commit()
    conn.close()
def InsertDataContact():
    conn = sqlite3.connect("sqlitedb.db")
    cursor = conn.cursor()
    for item in queryInsertContact:
        print(item)
        cursor.execute(item)
    conn.commit()
    conn.close()
def InsertDataCity():
    conn = sqlite3.connect("sqlitedb.db")
    cursor = conn.cursor()
    for item in queryInsertCity:
        cursor.execute(item)
    querySetCash = "UPDATE city SET many = 0"
    cursor.execute(querySetCash)
    conn.commit()
    conn.close()
def InsertDataArea():
    conn = sqlite3.connect("sqlitedb.db")
    cursor = conn.cursor()
    for item in queryInsertArea:
        cursor.execute(item)
    conn.commit()
    conn.close()
createTable()
InsertDataContact()
InsertDataCity()
InsertDataArea()
print("[+] Good")