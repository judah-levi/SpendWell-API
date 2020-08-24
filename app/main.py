from fastapi import FastAPI
from models.product import Product
from models.user_signup import UserSignup
from models.reccomendation_engine import ReccomendationEngine
from db import MongoDB
import json
import os

rec_eng = ReccomendationEngine()
app = FastAPI()
config = os.environ.get("SECRET_KEY")


@app.get("/")
async def root():
    return {"message": "Welcome to SpendWell's API, feel free to visit the docs for more info on how to use me! https://spendwell-api.herokuapp.com/docs"}

@app.post("/login")
def login():
    pass

@app.post("/signup")
def signup(user: UserSignup):
    try:
        if MongoDB.user_lookup(user.email) is not True:
            new_user = mongoDB.signup(user.username, user.password, user.email)
            token = jwt.encode({'user': new_user, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(days=2)}, config, 'HS512')
            return json.dumps({'token': token.decode('UTF-8')})
        else:
            return make_response(json.dumps({"message": "User already Exists"}), 409)
    except KeyError:
        return make_response(json.dumps({"message": "missing fields"}), 409)


@app.post("/barcode")
async def post_barcode(product: Product):
    reccomendation_list = rec_eng.get_rec_list(product.upc)
    return reccomendation_list

