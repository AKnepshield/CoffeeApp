from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from CoffeeApp.db import get_db
from CoffeeApp.user import schemas as user_schemas
from CoffeeApp.user import models as user_models
from CoffeeApp.coffee_shop import schemas as coffee_shop_schemas
from CoffeeApp.coffee_shop import models as coffee_shop_models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str = "Andy Knepshield"):
    return {"message": f"Hello {name}"}


@app.get("/users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(user_models.User).all()
    return users


@app.post("/users/", response_model=user_schemas.User)
async def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = user_models.User(email=user.email, name=user.name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError as e:
        raise HTTPException(
            status_code=409, detail="Duplicate email.  Use different email."
        ) from e
    return db_user


@app.get("/coffee_shops/")
async def get_coffee_shops(db: Session = Depends(get_db)):
    coffee_shops = db.query(coffee_shop_models.CoffeeShop).all()
    return coffee_shops


@app.post("/coffee_shops/", response_model=coffee_shop_schemas.CoffeeShop)
async def create_coffee_shop(
    coffee_shop: coffee_shop_schemas.CoffeeShopCreate, db: Session = Depends(get_db)
):
    db_coffee_shop = coffee_shop_models.CoffeeShop(name=coffee_shop.name)
    db.add(db_coffee_shop)
    db.commit()
    db.refresh(db_coffee_shop)
    return db_coffee_shop
