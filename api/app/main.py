from typing import Union, Optional

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel


import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def health_check():
    return {"status": "OK"}


@app.get("/users", response_model=schemas.User)
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_user(user_id, db)
    return users


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # user = crud.get_user_name(name, db)
    # if user:
    #     raise HTTPException(status_code=400, detail="User name")
    # user = schemas.UserCreate(name=name, age=age)
    users = crud.create_user(user, db)
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, db: Session = Depends(get_db)):
    pass


@app.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    users = crud.delete_user(user_id)
    pass
