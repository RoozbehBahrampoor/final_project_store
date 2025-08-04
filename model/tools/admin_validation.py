import re


def code_validator(code):
    try:
        code = int(code)
        if code <= 0:
            raise ValueError("Invalid code !!!")
    except:
        raise ValueError("Invalid code !!!")


def name_validator(name):
    if not re.match(r".+", name):
        raise ValueError("Invalid name !!!")


def family_validator(family):
    if not re.match(r".+", family):
        raise ValueError("Invalid family !!!")


def username_validator(username):
    if not re.match(r".+", username):
        raise ValueError("Invalid username !!!")


def password_validator(password):
    password = str(password)
    if not re.match(r"^[a-zA-Z0-9 _-]+$", password):
        raise ValueError("Invalid password !!!")


def locked_validator(locked):
    if not re.match(r"^[01]$", str(locked)):
        raise ValueError("Invalid locked !!!")
