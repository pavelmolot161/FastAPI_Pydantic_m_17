### - 08.12.24
### - этот файл не заполнялся в лекции, поэтому заполнен по аналогии

from fastapi import APIRouter, HTTPException
from app.schemas.products import Product, ProductCreate              ### - ?
from app.schemas.products import CreateProduct

router = APIRouter(
    prefix="/products",
    tags=["products"]                                                ### - группа маршрутов для документации
)

products = [{'id': 1, 'name': "Laptop", 'category_id': 1}, {'id': 2, "name": "Book", 'category_id': 2}]             ### - фейковые данные


# @router.get("/")                                                   ### - было до 05.12.24
# async def all_products():
#     pass

# @router.get("/", response_model=list[Product])
@router.get("/", response_model=list[Product])
async def get_all_products():
    return products

# @router.post("/create")                                             ### - было до 05.12.24
# async def create_product():
#     pass

@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    """Создать продукт"""
    new_product = {"id": len(products) + 1, "name": product.name, "category_id": product.category_id}
    products.append(new_product)
    return new_product

@router.get("/{all_products_slug}")
async def product_by_category():
    pass

@router.get("/detail/{product_slug}")
async def product_detail():
    pass

# @router.put("/detail/{product_slug}")                                ### - было до 05.12.24
# async def update_product():
#     pass

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate):
    """Обновить продукт"""
    for prod in products:
        if prod["id"] == product_id:
            prod["name"] = product.name
            prod["category_id"] = product.category_id
            return prod
    raise HTTPException(status_code=404, detail="Product not found")

# @router.delete("/delete")                                             ### - было до 05.12.24
# async def delete_product():
#     pass

@router.delete("/{product_id}")
def delete_product(product_id: int):
    """Удалить продукт"""
    global products
    products = [prod for prod in products if prod["id"] != product_id]
    return {"message": "Product deleted"}

'''Пояснения к коду:
1 - Фейковые данные: Продукты представлены как список словарей.
2 - Логика обновления: Ищем продукт по id, если не найдено — возвращаем ошибку 404'''