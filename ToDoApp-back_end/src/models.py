from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    todos = relationship("ToDo")


class ToDo(Base):

    __tablename__ = "todos"

    todo_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    data = Column(String)
    is_completed = Column(Boolean)
