from pymongo import MongoClient
from bson import ObjectId 

client = MongoClient('mongodb://localhost:27017')
db = client['Hospital']
collectioName = ['patient', 'equipment', 'madicine', 'staff', 'users', 'doctors']

def getCollection(collectionName):
    if collectionName not in collectioName:
        raise Exception('Collection not found')
    
    return db[collectionName]

def insert(collectionName, data):
    print(data)
    try:
        collection = getCollection(collectionName)
        return collection.insert_one(data)
    except Exception as e:
        print(e)
        return False

def find(collectionName):
    
    try:
        collection = getCollection(collectionName)
        print(collection)
        return collection.find()
    except Exception as e:
        print(e)
        return False

def findOne(collectionName, query):
    print(query)
    try:
        collection = getCollection(collectionName)
        return collection.find_one({'_id' : ObjectId(query)})
    except Exception as e:
        print(e)
        return False
    

def update(collectionName, query, data):
    print(query)
    print(data)
    try:
        collection = getCollection(collectionName)
        return collection.update_one({'_id' : ObjectId(query)}, {'$set': data})
    except Exception as e:
        print(e)
        return False
    

def delete(collectionName, query):
    print(query)
    try:
        collection = getCollection(collectionName)
        result = collection.delete_one({'_id': ObjectId(query)})
        return result
    except Exception as e:
        print(e)
        return False