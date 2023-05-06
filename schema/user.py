from datetime import datetime

from pydantic import BaseModel


class Products(BaseModel):
    name : str
    price : int
    url: str
    
