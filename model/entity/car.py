class Car:
    def __init__(self, code, name, model, color, year, price, locked=False):
        self.code = code
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.locked = locked

    def __repr__(self):
        return f"{self.__dict__}"

