from sqlalchemy.orm import Session

import models
import schemas


def get_user(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_name(id: int, db: Session):
    # return db.get(models.User, id)
    return db.query(models.User).filter(models.User.id == id).first()


def create_user(user: schemas.UserCreate, db: Session):
    db_user = models.User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
