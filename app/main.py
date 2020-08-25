from fastapi import FastAPI, Response, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from models.product import Product
from models.user_signup import UserSignup
from models.reccomendation_engine import ReccomendationEngine
from data.mongodb import MongoDB
import json, datetime, jwt, os

rec_eng = ReccomendationEngine()
security = HTTPBasic()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
SECRET_KEY= os.getenv("MONGDB_URI")

@app.get("/")
async def root():
    return {"message": "Welcome to SpendWell's API, feel free to visit the docs for more info on how to use me! https://spendwell-api.herokuapp.com/docs"}

@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    check_user = MongoDB.login(username, password)
    if check_user["authenticated"]:
        print("secret_key" + os.environ.get('SECRET_KEY'))
        print("userid" + check_user["user_id"])
        try:
            token = jwt.encode({'user': check_user["user_id"], 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(days=2)}, SECRET_KEY, algorithm='HS256')
            return jsonable_encoder({'token': token.decode('UTF-8')})
        except Exception as e:
            print(e)
    return Response(json.dumps({"message": 'login failed'}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.post("/signup")
async def signup(user: UserSignup):
    try:
        if MongoDB.user_lookup(user.email) is not True:
            new_user = MongoDB.signup(user.username, user.password, user.email)
            token = jwt.encode({'user': new_user, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(days=1)}, SECRET_KEY, 'HS512')
            return jsonable_encoder({'token': token.decode('UTF-8')})
        else:
            return Response(json.dumps({"message": "User already Exists"}), 409)
    except KeyError:
        return Response(json.dumps({"message": "missing fields"}), 409)


@app.post("/barcode")
async def post_barcode(product: Product):
    reccomendation_list = rec_eng.get_rec_list(product.barcode)
    return reccomendation_list

