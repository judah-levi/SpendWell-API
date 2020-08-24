from fastapi import FastAPI
from models.product import Product
from models.reccomendation_engine import ReccomendationEngine

rec_eng = ReccomendationEngine()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to SpendWell's API, feel free to visit the docs for more info on how to use me! https://spendwell-api.herokuapp.com/docs"}

@app.post("/barcode")
async def post_barcode(product: Product):
    reccomendation_list = rec_eng.get_rec_list(product.upc)
    return reccomendation_list

