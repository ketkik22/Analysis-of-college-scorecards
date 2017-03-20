
from pymongo import MongoClient
from config import *

try:
    mongoClient = MongoClient(HOST_NAME,PORT_NUMBER, serverSelectionTimeoutMS=CONNECTION_ATTEMPT_DURATION_MS)

    db = mongoClient[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    for post in collection.find({"INSTNM":"University of Southern California"}).limit(1):
        if(post["HIGHDEG"] == 0):
            print "Highest degree offered by %s is Non-degree granting" %post["INSTNM"]
        elif(post["HIGHDEG"] == 1):
            print "Highest degree offered by %s is certificate degree" % post["INSTNM"]
        elif (post["HIGHDEG"] == 2):
            print "Highest degree offered by %s is Associate degree" % post["INSTNM"]
        elif (post["HIGHDEG"] == 3):
            print "Highest degree offered by %s is Bachelor's degree" % post["INSTNM"]
        elif (post["HIGHDEG"] == 4):
            print "Highest degree offered by %s is Graduate degree" % post["INSTNM"]
        #print post["HIGHDEG"]

    mongoClient.close()
except Exception, e:
    print str(e)