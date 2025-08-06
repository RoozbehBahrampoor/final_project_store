from model.entity.house import House
from model.repository.house_repository import HouseRepository


class HouseController:
    def __init__(self):
        self.house_repository = HouseRepository()

    def save(self, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked):
        try:
            house = House(None, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked)
            self.house_repository.save(house)
            return True, "House saved successfully"
        except Exception as e:
            return False, str(e)

    def edit(self, code, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked):
        try:
            house = House(code, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked)
            self.house_repository.edit(house)
            return True, "House edited successfully"
        except Exception as e:
            return False, str(e)

    def delete(self, code):
        try:
            self.house_repository.delete(code)
            return True, "House deleted successfully"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            house_list = self.house_repository.find_all()
            return True, house_list
        except Exception as e:
            return False, str(e)

    def find_by_code(self, code):
        try:
            house = self.house_repository.find_by_code(code)
            return True, house
        except Exception as e:
            return False, str(e)

    def find_by_region_price(self, region, price):
        try:
            house_list = self.house_repository.find_by_region_price(region, price)
            return True, house_list
        except Exception as e:
            return False, str(e)

    def find_by_price(self, price):
        try:
            house_list = self.house_repository.find_by_price(price)
            return True, house_list
        except Exception as e:
            return False, str(e)