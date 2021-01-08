from api.authentication import check_existed_token
from database.connect import read_sql_query
from utils import on_success, on_fail


def create_post(token):
    return on_success()


def get_list_category():
    try:
        list_output = []
        list_category = read_sql_query("select id, name from category").values
        for category_id in list_category:
            data = {
                'id': category_id[0],
                'name': category_id[1]
            }
            list_output.append(data)

        return on_success(list_output)
    except Exception as err:
        print(err)
        return on_fail()
