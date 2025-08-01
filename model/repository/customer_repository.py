import sqlite3


class CustomerRepository:
    def connect(self):
        self.connection = sqlite3.connect("store_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            """insert into CUSTOMERS
                   (name, family, username, password, phone_number, locked)
               values (?, ?, ?, ?, ?, ?)""",
            [customer.name, customer.family, customer.username, customer.password,
             customer.phone_number, customer.locked])
        self.disconnect(commit=True)

    def edit(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set name=?, family=?, username=?, password=?, password=?, locked=?where code=?",
            [customer.name, customer.family, customer.username, customer.password,
             customer.phone_number, customer.locked,
             customer.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from customers where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from customers")
        customer_list = self.cursor.fetchall()
        self.disconnect()
        return customer_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from customers where code = ?", [code])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer

    def find_by_name_family(self, name, family):
        self.connect()
        self.cursor.execute("select * from customers where name like ? and family like ?", [name + "%", family + "%"])
        customer_list = self.cursor.fetchall()
        self.disconnect()
        return customer_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from customers where username = ?", [username])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer

    def find_by_username_and_phone_number(self, username, phone_number):
        self.connect()
        self.cursor.execute("select * from customers where username = ? and phone_number = ?", [username, phone_number])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer
