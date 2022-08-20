from sqlalchemy import Column, Integer, String

from database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
