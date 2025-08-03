from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from .models import User
from .schemas import UserCreate, UserRead

app = FastAPI(title="User Profile Service")


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


def get_db():
    with SessionLocal() as db:
        yield db


@app.post("/users", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(**payload.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/healthz")
def health():
    return {"status": "ok"}
