from fastapi import FastAPI
from app.api.endpoints import sleep
from app.db.base import Base
from app.db.session import engine

# Crea todas las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar las rutas
app.include_router(sleep.router, prefix="/api/v1")