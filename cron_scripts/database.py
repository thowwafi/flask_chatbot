from pymongo import MongoClient
from decouple import config


client = MongoClient('mongodb://localhost:27017/')
db = client[config('DATABASE_NAME')]
collection = db[config('DATABASE_COLLECTION_NAME')]
    
def add_one_record(record):
    collection.insert_one(record)
    return


def retrieve_last_record():
    # read the last record
    record = collection.find_one(sort=[('_id', -1)])
    print(record)

if __name__ == "__main__":
    # questions = ["apa itu deltacloud.id?", "layanan deltacloud.id", "berapa harga layanan hosting termurah?", 
    #              "apa saja layanan yang disediakan deltacloud",
    #              "apa itu fastlab", "layanan fastlab", "berapa harga layanan fastlab?", "apa saja layanan yang disediakan fastlab"]
    questions = ["apa saja tipe performance hosting di deltacloud?"]
    for question in questions:
        record = {
            "number": "+6280989999",
            "question": f"{question}",
            "answer": "easy, medium, hard",
            "question_token_count": 0,
            "answer_token_count": 0,
            "is_sent": True
        }
        print(question)
        add_one_record(record)

    retrieve_last_record()
