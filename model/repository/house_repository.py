import sqlite3


class HouseRepository:

    def save(self, house):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """insert into HOUSES
                   (region, address, floor, area, rooms, elevator, parking, storage, year, price, locked)
                   values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [house.region, house.address, house.floor, house.area, house.rooms, house.elevator,
                 house.parking, house.storage, house.year, house.price, house.locked])
            connection.commit()

    def edit(self, house):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "update houses set region=?, address=?, floor=?, area=?, rooms=?, elevator=?, parking=?, storage=?, year=?, price=?, locked=? where code=?",
                [house.region, house.address, house.floor, house.area, house.rooms, house.elevator,
                 house.parking, house.storage, house.year, house.price, house.locked, house.code])
            connection.commit()

    def delete(self, code):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from houses where code = ?", [code])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses")
            house_list = cursor.fetchall()
            return house_list

    def find_by_code(self, code):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where code = ?", [code])
            house = cursor.fetchone()
            return house

    def find_by_region_price(self, region, price):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()

            query = "select * from houses where region like ? and price like ?"
            params = [f"%{region}%", f"%{price}%"]

            cursor.execute(query, params)
            house_list = cursor.fetchall()
            return house_list

    def find_by_region(self, region):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where region like ?", ["%" + region + "%"])
            house_list = cursor.fetchall()
            return house_list

    def find_by_floor(self, floor):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where floor = ?", [floor])
            house = cursor.fetchone()
            return house

    def find_by_area_and_parking(self, area, parking):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where area = ? and parking = ?", [area, parking])
            house = cursor.fetchone()
            return house

    def find_by_price_range(self, start_price, end_price):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where price between ? and ?", [start_price, end_price])
            house = cursor.fetchone()
            return house

    def find_by_price(self, price):
        with sqlite3.connect("store_db.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from houses where price = ?", [price])
            house_list = cursor.fetchall()
            return house_list