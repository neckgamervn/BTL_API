from database.connect import read_sql_query, execute_query
from utils import on_success, on_fail
import shutil
from time import time
from constant import BASE_URL


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
