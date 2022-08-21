from datetime import datetime
from unittest.util import _MAX_LENGTH

from sqlalchemy import Column, DateTime, Integer, String

from database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    Column(
        "create_date", DateTime(timezone=True), nullable=False, default=datetime.now
    ),
