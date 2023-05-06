from sqlalchemy import Column, DateTime, Float, Integer, String, Table
from sqlalchemy.sql import func

from config.db import Base, meta


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    url = Column(String)
    created_at=Column(DateTime(timezone=True), default=func.now())
    updated_at=Column(DateTime(timezone=True), onupdate=func.now())

