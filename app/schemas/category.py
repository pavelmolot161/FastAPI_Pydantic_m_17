### - 08.12.24

from pydantic import BaseModel

class Category(BaseModel):
    id: int                    # Поле для уникального идентификатора
    name: str                  # Поле для названия категории

class Config:
    orm_mode = True            # Указывает, что объект может быть преобразован из ORM (например, SQLAlchemy)

class CategoryCreate(BaseModel):
    name: str                  # Поле для ввода названия категории при создании

class CreateCategory(BaseModel):  ### - перемещен из файла в папке арр/schemas
    name: str
    parent_id: int | None

'''Пояснения:

1 - BaseModel: Все модели Pydantic наследуются от BaseModel.
2 - id и name: Типы данных (int, str) указывают, что FastAPI будет проверять типы на этапе выполнения.
3 - orm_mode = True: Позволяет преобразовывать данные из объектов базы данных.
4 - CategoryCreate: Модель для данных, необходимых при создании категории 
(здесь не нужен id, так как он генерируется автоматически).'''