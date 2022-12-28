import pymongo
#import urllib.parse

#username = urllib.parse.quote_plus('username')
#password = urllib.parse.quote_plus("password")

#url = "mongodb+srv://{}:{}@cluster0.tjvmguu.mongodb.net/?retryWrites=true&w=majority".format(username, password)
# url is just an example (your url will be different)

#cluster = MongoClient(url)
#db = cluster['Sample']
#collection = db['temporary']
client = pymongo.MongoClient("mongodb+srv://Prachi404:hdy3ivgZNPWMD88b@cluster0.tjvmguu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1=client['mongotest']
coll = db1['test']
coll.insert_one(d )
