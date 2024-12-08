### - 08.12.24

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    category_id: int                 # Поле для связи с категорией

class Config:
    orm_mode = True

class ProductCreate(BaseModel):
    name: str
    category_id: int

class CreateProduct(BaseModel):      ### - перемещен из файла в папке арр/schemas
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category: int


'''Пояснения:

1 - category_id: Поле для указания, к какой категории относится продукт.
2 - Модель ProductCreate: Используется только для создания или обновления продукта.'''


