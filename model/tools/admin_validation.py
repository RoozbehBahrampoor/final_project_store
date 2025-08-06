import re

def code_validator(code):
    if not (isinstance(code, int) and code > 0):
        raise ValueError("Invalid code !!!")

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name !!!")

def family_validator(family):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
        raise ValueError("Invalid family !!!")

def username_validator(username):
    if not (isinstance(username, str) and len(username) >= 3):
        raise ValueError("Username must be at least 3 characters long.")

def password_validator(password):
    if not (isinstance(password, str) and len(password) >= 6):
        raise ValueError("Password must be at least 6 characters long.")

def locked_validator(locked):
    if not isinstance(locked, bool):
        raise ValueError("Invalid locked !!!")