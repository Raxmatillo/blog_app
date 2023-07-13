from fastapi import HTTPException, status

from .. import schemas, models


from sqlalchemy.orm import Session





def get_all_category(db: Session):
    categories = db.query(models.Category).all()
    return categories


def create_category(request: schemas.CategoryCreate, db: Session):
    new_category = models.Category(name=request.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def delete_cateogory(id: int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id)

    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Category with the {id} is not available!')
    
    category.delete(synchronize_session=False)
    db.commit()
    return 'category delete'


def update_category(id: int, request: schemas.Category, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id)

    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Category with the {id} is not available!')
    
    category.update(dict(request))
    db.commit()
    return 'category updated'


def get_category(id: int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Category with the {id} is not available!')
    
    return category