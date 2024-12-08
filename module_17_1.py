
### - FastAPI_Pydantic_m_17
### - 05.12.24
### - Установка - >>> pip install uvicorn
### - Переход в cd app вот так - (.venv) PS D:\FastAPI_Pydantic_m_17> >>> cd app
'''04.12.24 файл module_17_1 перенесен из своей папки в app в корневую папку фастапи для запуска всего проэкта, так как
он перестал запускатся со своего места из папки app'''
### - >>> uvicorn app.module_17_1:app --reload    ### - если запускной файл в app
### - ЗАПУСК - >>> python -m uvicorn module_17_1:app
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> pip install alembic
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> alembic init app/migrations ### - создание папки migrations
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> alembic revision --autogenerate -m "Initial migration Первоначальная миграция"



from fastapi import FastAPI
from app.routers import category, products

app = FastAPI()

### - Подключаем маршруты
# app.include_router(category.router)
# app.include_router(products.router)

@app.get("/")
async def root():
    """Главная страница"""
    return {"message": "Welcome to the Shop API"}

# ### - Подключаем маршруты
app.include_router(category.router)
app.include_router(products.router)

'''Пояснения:

1 - app.include_router: Подключаем маршруты из файлов category.py и products.py.
2 - Главная страница: Простая точка входа с приветствием.'''
#################################################################################

#_________________________________env.py_________________________________________

# target_metadata = None   ### - было

# from app.backend.db import Base
# from app.models.category import Category
# from app.models.products import Product
# target_metadata = Base.metadata

#________________________________________________________________________________

#_______________________________alembic.ini______________________________________

# sqlalchemy.url = driver://user:pass@localhost/dbname   ### - было
# sqlalchemy.url = sqlite:///ecommerce.db

#________________________________________________________________________________

'''Создание миграций:
Убедитесь, что у Вас есть актуальные миграции. Для создания новой миграции выполните команду:
>>> alembic revision --autogenerate -m "Описание изменений"

   Применение миграций:
После создания миграций нужно их применить. Используйте команду:
>>> alembic upgrade head

   Проверка состояния миграций:
Можно проверить, какие миграции были применены и какие — нет, выполнив:
>>> alembic current
>>> alembic history            '''





























