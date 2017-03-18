from pymongo import MongoClient

try:
    mongoClient = MongoClient("mongodb://172.28.128.3:27017")

    db = mongoClient.usdata

    data = db.cityinfo.find().limit(10)

    for d in data:
        print d

except Exception, e:
    print str(e)