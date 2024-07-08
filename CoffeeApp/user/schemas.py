from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    name: str


class User(UserBase):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
