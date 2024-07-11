from sqlalchemy import Column, String, Integer
from CoffeeApp.db import Base


class CoffeeShop(Base):
    __tablename__ = "coffee_shops"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __init__(self, name, *args, **kwargs):
        self.name = name
