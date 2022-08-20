from sqlalchemy.orm import Session

import models
import schemas


def get_user(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_name(name: str, db: Session):
    return db.query(models.User).filter(models.User.name == name).first()


def create_user(user: schemas.UserCreate, db: Session):
    # temp = dict(name=name, age=age)
    db_user = models.User(age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    pass
