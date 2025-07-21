from pymongo import MongoClient

class Services():
    def __init__(self, nameOfDataBase):
        client = MongoClient(host="localhost", port=27017)
        db = client[nameOfDataBase]
        self.workCollection = db["orders"]

    def setorder(self, orderData):
        self.workCollection.insert_one(orderData)

    def updateorder(self, orderName, newOrderData):
        self.workCollection.update_one({"pishghaza": orderName}, {"$set": newOrderData})

    def deleteorder(self, orderName):
        self.workCollection.delete_one({"pishghaza": orderName})

    def getorder(self, orderName):
        return self.workCollection.find_one({"pishghaza": orderName})

    def getAllorders(self):
        return self.workCollection.find({}, {"_id": 0})

    def getDoneorders(self, orderName):
        return self.workCollection.update_one({"pishghaza": orderName}, {"$set": {"price": True}})