from typing import List

from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Product, Characteristic
from app.schemas import ProductCreate, CharacteristicCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload


# async def create_product(db: AsyncSession, product: ProductCreate):
#     try:
#         db_product = Product(name=product.name, quantity=product.quantity, sku=product.sku)
#         db.add(db_product)
#         await db.flush()
#         for char in product.characteristics:
#             db_char = Characteristic(name=char.name, value=char.value, product_id=db_product.id)
#             db.add(db_char)
#         await db.commit()
#         await db.refresh(db_product)
#         return db_product
#     except IntegrityError:
#         await db.rollback()
#         raise HTTPException(status_code=400, detail="SKU must be unique.")
async def create_product(db: AsyncSession, product: ProductCreate):
    try:
        db_product = Product(name=product.name, quantity=product.quantity, sku=product.sku)
        db.add(db_product)
        await db.flush()

        for char in product.characteristics:
            db_char = Characteristic(name=char.name, value=char.value, product_id=db_product.id)
            db.add(db_char)

        await db.commit()

        result = await db.execute(
            select(Product)
            .options(selectinload(Product.characteristics))
            .where(Product.id == db_product.id)
        )
        return result.scalars().first()

    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU must be unique.")


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(Product)
        .options(selectinload(Product.characteristics))
        .where(Product.id == product_id)
    )
    return result.scalars().first()


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Product)
        .options(selectinload(Product.characteristics))
        .offset(skip).limit(limit)
    )
    return result.scalars().all()


async def update_product(db: AsyncSession, product_id: int, product_data: ProductCreate):
    product = await get_product(db, product_id)
    if product:
        product.name = product_data.name
        product.quantity = product_data.quantity
        product.sku = product_data.sku
        await db.commit()
        await db.refresh(product)
    return product


async def update_characteristics(db: AsyncSession, product_id: int, characteristics: List[CharacteristicCreate]):
    product = await get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Видаляємо старі характеристики
    await db.execute(delete(Characteristic).where(Characteristic.product_id == product_id))

    # Додаємо нові характеристики
    for char in characteristics:
        db_char = Characteristic(name=char.name, value=char.value, product_id=product.id)
        db.add(db_char)

    await db.commit()  # Комітимо зміни
    return {"detail": "Characteristics updated"}

async def delete_product(db: AsyncSession, product_id: int):
    product = await get_product(db, product_id)
    if product:
        await db.delete(product)
        await db.commit()  # Комітимо видалення продукту
    return product
