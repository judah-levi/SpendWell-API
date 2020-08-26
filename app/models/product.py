from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    barcode: int
    brand: Optional [str] = None
    name: Optional [str] = None
    description: Optional[str] = None