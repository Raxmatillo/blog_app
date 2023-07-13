from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .. import database, schemas, models
from .. hashing import Hash
from ..repository import user
from sqlalchemy.orm import Session




router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


get_db = database.get_db



@router.get('/', response_model=List[schemas.User], status_code=status.HTTP_200_OK)
def get_all_user(db: Session = Depends(get_db)):
    return user.get_all_user(db)


@router.post('/', response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.UserBase, db: Session = Depends(get_db)):
    return user.update_user(id, request, db)


@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)