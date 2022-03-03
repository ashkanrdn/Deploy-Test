from pymongo import MongoClient
from config import MONGO_CONFIGURATION


connection = MongoClient(**MONGO_CONFIGURATION)
db = connection["testdb"]
collection = db["test"]

deviceId = 1
def send_to_mongo(samples):
    collection.update_one({'deviceId': deviceId, 'nsamples': {'$lt': 200}},
                          {
                              '$push': {'samples': samples},
                              '$inc': {'nsamples': 1}
                          },
                          upsert=True

                          )