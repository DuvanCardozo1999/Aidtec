import datetime
from pydantic import BaseModel

class TokenCreate(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    status: bool
    created_date: datetime.datetime

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class Config:
        orm_mode = True  

class LoginRequest(BaseModel):
    email: str
    password: str

