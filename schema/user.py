from typing import List

from pydantic import BaseModel


class Product(BaseModel):
     name : List[str]
    
    
