from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    name: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
