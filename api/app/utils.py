from sqlalchemy.orm import Session

from database.tables.user import User

def search_user_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def serach_user_name(name: str, db: Session):
    return db.query(User).filter(User.name == name).first()
