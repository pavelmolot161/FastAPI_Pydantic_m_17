### - 06.12.24

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import *
from sqlalchemy import insert
from app.schemas.category import CreateCategory

from slugify import slugify



router = APIRouter(
    prefix="/category",
    tags=["category"]                               ### - группа маршрутов для документации
)

@router.post("/create")
async def create_category(db: Annotated[Session, Depends(get_db)], create_category: CreateCategory):
    db.execute(insert(Category).values(name=create_category.name,
                                       parent_id=create_category.parent_id,
                                       slug=slugify(create_category.name)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': "Successful (1)"
    }

### -  ---------------------------------------------------------------------------------------------------------

from sqlalchemy import select
@router.get("/all_categories")
async def get_all_categories(db: Annotated[Session, Depends(get_db)]):
    categories = db.scalars(select(Category).where(Category.is_active == True)).all()
    return categories

### -  ---------------------------------------------------------------------------------------------------------

@router.put("/update_category")
async def update_category(db: Annotated[Session, Depends(get_db)], category_id: int, update_category: CreateCategory):
    category = db.scalar(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no Category found (2)"
        )
    db.execute(insert(Category).values(name=update_category.name,
                                       slug=slugify(update_category.name),
                                       parent_id=update_category.parent_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': "Category update is Successful (3)"
    }

### -  --------------------------------------------------------------------------------------------------------
from sqlalchemy import update

@router.delete("/{category_id}")
async def delete_category(db: Annotated[Session, Depends(get_db)], category_id: int):
    category = db.scalar(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no Category found (4)"
        )
    db.execute(update(Category).where(Category.id == category_id).values(is_active=False))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': "Category delite is Successful (4)"
    }
### -  ---------------------------------------------------------------------------------------------------------










