from sqlalchemy import Column, Integer, String

from CoffeeApp.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)

    def __init__(self, name, email, *args, **kwargs):
        self.name = name
        self.email = email

