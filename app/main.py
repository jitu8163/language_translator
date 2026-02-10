from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Transformer Translator API")

app.include_router(router)
