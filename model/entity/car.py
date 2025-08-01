class Car:
    def __init__(self, code, name, model, color, year, price, locked=False):
        self.code = code
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.locked = locked

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        code_validator(value)
        self._code = (value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        model_validator(value)
        self._model = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        color_validator(value)
        self._color = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        year_validator(value)
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        locked_validator(value)
        self._locked = (value)

    def __repr__(self):
        return f"{self.__dict__}"
