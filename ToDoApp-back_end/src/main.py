
from fastapi import FastAPI

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/login')
async def login(log_in: LogIn):
    """
    Check in the database if there is a user with this log-in
    """
    return log_in


@app.post("/register")
async def register(register: Register):
    """
    Check if data is okay and add user to the database
    """
    
    return register
