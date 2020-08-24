from fastapi import FastAPI
from models.product import Product
import os


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to SpendWell's API"}

@app.post("/barcode")
async def post_barcode(product: Product):
    return product



