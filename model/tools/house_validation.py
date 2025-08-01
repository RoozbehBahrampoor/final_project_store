import re


def code_validator(code):
    if type(code) == int and code > 0:
        raise ValueError("Invalid code !!!")


def region_validator(region):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", region):
        raise ValueError("Invalid region !!!")


def address_validator(address):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", address):
        raise ValueError("Invalid address !!!")


def floor_validator(floor):
    if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', floor):
        raise ValueError("Invalid floor !!!")


def area_validator(area):
    if not re.match(r"^[0-9]{4}-[0-9]{2}$", area):
        raise ValueError("Invalid area !!!")


def rooms_validator(rooms):
    if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", rooms):
        raise ValueError("Invalid rooms !!!")


def elevator_validator(elevator):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", elevator):
        raise ValueError("Invalid elevator !!!")


def parking_validator(parking):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", parking):
        raise ValueError("Invalid parking !!!")


def storage_validator(storage):
    if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', storage):
        raise ValueError("Invalid storage !!!")


def year_validator(year):
    if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', year):
        raise ValueError("Invalid year !!!")


def price_validator(price):
    if not re.match(r"^[0-9]{6}$", str(price)):
        raise ValueError("Invalid price !!!")


def locked_validator(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", locked):
        raise ValueError("Invalid locked !!!")
