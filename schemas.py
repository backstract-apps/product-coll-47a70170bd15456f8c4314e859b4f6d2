from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Product(BaseModel):
    product_id: int
    product_name: str
    product_description: str
    category: str
    price: int


class ReadProduct(BaseModel):
    product_id: int
    product_name: str
    product_description: str
    category: str
    price: int
    class Config:
        from_attributes = True


