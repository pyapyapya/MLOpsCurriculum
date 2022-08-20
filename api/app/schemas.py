from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class User(UserBase):
    id: int
    name: str
    age: Optional[int] = None

    class Config:
        orm_mode = True


class UserInfo(UserBase):
    name: str
    age: Optional[int] = None
