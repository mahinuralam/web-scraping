from datetime import datetime

from decouple import config
from fastapi import APIRouter, HTTPException

from config.db import session
from models.index import Products
from schema.index import Products

user_router = APIRouter()

@user_router.get("/query_by_user_id/{user_id}")
async def read_user(user_id: int):
    try:
        return session.query(Products).filter(Products.id == user_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="User not found")
    

@user_router.get("/get_all_user")
async def read_user():    
    try:
        res = session.query(Products).all()
    except Exception:
        res = []
    return res


@user_router.post("/regiser_user")
async def write_user(user : Products):
    try:
        user_data = Products(
                name = user.name,
                price = user.price,
                ulr = user.url
        )
        session.add(user_data)
        session.commit()
        session.refresh(user_data)
        return session.query(Products).filter_by(id=user_data.id).first()
    except Exception as e:
        print(e) 
        session.rollback()
        return []





