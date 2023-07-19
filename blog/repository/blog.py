from fastapi import HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from .. import models, schemas

from slugify import slugify

import os
import shutil



def create_slug(slug)-> str:
    if slug is not None:
        return slugify(slug)




def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request, file: UploadFile, db: Session):
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


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the {id} is not available")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Blog, file: UploadFile, db: Session):
    upload_dir = os.path.join(os.getcwd(), "uploads")

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    with open(dest, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the {id} is not available")
    print(file.filename)
    blog.update(*request.dict(), photo=file.filename)
    db.commit()
    return 'updated'


def show(slug: str, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.slug == slug).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the {slug} is not available")
    return blog