from sqlalchemy.orm import Session

import models


def search_user_id(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def serach_user_name(name: str, db: Session):
    return db.query(models.User).filter(models.User.name == name).first()
