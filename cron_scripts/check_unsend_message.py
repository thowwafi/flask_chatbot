from pymongo import MongoClient
from decouple import config


client = MongoClient('mongodb://localhost:27017/')
db = client[config('DATABASE_NAME')]
collection = db[config('DATABASE_COLLECTION_NAME')]


def check_unsend_message():
    # read the last record
    # collection find all record with is_sent = False
    records = collection.find({'is_sent': False})
    for record in records:
        print(record)
    # record = collection.find_one(sort=[('_id', -1)])
    # print(record)
    # if record['is_sent'] == False:
    #     return record
    # else:
    #     return None


if __name__ == "__main__":
    check_unsend_message()
