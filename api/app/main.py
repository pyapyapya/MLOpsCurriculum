from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, status
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


from crud import crud_user
from database.tables.user import Base
from schemas.user import UserInfo, UserCreate
from database.database import SessionLocal, engine
from utils import search_user_id, serach_user_name

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	content = {'status_code': 400, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


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
    checking a db connection
    """
    return "OK"


@app.get("/users", response_model=List[UserInfo])
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
    users = crud_user.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=UserInfo)
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

    users = crud_user.get_user(user_id, db)
    return users


@app.post("/users", response_model=UserInfo)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
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

    users = crud_user.create_user(user, db)
    return users


@app.put("/users/{user_id}", response_model=UserInfo)
async def update_user(
    user_id: int, user_info: UserCreate, db: Session = Depends(get_db)
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

    crud_user.update_user(user_id, user_info, db)
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
    user = crud_user.get_user(user_id, db)

    if not isinstance(user_id, int):
        raise HTTPException(status_code=400, detail=f"Invalid User ID: {user_id}")

    has_id = search_user_id(user_id, db)
    if not has_id:
        raise HTTPException(status_code=404, detail=f"The User is not found.")

    crud_user.delete_user(user_id, db)
    return user
