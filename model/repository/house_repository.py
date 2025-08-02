import sqlite3


class HouseRepository:
    def connect(self):
        self.connection = sqlite3.connect("store_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, house):
        self.connect()
        self.cursor.execute(
            """insert into HOUSES
               (region, address, floor, area, rooms, elevator, parking, storage, year, price, locked)
               values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [house.region, house.address, house.floor, house.area, house.rooms, house.elevator,
             house.parking, house.storage, house.year, house.price, house.locked])
        self.disconnect(commit=True)

    def edit(self, house):
        self.connect()
        self.cursor.execute(
            "update houses set region=?, address=?, floor=?, area=?, rooms=?, elevator=?, parking=?, storage=?, year=?, price=?, locked=? where code=?",
            [house.code, house.region, house.address, house.floor, house.area, house.rooms, house.elevator,
             house.parking, house.storage, house.year, house.price, house.locked])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from houses where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from houses")
        house_list = self.cursor.fetchall()
        self.disconnect()
        return house_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from houses where code = ?", [code])
        house = self.cursor.fetchone()
        self.disconnect()
        return house

    def find_by_region(self, region):
        self.connect()
        self.cursor.execute("select * from houses where region like ?", ["%" + region + "%"])
        house_list = self.cursor.fetchall()
        self.disconnect()
        return house_list

    def find_by_floor(self, floor):
        self.connect()
        self.cursor.execute("select * from houses where floor = ?", [floor])
        house = self.cursor.fetchone()
        self.disconnect()
        return house

    def find_by_area_and_price(self, area, price):
        self.connect()
        self.cursor.execute("select * from houses where area = ? and price = ?", [area, price])
        house = self.cursor.fetchone()
        self.disconnect()
        return house

    def find_by_price_range(self, start_price, end_price):
        self.connect()
        self.cursor.execute("select * from houses where price between ? and ?", [start_price, end_price])
        house = self.cursor.fetchone()
        self.disconnect()
        return house