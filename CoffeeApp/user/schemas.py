from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str = Field(min_length=1)
    name: str = Field(min_length=1)


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
