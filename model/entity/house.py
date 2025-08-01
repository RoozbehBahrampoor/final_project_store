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
        self.year_built = year
        self.price = price
        self.locked = locked

    def __repr__(self):
        return f"{self.__dict__}"



