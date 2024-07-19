from pydantic import BaseModel, ConfigDict


class CoffeeShopBase(BaseModel):
    name: str


class CoffeeShopCreate(CoffeeShopBase):
    name: str


class CoffeeShop(CoffeeShopBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
