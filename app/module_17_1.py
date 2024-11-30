
### - FastAPI_Pydantic_m_17
### - 30.11.24
### - Установка - >>> pip install uvicorn
### - Переход в cd app вот так - (.venv) PS D:\FastAPI_Pydantic_m_17> >>> cd app
### - ЗАПУСК - >>> python -m uvicorn module_17_1:app
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> pip install alembic
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> alembic init app/migrations ### - создание папки migrations
### - (.venv) PS D:\FastAPI_Pydantic_m_17> - >>> alembic revision --autogenerate -m "Initial migration"



from fastapi import FastAPI
from app.routers import category, products

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(category.router)
app.include_router(products.router)

#################################################################################

# target_metadata = None   ### - было
# from app.backend.db import Base
# from app.models.category import Category
# from app.models.products import Product
# target_metadata = Base.metadata


#sqlalchemy.url = driver://user:pass@localhost/dbname   ### - было
# sqlalchemy.url = sqlite:///ecommerce.db
