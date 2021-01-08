from api.authentication import check_existed_token
from database.connect import read_sql_query
from utils import on_success, on_fail, un_unicode
import unicodedata


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

def get_list_post(id_category, keyword):
    try:
        list_output = []
        list_post = read_sql_query("select * from post where id_category = '{}'".format(id_category)).values
        for post in list_post:
            if keyword.lower() in un_unicode(post[2]).lower():
                data = {
                    'id': post[0],
                    'title': post[1],
                    'description': post[2],
                    'url_linked': post[3],
                    'img_url': post[4],
                    'id_category': post[5]
                }
                list_output.append(data)
        return on_success(list_output)
    except Exception as err:
        print("List post error: ", err)
        return on_fail()


