
### - 2,3,4 занятие
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *

class Product(Base):
    __tablename__ = "products"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))                ### - связь один ко многим
    rating = Column(Float)
    is_active = Column(Boolean, default=True)
    category = relationship('Category', back_populates='products')   ### - связывает сущности между собой 1 - 1

from sqlalchemy.schema import CreateTable
print(CreateTable(Product.__table__))
