from fastapi import FastAPI

from database import execute_query, read_sql_query
from models import LoginBody, RegisterBody

app = FastAPI()


@app.post("/login")
async def login(body: LoginBody):
    df = read_sql_query("select username,password from [user] where username ='{}'".format(body.username))
    if len(df.values) > 0:
        if body.password == df['password'].values[-1]:
            del body.password
            return {
                "message": "Thành công",
                "data": body
            }
    return {
        "message": "Thất bại",
    }


@app.post("/register")
async def register(body: RegisterBody):
    try:
        query = "insert into [user] (username, password, fullname, birthday, phone, gender, token)" \
                " values ('{0}','{1}',N'{2}','{3}','{4}',{5},'{6}')". \
            format(body.username, body.password, body.fullname, body.birthday, body.phone, body.gender,
                   "623674278936478")
        execute_query(query)
        return {
            "message": "Thành công",
            "data": body
        }
    except Exception as err:
        print(err)
        return {
            "message": "Thất bại"
        }
