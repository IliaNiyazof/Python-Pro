import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.mydb.pokupki
# # осуществляем добавление документа в коллекцию,
# # который содержит поля name и price - имя и цена
# doc = db.insert_many([{"name": "Стакан", "price": "100"}, {"name": "Куртка", "price": "5000"},
# {"name": "Колонка", "price": "2500"}, {"name": "Ноутбук", "price": "40000"}])
# заменить
# doc = db.replace_one({"name": "Стакан", "price": "100"}, {"name": "Стакан", "price": "200"})
#
# # обновить
# doc = db.update_one({"name": "Стакан", "price": "200"}, {"$set": {"name": "Кружка", "price": "200"}})
#
# # удалить
doc = db.delete_one({"name": "Кружка", "price": "200"})
#
# выводим все документы из коллекции coll
for men in db.find():
    print(men)
