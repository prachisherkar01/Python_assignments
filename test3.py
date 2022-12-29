import pymongo

client = pymongo.MongoClient("mongodb+srv://Prachi404:hdy3ivgZNPWMD88b@cluster0.tjvmguu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

database = client['inventory']
collection = database['table']
#collection.insert_many(data)

#d = collection.find()
#d=collection.find({"status" : "A"})
#d=collection.find({"status" : {"$in" :["A","P"]}})
#d=collection.find({"status" : {"$gt" :"B"}})
#d=collection.find({"status" : {"$gte" :"B"}})
#d=collection.find({"qty" : 100})
#d=collection.find({"qty" : {"$gte" :70}})
#d = collection.find({"item" : "sketchbook" , "qty" : 80 })
#d = collection.find({"item" : "sketchbook","qty" : {"$gte" : 50}})
#d = collection.find({'$or' : [{'item' : 'sketchbook'},{"qty" : {"$gte" : 50}}]})

#d = collection.update_one({'item':'canvas'} , {'$set' : {'item' : 'prachi'}})
d = collection.delete_one({'qty' : 25})
d = collection.find()
for i in d :
    print(i)

