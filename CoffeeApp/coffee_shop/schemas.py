from pydantic import BaseModel


class CoffeeShopBase(BaseModel):
    name: str


class CoffeeShopCreate(CoffeeShopBase):
    name: str


class CoffeeShop(CoffeeShopBase):
    id: int
    name: str

    class Config:
        from_attributes = True
