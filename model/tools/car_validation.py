import re


def code_validator(code):
    pass


def name_validator(name):
    if not re.match(r'^[\w\s\-]+$', name):
        raise ValueError("Invalid name !!!")


def model_validator(model):
    model = str(model).strip()
    if not re.match(r'^.+$', model):
        raise ValueError("Invalid model !!!")


def color_validator(color):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", color):
        raise ValueError("Invalid color !!!")


def year_validator(year):
    if not re.match(r'^\d{1,4}$', year):
        raise ValueError("Invalid year !!!")


def price_validator(price):
    if not re.match(r'^[0-9.]+$', (price)):
        raise ValueError("Invalid price !!!")


def locked_validator(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", locked):
        raise ValueError("Invalid locked !!!")
