class Customer:
    def __init__(self, code, name, family, username, password, phone_number, locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.locked = locked

    def __repr__(self):
        return f"{self.__dict__}"
