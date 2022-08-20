from typing import List, Optional, Union

from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
from utils import search_user_id, serach_user_name

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """
    Get Database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def health_check():
    """
    health_check that is checking a db connection

    Returns
    -------
    _type_
        _description_
    """
    return "OK"


@app.get("/users", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    """
    Get All User Lists

    Parameters
    ----------
    db : Session, optional
        _description_, by default Depends(get_db)

    Returns
    -------
    _type_
        _description_
    """
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    get_user _summary_

    Parameters
    ----------
    user_id : int
        _description_
    db : Session, optional
        _description_, by default Depends(get_db)

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    HTTPException
        _description_
    HTTPException
        _description_
    """
    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    has_id = search_user_id(user_id, db)
    if not has_id:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    users = crud.get_user(user_id, db)
    return users


@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserInfo, db: Session = Depends(get_db)):
    """
    Create a user in the database

    Parameters
    ----------
    user : schemas.UserInfo
        _description_
    db : Session, optional
        _description_, by default Depends(get_db)

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    HTTPException
        _description_
    HTTPException
        _description_
    """
    if user.age <= 0:
        raise HTTPException(status_code=400, detail="age parameter is must be integer.")

    has_name = serach_user_name(user.name, db)
    if has_name:
        raise HTTPException(status_code=409, detail="The user already exists.")

    users = crud.create_user(user, db)
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int, user_info: schemas.UserInfo, db: Session = Depends(get_db)
):
    """
    Update a user in the database

    Parameters
    ----------
    user_id : int
        _description_
    user_info : schemas.UserInfo
        _description_
    db : Session, optional
        _description_, by default Depends(get_db)

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    HTTPException
        _description_
    HTTPException
        _description_
    HTTPException
        _description_
    HTTPException
        _description_
    """
    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    if user_info.age <= 0:
        raise HTTPException(status_code=400, detail="age parameter is must be integer.")

    has_id = search_user_id(user_id, db)
    if not has_id:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    has_name = serach_user_name(user_info.name, db)
    if has_name:
        raise HTTPException(status_code=409, detail="The user already exists.")

    crud.update_user(user_id, user_info, db)
    return {"id": user_id, **user_info.dict()}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user in the database

    Parameters
    ----------
    user_id : int
        _description_
    db : Session, optional
        _description_, by default Depends(get_db)

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    HTTPException
        _description_
    HTTPException
        _description_
    """
    user = crud.get_user(user_id, db)

    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    has_id = search_user_id(user_id, db)
    if not has_id:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    crud.delete_user(user_id, db)
    return user
