from fastapi import HTTPException, status

from .. import schemas, models
from ..hashing import Hash


from sqlalchemy.orm import Session



def get_all_user(db: Session):
    users = db.query(models.User).all()
    return users


def create_user(request: schemas.UserCreate, db: Session):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password), full_name=request.full_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the {id} is not available!")

    user.delete(synchronize_session=False)
    db.commit()
    return 'user delete'

def update_user(id: int, request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the {id} is not available")
    
    user.update(dict(request))
    db.commit()
    return 'user updated'



def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the {id} is not available")
    return user

