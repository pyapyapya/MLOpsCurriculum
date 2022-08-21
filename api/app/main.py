from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from crud import crud_user
from schemas.user import UserCreate, UserInfo
from database.session import get_db

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    content = {"status_code": 400, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


@app.get("/")
async def health_check():
    """
    checking a DB connection
    """
    return "OK"


@app.get("/users", response_model=List[UserInfo])
async def get_users(db: Session = Depends(get_db)):
    """
    Get All User Lists

    Parameters
    ----------
    db : Session, optional

    Returns
    -------
    List[User]
        User information List
    """
    users = crud_user.find_all(db)
    return users


@app.get("/users/{user_id}", response_model=UserInfo)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get User Information

    Parameters
    ----------
    user_id : int
    db : Session, optional

    Returns
    -------
    User
        get user

    Raises
    ------
    HTTPException
        status_code=400, Invalid User ID: {user_id}
    HTTPException
        status_code=404, The User is not found.
    """
    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    user = crud_user.find(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail=f"The User is not found.")
    print(type(user))
    return user


@app.post("/users", response_model=UserInfo)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a user in the database

    Parameters
    ----------
    user : schemas.UserInfo
        name: str (max_length<=16)
        age: int (0 < age <= 120)
    db : Session, optional

    Returns
    -------
    User
        Created User Information

    Raises
    ------
    HTTPException
        status_cod=400, Age parameter is must be integer.
    HTTPException
        status_code=409, The user already exists.
    """
    if user.age <= 0:
        raise HTTPException(status_code=400, detail="Age parameter is must be integer.")

    has_name = crud_user.find_name(user.name, db)
    if has_name:
        raise HTTPException(status_code=409, detail="The user already exists.")

    users = crud_user.create(user, db)
    return users


@app.put("/users/{user_id}", response_model=UserInfo)
async def update_user(
    user_id: int, user: UserCreate, db: Session = Depends(get_db)
):
    """
    Update a user in the database

    Parameters
    ----------
    user_id : int
    user : schemas.UserInfo
        name: str (max_length<=16)
        age: int (0 < age <= 120)
    db : Session, optional

    Returns
    -------
    User
        Updated User Information

    Raises
    ------
    HTTPException
        status_code=400, Invalid User ID: {user_id}
    HTTPException
        status_cod=400, Age parameter is must be integer.
    HTTPException
        status_code=404, The User is not found.
    HTTPException
        status_code=409, The user already exists.
    """
    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    if user.age <= 0:
        raise HTTPException(status_code=400, detail="Age parameter is must be integer.")

    has_id = crud_user.find(user_id, db)
    if not has_id:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    has_name = crud_user.find_name(user.name, db)
    if has_name:
        raise HTTPException(status_code=409, detail="The user already exists.")

    crud_user.update(user_id, user, db)
    return {"id": user_id, **user.dict()}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user in the database

    Parameters
    ----------
    user_id : int
    db : Session, optional

    Returns
    -------
    User
        Deleted User Information
        (user_id, name, age)

    Raises
    ------
    HTTPException
        status_code=400, Invalid User ID: {user_id}
    HTTPException
        status_code=404, The User is not found.
    """

    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    user = crud_user.find(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    crud_user.delete(user_id, db)
    return user
