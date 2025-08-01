class Admin:
    def __init__(self, code, name, family, username, password, locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.locked = locked

    def __repr__(self):
        return f"{self.__dict__}"


