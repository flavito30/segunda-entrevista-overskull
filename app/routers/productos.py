
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db
from fastapi import Depends
from fastapi import HTTPException

router = APIRouter(
    prefix="/productos",
    tags=["productos"],
)

#filter by page and size



@router.get("/", response_model=list[schemas.Product])
def read_products(page: int = 1, size: int = 3, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    limit = size
    return services.get_products(db, skip=skip, limit=limit)

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

