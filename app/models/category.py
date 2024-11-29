
### - 2,3,4 занятие
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


    # parent_id = Column(Integer, ForeignKey('categories.id'), nullable= True)
    # parent_id = Column(Integer, ForeignKey('products.id'), nullable=True, index=True)

    products = relationship('Product', back_populates='category')  ### - связывает сущности между собой 1 - 1

from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))

############################################################################################
