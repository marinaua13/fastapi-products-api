from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    sku = Column(String(20), unique=True, index=True, nullable=False)
    characteristics = relationship("Characteristic", back_populates="product", cascade="all, delete", lazy="selectin")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, sku={self.sku})>"


class Characteristic(Base):
    __tablename__ = 'characteristics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product = relationship("Product", back_populates="characteristics", lazy="selectin")

    def __repr__(self):
        return f"<Characteristic(id={self.id}, name={self.name}, value={self.value})>"
