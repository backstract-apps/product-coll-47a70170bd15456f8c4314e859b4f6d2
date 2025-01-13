from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/product/')
async def get_product(db: Session = Depends(get_db)):
    try:
        return await service.get_product(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/product/product_id')
async def get_product_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_product_product_id(db, product_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/product/')
async def post_product(product_id: int, product_name: str, product_description: str, category: str, price: int, db: Session = Depends(get_db)):
    try:
        return await service.post_product(db, product_id, product_name, product_description, category, price)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/product/product_id/')
async def put_product_product_id(db: Session = Depends(get_db)):
    try:
        return await service.put_product_product_id(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/product/product_id')
async def delete_product_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_product_product_id(db, product_id)
    except Exception as e:
        raise HTTPException(500, str(e))

