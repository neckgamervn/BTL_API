from hashlib import sha256 as sh
from time import time
from database.connect import read_sql_query
import re


def sha256(text):
    return sh(text.encode('utf-8')).hexdigest()


def new_token(text="random"):
    return sha256(text + str(time()))


def on_success(data=None, message="Thành công"):
    if data is not None:
        return {
            "message": message,
            "data": data
        }
    return {
        "message": message,
    }


def on_fail(message="Thất bại"):
    return {
        "message": message,
    }


def check_existed_token(token):
    existed_user = read_sql_query("select id,username, token from [user] where token='{}'".format(token))
    if len(existed_user.values) > 0:
        id_user = existed_user.values[-1][0],
        username = existed_user.values[-1][1],
        return id_user, username
    return None

def un_unicode(text):
    patterns = {
        '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
        '[đ]': 'd',
        '[èéẻẽẹêềếểễệ]': 'e',
        '[ìíỉĩị]': 'i',
        '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
        '[ùúủũụưừứửữự]': 'u',
        '[ỳýỷỹỵ]': 'y'
    }
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output