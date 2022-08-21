from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    pass


class UserInfo(UserBase):
    id: int = Field(title="유저 고유 아이디")
    name: str = Field(title="유저 닉네임")
    age: Optional[int] = Field(title="유저 나이", default=None)

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    name: str = Field(title="유저 닉네임")
    age: Optional[int] = Field(title="유저 나이", default=None)
