
from fastapi import FastAPI
from app.database import Base,engine
from app.routers import productos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Management API",
    description="Api para gestionar Productos en FastAPI",
    version="1.0.0"
)

app.include_router(productos.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your products management API!"}


