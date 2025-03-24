from pydantic import BaseModel, Field
from typing import List, Optional


class CharacteristicBase(BaseModel):
    name: str = Field(
        ...,
        title="Characteristic Name",
        description="For example: color, size, weight, etc.",
        example="Color"
    )
    value: str = Field(
        ...,
        title="Characteristic Value",
        description="The value of the corresponding characteristic",
        example="Red"
    )


class CharacteristicCreate(CharacteristicBase):
    pass


class Characteristic(CharacteristicBase):
    id: int = Field(
        ...,
        title="Characteristic ID",
        description="Unique identifier for the characteristic",
        example=1
    )
    product_id: int = Field(
        ...,
        title="Product ID",
        description="ID of the product to which this characteristic belongs",
        example=5
    )

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str = Field(
        ...,
        title="Product Name",
        description="The full name of the product",
        example="Lenovo ThinkPad Laptop"
    )
    quantity: int = Field(
        ...,
        title="Quantity",
        description="Number of items available",
        example=20
    )
    sku: str = Field(
        ...,
        title="SKU (Stock Keeping Unit)",
        description="Unique product identifier",
        example="ABC12345"
    )


class ProductCreate(ProductBase):
    characteristics: Optional[List[CharacteristicCreate]] = Field(
        default=[],
        title="List of Characteristics",
        description="Additional product features such as size, color, weight"
    )


class Product(ProductBase):
    id: int = Field(
        ...,
        title="Product ID",
        description="Unique identifier for the product",
        example=10
    )
    characteristics: List[Characteristic] = Field(
        default=[],
        title="Characteristics",
        description="List of characteristics associated with the product"
    )


    class Config:
        from_attributes = True
