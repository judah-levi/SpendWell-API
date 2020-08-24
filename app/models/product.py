from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    upc: int
    brand: str
    name: str
    description: Optional[str] = None