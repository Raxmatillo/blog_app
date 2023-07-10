from typing import List, Optional

from pydantic import BaseModel, EmailStr





class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True



class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str or None = None


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str or None = None

    class Config():
        orm_mode = True



class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

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