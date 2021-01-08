from typing import Optional

from fastapi import FastAPI, Header, Form, File, UploadFile
from fastapi.responses import FileResponse

from api.admin import create_post, edit_post
from api.admin import get_list_category, get_list_post
from api.authentication import login, register, logout, check_existed_token
from database.models import LoginBody, RegisterBody
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


@app.post("/create_post")
def _create_post(token: Optional[str] = Header(None),
                 image: UploadFile = File(...),
                 title: str = Form(...),
                 description: str = Form(...),
                 url: str = Form(...),
                 category_id: str = Form(...),
                 ):
    return create_post(title, description, url, category_id, image) if check_existed_token(
        token) is not None else on_fail()


@app.post("/edit_post")
def _edit_post(token: Optional[str] = Header(None),
               image: UploadFile = File(...),
               id_post: str = Form(...),
               title: str = Form(...),
               description: str = Form(...),
               url: str = Form(...),
               category_id: str = Form(...),
               ):
    return edit_post(id_post, title, description, url, category_id, image) if check_existed_token(
        token) is not None else on_fail()


@app.get("/image")
def _image(url):
    print(url)
    return FileResponse("./image_upload/" + url)


@app.get("/get_list_post")
def _get_list_post(token: Optional[str] = Header(None), id_category='0', keyword=''):
    return get_list_post(id_category, keyword) if check_existed_token(token) is not None else on_fail()
