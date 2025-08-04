import sqlite3


class CarRepository:
    def connect(self):
        self.connection = sqlite3.connect("store_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, car):
        self.connect()
        self.cursor.execute(
            """insert into CARS
                   (name, model, color, year, price, locked)
               values (?, ?, ?, ?, ?, ?)""",
            [car.name, car.model, car.color, car.year, car.price, car.locked])
        self.disconnect(commit=True)

    def edit(self, car):
        self.connect()
        self.cursor.execute("update cars set name=?, model=?, color=?, year=?, price=?, locked=? where code=?",
                            [car.name, car.model, car.color, car.year, car.price, car.locked,
                             car.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from cars where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from cars")
        car_list = self.cursor.fetchall()
        self.disconnect()
        return car_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from cars where code = ?", [code])
        car = self.cursor.fetchone()
        self.disconnect()
        return car

    def find_by_name_model(self, name, model):
        self.connect()
        self.cursor.execute("select * from cars where name like ? and model like ?", [name + "%", model + "%"])
        car_list = self.cursor.fetchall()
        self.disconnect()
        return car_list

    def find_by_color(self, color):
        self.connect()
        self.cursor.execute("select * from cars where color = ?", [color])
        car = self.cursor.fetchone()
        self.disconnect()
        return car

    def find_by_name_and_price(self, name, price):
        self.connect()
        self.cursor.execute("select * from cars where name = ? and price = ?", [name, price])
        car = self.cursor.fetchone()
        self.disconnect()
        return car