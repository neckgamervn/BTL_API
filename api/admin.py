from database.connect import execute_query, read_sql_query
from database.models import LoginBody, RegisterBody
from utils import new_token, sha256, on_success, on_fail


def create_post(token):
    return on_success()
