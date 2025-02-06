from pydantic import BaseModel, Field
from typing import List
import re

class Item(BaseModel):
    shortDescription: str = Field(..., pattern=r"^[\w\s\-]+$")
    price: str = Field(..., pattern=r"^\d+\.\d{2}$")

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$")
    purchaseDate: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD
    purchaseTime: str = Field(..., pattern=r"^\d{2}:\d{2}$")  # HH:MM
    items: List[Item]
    total: str = Field(..., pattern=r"^\d+\.\d{2}$")

class ReceiptResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    points: int
