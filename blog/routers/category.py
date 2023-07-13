from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .. import database, schemas
from ..repository import category

from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/category",
    tags=["Categories"]
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.Category], status_code=status.HTTP_200_OK)
def get_all_category(db: Session = Depends(get_db)):
    return category.get_all_category(db)

@router.post('/', response_model=schemas.Category)
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return category.create_category(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int, db: Session = Depends(get_db)):
    return category.delete_cateogory(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_category(id: int, request: schemas.Category, db: Session = Depends(get_db)):
    return category.update_category(id, request, db)

@router.get('/{id}', response_model=schemas.Category)
def get_category(id: int, db: Session = Depends(get_db)):
    return category.get_category(id, db)