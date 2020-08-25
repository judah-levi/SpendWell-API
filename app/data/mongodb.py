import pymongo
import os
from argon2 import PasswordHasher
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client["spendwell"]
users = db["users"]
ph = PasswordHasher()

class MongoDB:

    @staticmethod
    def signup(username, password, email):
        hashed_password = ph.hash(password)
        users.insert_one({
            "user": username,
            "password": hashed_password,
            "email": email})
        return str(users.find_one({'user': username})["_id"])

    @staticmethod
    def login(username, password):
        find_user = users.find_one({'user': username})
        if find_user:
            if ph.verify(find_user["password"], password):
                return {"user_id": str(find_user["_id"]), "authenticated": True}
        return {"authenticated": False}

    @staticmethod
    def user_lookup(email):
        if users.find_one({"email": email}):
            return True
        else:
            return False
