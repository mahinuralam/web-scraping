from datetime import datetime

from decouple import config
from fastapi import APIRouter, HTTPException

from config.db import session
from models.index import Products
from schema.index import Products

product_router = APIRouter()

@product_router.get("/query_by_user_id/{user_id}")
async def read_user(user_id: int):
    try:
        return session.query(Products).filter(Products.id == user_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="User not found")
    

@product_router.get("/get_all_user")
async def read_user():    
    try:
        res = session.query(Products).all()
    except Exception:
        res = []
    return res


@product_router.post("/get_products")
async def write_product(product : Products):
    search_product = ['HP', 'Asus', 'Dell', 'Razor', 'Aser']
    
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





