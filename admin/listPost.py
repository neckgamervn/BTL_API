from utils import on_success, on_fail
from api.authentication import check_existed_token
from database.connect import read_sql_query, execute_query
def get_list_category(token):
    try:
        existed_user = check_existed_token(token)['data']['username']
        list_output = []
        list_category = read_sql_query("select id, name from category").values

        for category in list_category:
            data = {
                'id': category[0],
                'name': category[1]
            }
            list_output.append(data)

        return on_success(list_output)
    except Exception as err:
        print(err)
        return on_fail()



