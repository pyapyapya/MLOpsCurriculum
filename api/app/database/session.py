from .database import SessionLocal, engine
from .tables.user import Base

Base.metadata.create_all(bind=engine)


def get_db():
    """
    Get Database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
