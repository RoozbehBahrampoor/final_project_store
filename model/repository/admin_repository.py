import sqlite3


class AdminRepository:
    def save(self, admin):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO table_name (FIELD) VALUES (%s,%s,%s,%s,%s,%s)",
            [data])
        connection.commit()
        cusor.close()
        connection.close()

    def edit(self, admin):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        connection.commit()
        cusor.close()
        connection.close()

    def delete(self, code):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        connection.commit()
        cusor.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cusor.close()
        connection.close()

    def find_by_code(self, code):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cusor.close()
        connection.close()

    def find_by_name_family(self, name, family):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cusor.close()
        connection.close()

    def find_by_username(self, username):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cusor.close()
        connection.close()

    def find_by_username_and_password(self, username, password):
        connection = sqlite3.connect("store_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cusor.close()
        connection.close()
