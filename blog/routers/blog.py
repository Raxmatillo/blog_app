from typing import List
import os, shutil
from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File

from .. import schemas, models, database, oaut2
from .. repository import blog
from slugify import slugify

from sqlalchemy.orm import Session



get_db = database.get_db

router = APIRouter(
    tags=["Blogs"], 
    prefix="/blog"
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


def create_slug(slug)-> str:
    if slug is not None:
        return slugify(slug)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    upload_dir = os.path.join(os.getcwd(), "uploads")

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    dest = os.path.join(upload_dir, file.filename)
    print(dest, '<<<<')

    with open(dest, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    slugword = create_slug(request.title.lower())
    newBlog = models.Blog(**request.dict(), slug=slugword, photo=file.filename)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.update(id, request, file, db)


@router.get('/{slug}', status_code=200, response_model=schemas.ShowBlog)
def show(slug: str, db: Session = Depends(get_db)):
    return blog.show(slug, db)