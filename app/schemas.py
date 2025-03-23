from pydantic import BaseModel
from typing import List, Optional


class CharacteristicBase(BaseModel):
    name: str
    value: str


class CharacteristicCreate(CharacteristicBase):
    pass


class Characteristic(CharacteristicBase):
    id: int
    product_id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    quantity: int
    sku: str


class ProductCreate(ProductBase):
    characteristics: Optional[List[CharacteristicCreate]] = []


class Product(ProductBase):
    id: int
    characteristics: List[Characteristic] = []

    class Config:
        from_attributes = True
