from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_product(db: Session):

    product_all = db.query(models.Product).order_by(models.Product.id).all()
    res = {
        'product_all': product_all,
    }
    return res

async def get_product_product_id(db: Session, product_id: int):

    product_one = db.query(models.Product).filter(models.Product.product_id == 'product_id').first()
    res = {
        'product_one': product_one,
    }
    return res

async def post_product(db: Session, product_id: int, product_name: str, product_description: str, category: str, price: int):

    product_all = db.query(models.Product).order_by(models.Product.id).all()

    product_price = db.query(models.Product).filter(models.Product.product_id == 'price').first()
    res = {
        'product_inserted_record': product_inserted_record,
    }
    return res

async def put_product_product_id(db: Session):

    product_edited_record = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    for key, value in {'product_id': product_id, 'product_name': product_name, 'product_description': product_description, 'category': category, 'price': price}.items():
          setattr(product_edited_record, key, value)
    db.commit()
    db.refresh(product_edited_record)
    product_edited_record = product_edited_record

    res = {
        'product_edited_record': product_edited_record,
    }
    return res

async def delete_product_product_id(db: Session, id: str):

    product_deleted = None
    record_to_delete = db.query(models.Product).filter(models.Product.product_id == product_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        product_deleted = record_to_delete
    res = {
        'product_deleted': product_deleted,
    }
    return res

