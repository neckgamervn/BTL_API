from database.connect import execute_query, read_sql_query
from database.models import LoginBody, RegisterBody
from utils import new_token, sha256, on_success, on_fail, check_existed_token


def login(body: LoginBody):
    try:
        df = read_sql_query("select username,password from [user] where username ='{}'".format(body.username))
        if len(df.values) > 0:
            if sha256(body.password) == df['password'].values[-1]:
                token = new_token(body.username)
                execute_query("update [user] SET token = '{}' where username ='{}'".format(token,
                                                                                           body.username))
                del body.password
                return on_success({
                    'username': body.username,
                    'token': token
                })
        return on_fail("Sai tài khoản hoặc mật khẩu")
    except Exception as err:
        print(err)
        return on_fail()


def register(body: RegisterBody):
    try:
        check_existed_user = read_sql_query("select username from [user] where username='{}'".format(body.username))
        if len(check_existed_user.values) == 0:
            password = sha256(body.password)
            query = "insert into [user] (username, password, fullname, birthday, phone, gender, token)" \
                    " values ('{0}','{1}',N'{2}','{3}','{4}',{5},'{6}')". \
                format(body.username, password, body.fullname, body.birthday, body.phone, body.gender,
                       new_token(body.username))
            execute_query(query)
        else:
            return on_fail("Tài khoản đã tồn tại")
        del body.password
        return on_success(body)
    except Exception as err:
        print(err)
        return on_fail()


def logout(token):
    try:
        _, username = check_existed_token(token)
        execute_query("update [user] SET token = NULL where token ='{}'".format(token))
        data = {
            'username': username
        }
        return on_success(data)
    except Exception as err:
        print(err)
        return on_fail()
