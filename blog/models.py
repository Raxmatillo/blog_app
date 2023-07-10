from typing import Optional


from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

from datetime import datetime, date

from .database import Base



class Mixin:
    create_user: Mapped[int] = mapped_column()
    update_user: Mapped[Optional[int]] = mapped_column(default=None, init=False)



class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped(str) = mapped_column(String(120), index=True)



class Blog(Base):
    __tablename__ = 'blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner: Mapped[str]
    category: Mapped[str]
    title: Mapped[str] = mapped_column(String(120))
    summary: Mapped[str] = mapped_column(String(300))
    body: Mapped[str] = mapped_column(String)
    photo: Mapped[str]
    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


    def __repr__(self):
        return '<User %r>' % self.title




class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    full_name: Mapped[str] = mapped_column(String(120), index=True)