
### - FastAPI_Pydantic_m_17
### - 29.11.24
### - Установка - >>> pip install uvicorn
### - Переход в cd app вот так - (.venv) PS D:\FastAPI_Pydantic_m_17> >>> cd app
### - ЗАПУСК - >>> python -m uvicorn module_17_1:app

from fastapi import FastAPI
from app.routers import category, products

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(category.router)
app.include_router(products.router)






