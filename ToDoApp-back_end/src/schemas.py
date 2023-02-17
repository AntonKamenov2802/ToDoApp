from pydantic import BaseModel


class TodoBase(BaseModel):
    data: str
    is_completed: bool


class TodoCreate(BaseModel):
    pass


class Todo(BaseModel):
    todo_id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    surname: str
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    todos: list[Todo] = []

    class Config:
        orm_mode = True
