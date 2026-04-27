from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/") # normal without docker

client = MongoClient("mongodb://mongodb:27017/") # specific for docker

db = client["rag_db"]
chat_collection = db["chat_history"]