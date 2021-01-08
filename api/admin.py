import shutil
from time import time

from constant import BASE_URL
from database.connect import execute_query
from database.connect import read_sql_query
from utils import on_success, on_fail, un_unicode


def create_post(title, description, url, category_id, image):
    try:
        image_file_url = str(time()) + ".png"
        with open("./image_upload/" + image_file_url, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_file_url = BASE_URL + "image?url=" + image_file_url
        execute_query(
            "INSERT INTO post"
            " (title, description, url_linked, image_url, id_category)"
            " values ('{}','{}','{}','{}','{}')".format(title, description, url, image_file_url, category_id))
        data = read_sql_query("select * from post where image_url='{}'".format(image_file_url))
        id_post = data.values[-1][0]
        return on_success(
            {"id": id_post,
             "title": title,
             "description": description,
             "url": url,
             "image_url": image_file_url,
             "category_id": category_id
             })
    except Exception as err:
        print(err)
        return on_fail()


def edit_post(id_post, title, description, url, category_id, image):
    try:
        image_file_url = str(time()) + ".png"
        with open("./image_upload/" + image_file_url, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_file_url = BASE_URL + "image?url=" + image_file_url
        execute_query(
            "UPDATE post set "
            "title='{}', description='{}', url_linked='{}', image_url='{}', id_category='{}'"
            "where id='{}'"
                .format(title, description, url, image_file_url, category_id, id_post))

        return on_success(
            {"id": id_post,
             "title": title,
             "description": description,
             "url": url,
             "image_url": image_file_url,
             "category_id": category_id
             })
    except Exception as err:
        print(err)
        return on_fail()


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


def get_list_post(id_category, keyword, page):
    try:
        list_output = []
        if id_category == '0':
            list_post = read_sql_query("select * from post").values
        else:
            list_post = read_sql_query("select * from post where id_category = '{}'".format(id_category)).values
        count = 0
        for post in list_post:
            if count >= int(page)*10:
                break
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
                count = count + 1

        return on_success(list_output[-10:])
    except Exception as err:
        print("List post error: ", err)
        return on_fail()
