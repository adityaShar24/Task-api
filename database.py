from pymongo import MongoClient

MONGO_CONNECTION_LINK = "mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority"

mongo_client = MongoClient(MONGO_CONNECTION_LINK)

database = mongo_client["MyTaskapi"]
task_collections = database["tasks"]
users_collections = database["users"]