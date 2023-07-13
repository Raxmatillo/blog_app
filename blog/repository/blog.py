from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

from slugify import slugify




def create_slug(slug)-> str:
    if slug is not None:
        return slugify(slug)




def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request, db: Session):
    slugword = create_slug(request.title.lower())
    newBlog = models.Blog(**request.dict(), slug=slugword)
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

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the {id} is not available")
    
    blog.update(*request.dict())
    db.commit()
    return 'updated'


def show(slug: str, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.slug == slug).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the {slug} is not available")
    return blog