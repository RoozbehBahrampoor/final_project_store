import re


def code_validator(code):
    if type(code) == int and code > 0:
        raise ValueError("Invalid code !!!")


def region_validator(region):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", region):
        raise ValueError("Invalid region !!!")


def address_validator(address):
    if not re.match(r"^[a-zA-Z0-9\s,.-]{3,100}$", address):
        raise ValueError("Invalid address !!!")


def floor_validator(floor):
    if type(floor) == str and code > 0:
        raise ValueError("Invalid floor !!!")


def area_validator(area):
    if type(area) == str and area > 0:
        raise ValueError("Invalid area !!!")


def rooms_validator(rooms):
    if type(rooms) == str and rooms > 0:
        raise ValueError("Invalid rooms !!!")


def elevator_validator(elevator):
    if str(elevator) not in ["0", "1"]:
        raise ValueError("Invalid elevator !!!")


def parking_validator(parking):
    if str(elevator) not in ["0", "1"]:
        raise ValueError("Invalid parking !!!")


def storage_validator(storage):
    if str(elevator) not in ["0", "1"]:
        raise ValueError("Invalid storage !!!")


def year_validator(year):
    if type(year) == int and year > 0:
        raise ValueError("Invalid year !!!")


def price_validator(price):
    if not re.match(r"^[0-9]{6}$", (price)):
        raise ValueError("Invalid price !!!")


def locked_validator(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", locked):
        raise ValueError("Invalid locked !!!")
