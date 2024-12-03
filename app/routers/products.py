
### - этот файл не заполнялся в лекции, поэтому заполнен по аналогии

from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/all_products")
async def get_all_products():
    pass

@router.post("/create")
async def creaty_products():
    pass

@router.put("/update_products")
async def update_products():
    pass

@router.delete("/delete")
async def delete_products():
    pass
