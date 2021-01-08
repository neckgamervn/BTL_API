from fastapi import FastAPI, Header
from typing import Optional
from api.authentication import login, register, logout, check_existed_token
from database.models import LoginBody, RegisterBody
from api.admin import get_list_category, get_list_post
from utils import on_fail

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


@app.get("/get_list_category")
def _get_list_category(token: Optional[str] = Header(None)):
    return get_list_category() if check_existed_token(token) is not None else on_fail()

@app.get("/get_list_post")
def _get_list_post(token: Optional[str] = Header(None),id_category='0',keyword=''):
    return get_list_post(id_category, keyword) if check_existed_token(token) is not None else on_fail()