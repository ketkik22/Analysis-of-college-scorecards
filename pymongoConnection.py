from pymongo import MongoClient
from config import *

try:
    mongoClient = MongoClient(HOST_NAME, PORT_NUMBER)

    db = mongoClient.usdata

    data = db.cityinfo.find({"state": {"$in" : ["CA", "CO", "MA"]}}).limit(10)

    for d in data:
        print d

except Exception, e:
    print str(e)