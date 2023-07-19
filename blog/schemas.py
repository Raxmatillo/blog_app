from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from slugify import slugify




class BlogBase(BaseModel):
    title: str
    summary: Optional[str] = None
    body: Optional[str] = ...
    blog_subcategory: str
    owner_id: Optional[int] = None
    category_id: Optional[int] = None


class BlogCreate(BlogBase):
    slug: Optional[str] = Field(..., description="URL-ga mos keluvchi slug")
    owner_id: int
    category_id: int
    

 
class Blog(BlogBase):
    class Config():
        orm_mode = True




class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    

class UserCreate(UserBase):
    password: str

class User(UserBase):
    blogs: List[Blog] = []

    class Config():
        orm_mode = True



from datetime import datetime

class ShowBlog(BaseModel):
    title: str
    summary: str
    body: str
    photo: str
    slug: str
    views: int
    category_id: int
    owner_id: int
    created_at: datetime

    class Config():
        orm_mode=True




class Login(BaseModel):
    username: str
    password: str




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None