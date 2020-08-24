import pymongo
import os
from argon2 import PasswordHasher

client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
db = client["spendwell"]
users = db["users"]
ph = PasswordHasher()

class MongoDB:

    @staticmethod
    def signup(user_name, password, email):
        hashed_password = ph.hash(password)
        users.insert_one({
            "user": user_name,
            "password": hashed_password,
            "email": email})
        return str(users.find_one({'user': user_name})["_id"])

    @staticmethod
    def login(user_name, password):
        find_user = users.find_one({'user': user_name})
        if ph.verify(find_user["password"], password):
            return {"user_id": str(find_user["_id"]), "authenticated": True}
        else:
            return {"authenticated": False}

    @staticmethod
    def user_lookup(email):
        if users.find_one({"email": email}):
            return True
        else:
            return False
