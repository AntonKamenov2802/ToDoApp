from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password  # TODO: Need to hash the password
    
    db_user = models.User(
        name=user.name,
        surname=user.surname,
        username=user.username,
        email=user.email,
        password=password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo_by_user(db: Session, user_id: int):
    db.query(models.ToDo).filter(models.ToDo.user_id == user_id).all()


def create_user_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_item = models.ToDo(**todo.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
