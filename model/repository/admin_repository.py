import sqlite3


class AdminRepository:
    def connect(self):
        self.connection = sqlite3.connect("store_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, admin):
        self.connect()
        self.cursor.execute(
            """insert into ADMINS
                   (name, family, username, password, locked)
               values (?, ?, ?, ?, ?, ?)""",
            [admin.name, admin.family, admin.username, admin.password, admin.locked])
        self.disconnect(commit=True)

    def edit(self, admin):
        self.connect()
        self.cursor.execute("update admins set name=?, family=?, username=?, password=?, locked=?where code=?",
                            [admin.name, admin.family, admin.username, admin.password, admin.locked,
                             admin.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from admins where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from admins")
        admin_list = self.cursor.fetchall()
        self.disconnect()
        return admin_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from admins where code = ?", [code])
        admin = self.cursor.fetchone()
        self.disconnect()
        return admin

    def find_by_name_family(self, name, family):
        self.connect()
        self.cursor.execute("select * from admins where name like ? and family like ?", [name + "%", family + "%"])
        admin_list = self.cursor.fetchall()
        self.disconnect()
        return admin_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from admins where username = ?", [username])
        admin = self.cursor.fetchone()
        self.disconnect()
        return admin

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from admins where username = ? and password = ?", [username, password])
        admin = self.cursor.fetchone()
        self.disconnect()
        return admin
