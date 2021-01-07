from fastapi import FastAPI, Header
from typing import Optional
from api.authentication import login, register, logout
from database.models import LoginBody, RegisterBody

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
