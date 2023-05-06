from datetime import datetime
from typing import List

from decouple import config
from fastapi import APIRouter, HTTPException

from config.db import session
from models.index import Products
from schema.index import Product

from .utils import callscript

product_router = APIRouter()

# @product_router.get("/query_by_product_id/{user_id}")
# async def read_product(user_id: int):
#     try:
#         return session.query(Products).filter(Products.id == user_id).first()
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=404, detail="User not found")
    

# @product_router.get("/get_all_product")
# async def read_product():    
#     try:
#         res = session.query(Products).all()
#     except Exception:
#         res = []
#     return res


@product_router.post("/products/scrape")
async def write_product(product : List[Product]):
    print("HIT ----->>>> ", product)
    products = {}
    for item in product:
        for name in item.name:
            print("ITEM ----> ", name)
            products = await callscript(name)
    print("PRODUCTS ---- > ", products)
    return products
    try:
        product_data = Products(
            name = product.name,
        )
        session.add(product_data)
        session.commit()
        session.refresh(product_data)
        return session.query(Products).filter_by(id=product_data.id).first()
    except Exception as e:
        print(e) 
        session.rollback()
        return []





