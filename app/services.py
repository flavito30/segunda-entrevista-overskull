
from sqlalchemy.orm import Session
from app import models , schemas
from fastapi import HTTPException

def get_products (db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product ( db : Session ,productId : int):
    return db.query(models.Product).filter(models.Product.id == productId).first()

def create_product ( db : Session , product : schemas.ProductCreate):
    try :
      db_product = models.Product( nombre = product.nombre , categoria = product.categoria , precio = product.precio , stock = product.stock )
      db.add(db_product)
      db.commit()
      db.refresh(db_product)
      return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Algo Has hecho mal",)

def update_product ( db : Session ,productId : int , product : schemas.ProductUpdate):
    db_product = get_product(db, productId)
    if not db_product:
        return None
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value) 
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product ( db : Session , productId : int):
    db_product = db.query(models.Product).filter(models.Product.id == productId).first()
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
    

