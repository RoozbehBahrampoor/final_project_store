import re

def code_validator(code):
    if not (isinstance(code, int) and code > 0):
        raise ValueError("Invalid code !!!")

def region_validator(region):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", region):
        raise ValueError("Invalid region !!!")

def address_validator(address):
    if not re.match(r"^[a-zA-Z0-9\s,.-]{3,100}$", address):
        raise ValueError("Invalid address !!!")

def floor_validator(floor):
    if not (isinstance(floor, int) and floor >= 0):
        raise ValueError("Invalid floor !!!")

def area_validator(area):
    if not (isinstance(area, int) and area > 0):
        raise ValueError("Invalid area !!!")

def rooms_validator(rooms):
    if not (isinstance(rooms, int) and rooms >= 0):
        raise ValueError("Invalid rooms !!!")

def elevator_validator(elevator):
    if not isinstance(elevator, bool):
        raise ValueError("Invalid elevator !!!")

def parking_validator(parking):
    if not isinstance(parking, bool):
        raise ValueError("Invalid parking !!!")

def storage_validator(storage):
    if not isinstance(storage, bool):
        raise ValueError("Invalid storage !!!")

def year_validator(year):
    if not (isinstance(year, int) and year > 0):
        raise ValueError("Invalid year !!!")

def price_validator(price):
    try:
        price = int(price)
        if price <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Invalid price !!!")

def locked_validator(locked):
    if not isinstance(locked, bool):
        raise ValueError("Invalid locked !!!")