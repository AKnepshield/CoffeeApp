from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from CoffeeApp.db import get_db
from CoffeeApp.user import models, schemas
from CoffeeApp.user.models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str = "Andy Knepshield"):
    return {"message": f"Hello {name}"}


@app.get("/users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
