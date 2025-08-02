from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from typing import List
from models import Product
from schemas import ProductCreate

async def add_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(
        name=product_in.name.strip(),
        description=product_in.description,
        price=product_in.price,
        quantity=product_in.quantity
    )
    session.add(product)
    try:
        await session.commit()
        await session.refresh(product)
        return product
    except IntegrityError:
        await session.rollback()
        raise

async def get_all_products(session: AsyncSession) -> List[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.execute(stmt)
    return result.scalars().all()
