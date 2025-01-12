
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db
from fastapi import Depends
from fastapi import HTTPException
from typing import Optional
from app import models

router = APIRouter(
    prefix="/productos",
    tags=["productos"],
)

#filter by page and size



@router.get("/", response_model=list[schemas.Product])
def read_products(
    page: int = 1,
    size: int = 3,
    categoria: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db)
):
    skip = (page - 1) * size
    query = db.query(models.Product)

    # Aplicar filtros opcionales
    if categoria:
        query = query.filter(models.Product.categoria == categoria)
    if min_price is not None:
        query = query.filter(models.Product.precio >= min_price)
    if max_price is not None:
        query = query.filter(models.Product.precio <= max_price)

    # Paginación
    productos = query.offset(skip).limit(size).all()
    return productos

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return services.get_product(db, productId=product_id)

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate,db: Session = Depends(get_db)):
    return services.create_product(db, product=product)

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    dbProduct = services.update_product(db, productId=product_id, product=product)
    if dbProduct is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return dbProduct

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    dbProduct = services.delete_product(db, productId=product_id)
    if dbProduct is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return dbProduct

