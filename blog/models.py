from typing import List
from enum import Enum
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, Column, Integer

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from sqlalchemy.sql.sqltypes import Enum as EnumSql

from .database import Base



class BlogSubcategory(str, Enum):
    BLOG = "blog"
    PROJECT = "project"


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    title = Column(String(120))
    summary = Column(String(300))
    body = Column(String)
    photo = Column(String)
    views = Column(Integer, default=0)
    blog_subcategory = Column(String(length=50), EnumSql(BlogSubcategory), default=BlogSubcategory.BLOG)
    slug = Column(String(255), nullable=False, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)

    owner = relationship("User", back_populates="blogs")
    category = relationship("Category", back_populates="blogs")

    def __repr__(self) -> str:
        return "<Post %r>" % self.slug

    def __str__(self) -> str:
        return f"{self.slug}"


    



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(120), index=True)
    username = Column(String(120), unique=True)
    password = Column(String(128))
    email = Column(String(120), index=True, unique=True)

    blogs = relationship("Blog")


# class Mixin =
#     create_user = Mapped[int] = mapped_column()
#     update_user = Mapped[Optional[int]] = mapped_column(default=None, init=False)



class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120))

    blogs = relationship("Blog", back_populates="category")

    def __repr__(self) -> str:
        return "<Category %r>" % self.slug

    def __str__(self) -> str:
        return f"{self.slug}"
