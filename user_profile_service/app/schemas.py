from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    display_name: str

class UserRead(UserCreate):
    id: int

    class Config:
        orm_mode = True
