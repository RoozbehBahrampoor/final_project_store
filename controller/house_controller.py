from model.entity.house import House
from model.repository.house_repository import  HouseRepository

class HouseController:
    def save(self, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked):
        try:
            house = House(None, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked)
            house_repo = HouseRepository()
            house_repo.save(house)
            return True, f"House saved {house}"
        except Exception as e:
            return False, f"Error saving house {e}"

    def edit(self, code, region, address, floor, area, rooms, elevator, parking, storage, year, price, locked):
        try:
            house = House(code, region, address, floor, area, rooms, elevator, parking, storage, year, price,
                          locked)
            house_repo = HouseRepository()
            house_repo.edit(house)
            return True, f"House edited {house}"
        except Exception as e:
            return False, f"Error editing house {e}"

    def delete(self, code):
        try:
            house_repo = HouseRepository()
            house_repo.delete(code)
            return True, f"House removed {code}"
        except Exception as e:
            return False, f"Error removing house {e}"

    def find_all(self):
        try:
            house_repo = HouseRepository()
            return True, house_repo.find_all()
        except Exception as e:
            e.with_traceback()
            return False, f"Error find all houses {e}"

    def find_by_code(self, code):
        try:
            house_repo = HouseRepository()
            return True, house_repo.find_by_code(code)
        except Exception as e:
            return False, f"Error find houses code : {code} Error :{e}"

    def find_by_region_price(self, region, price):
        try:
            house_repo = HouseRepository()
            return True, house_repo.find_by_region_price(region, price)
        except Exception as e:
            return False, f"Error find houses region : {region} - price {price} -- Error :{e}"

    def find_by_year(self, year):
        try:
            house_repo = HouseRepository()
            return True, house_repo.find_by_year(year)
        except Exception as e:
            return False, f"Error find houses year : {year} -- Error :{e}"

    def find_by_area_and_parking(self, area, parking):
        try:
            house_repo = HouseRepository()
            return True, house_repo.find_by_area_and_parking(area, parking)
        except Exception as e:
            return False, f"Error find houses area :parking {area}:{parking}  -- Error :{e}"
