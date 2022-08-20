from sqlalchemy.orm import Session

from database.tables.user import User
from schemas.user import UserCreate


def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(user: UserCreate, db: Session):
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, user_info: UserCreate, db: Session):
    update_user = get_user(user_id, db)
    update_user.name = user_info.name
    update_user.age = user_info.age
    db.commit()
    return update_user


def delete_user(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
