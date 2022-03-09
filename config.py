from http import client
import pymongo
import certifi


mongl_url = "mongodb+srv://LeoFSDI:Tonio*726@cluster0.iiihb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongl_url, tlsCAFile=certifi.where())

# get specific db
db = client.get_database("SQSStyle")