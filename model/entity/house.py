from model.tools.house_validation import *


class House:
    def __init__(self, code, region, address, floor, area, rooms, elevator, parking, storage, year, price,
                 locked=False):
        self.code = code
        self.region = region
        self.address = address
        self.floor = floor
        self.area = area
        self.rooms = rooms
        self.elevator = elevator
        self.parking = parking
        self.storage = storage
        self.year = year
        self.price = price
        self.locked = locked

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        #code_validator(value)
        self._code = value

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        region_validator(value)
        self._region = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        address_validator(value)
        self._address = value

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        floor_validator(value)
        self._floor = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        area_validator(value)
        self._area = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        rooms_validator(value)
        self._rooms = value

    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, value):
        elevator_validator(value)
        self._elevator = value

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, value):
        parking_validator(value)
        self._parking = value

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        storage_validator(value)
        self._storage = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        year_validator(value)
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        # locked_validator(value)
        self._locked = value

    def __repr__(self):
        return f"{self.__dict__}"
