from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
