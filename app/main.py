from fastapi import FastAPI
from models.product import Product
import os


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to SpendWell's API, feel free to visit the docs for more info on how to use me! https://spendwell-api.herokuapp.com/docs"}

@app.post("/barcode")
async def post_barcode(product: Product):
    return product



