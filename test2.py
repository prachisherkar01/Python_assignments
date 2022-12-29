import pymongo

client = pymongo.MongoClient("mongodb+srv://Prachi404:hdy3ivgZNPWMD88b@cluster0.tjvmguu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
database =client['myinfo']
collection = database['ps1']
record=collection.find()
#for i in record:
 #   print(i)

#d1= collection.find({"companyName":'iNeuron'})

data= collection.find({"courseOffered" : {"$gt" : 'E'}})
for i in data:
    print(i)