from fastapi import FastAPI, Header
from typing import Optional
from api.authentication import login, register, logout, check_existed_token
from database.models import LoginBody, RegisterBody
from admin.listPost import get_list_category

app = FastAPI()


@app.post("/login")
def _login(body: LoginBody):
    return login(body)


@app.post("/register")
def _register(body: RegisterBody):
    return register(body)


@app.post("/logout")
def _logout(token: Optional[str] = Header(None)):
    return logout(token)

@app.post("/get_list_category")
def _get_list_category(token: Optional[str] = Header(None)):
    return get_list_category(token)
