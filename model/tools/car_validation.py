import re


def code_validator(code):
    if type(code) == int and code > 0:
        raise ValueError("Invalid code !!!")


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name !!!")


def model_validator(model):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", model):
        raise ValueError("Invalid model !!!")


def color_validator(color):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", color):
        raise ValueError("Invalid color !!!")


def year_validator(year):
    if type(year) == int and year > 0:
        raise ValueError("Invalid year !!!")


def price_validator(price):
    if not re.match(r"^[0-9]{6}$", (price)):
        raise ValueError("Invalid price !!!")


def locked_validator(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", locked):
        raise ValueError("Invalid locked !!!")
