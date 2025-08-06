import re

def code_validator(code):
    if not (isinstance(code, int) and code > 0):
        raise ValueError("Invalid code !!!")

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name !!!")

def model_validator(model):
    if not (isinstance(model, str) and len(model) >= 3):
        raise ValueError("Model must be at least 3 characters long.")

def color_validator(color):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", color):
        raise ValueError("Invalid color !!!")

def year_validator(year):
    if not (isinstance(year, int) and year > 0):
        raise ValueError("Invalid year !!!")

def price_validator(price):
    try:
        if isinstance(price, str):
            price = int(price)
        if price <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Invalid price !!!")

def locked_validator(locked):
    if not isinstance(locked, bool):
        raise ValueError("Invalid locked !!!")