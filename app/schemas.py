from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):

    id : int
    email: str
    class Config:
        orm_mode =True

class Post(PostBase):

    id : int
    created_at: datetime
    user_id: int
    owner : UserOut

    class Config:
        orm_mode = True

class UserCreate(BaseModel):

    email: EmailStr
    password: str


class UserLogin(BaseModel):

    email: EmailStr
    password: str

class Token(BaseModel):
    access_token :str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
