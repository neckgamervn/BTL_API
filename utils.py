from hashlib import sha256 as sh
from time import time


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
