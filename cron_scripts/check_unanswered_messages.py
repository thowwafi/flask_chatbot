from flask import Flask
from flask import request, jsonify
import llama_index
from load_vector import loadVectorIndex
import os
import tiktoken
from createVectorIndex import model_name
from decouple import config
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client[config('DATABASE_NAME')]
collection = db[config('DATABASE_COLLECTION_NAME')]


def check_unanswered_messages():
    records = collection.find({"$or":[ {"answer": None}, {"answer" : ''}]})
    for record in records:
        print(record)
        vectorIndex = loadVectorIndex("Store")
        query_engine = vectorIndex.as_query_engine()
        result = query_engine.query(record['question'])
    return


if __name__ == "__main__":
    check_unanswered_messages()
