from pydantic import BaseModel


class LoginBody(BaseModel):
    username: str
    password: str


class RegisterBody(BaseModel):
    username: str
    password: str
    fullname: str
    birthday: str
    phone: str
    gender: int
