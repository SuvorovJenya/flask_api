from sqlalchemy import Column, Integer, String
from database.db import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
