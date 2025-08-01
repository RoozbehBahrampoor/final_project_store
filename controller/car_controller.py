from model.entity.car import Car
from model.repository.car_repository import CarRepository


class CarController:
    def save(self, name, model, color, year, price, locked):
        try:
            car = Car(None, name, model, color, year, price, locked)
            car_repo = CarRepository()
            car_repo.save(car)
            return True, f"Car saved {car}"
        except Exception as e:
            return False, f"Error saving car {e}"

    def edit(self, code, name, model, color, year, price, locked):
        try:
            car = Car(code, name, model, color, year, price, locked)
            car_repo = CarRepository()
            car_repo.edit(car)
            return True, f"Car edited {car}"
        except Exception as e:
            return False, f"Error editing car {e}"

    def delete(self, code):
        try:
            car_repo = CarRepository()
            car_repo.delete(code)
            return True, f"Car removed {code}"
        except Exception as e:
            return False, f"Error removing car {e}"

    def find_all(self):
        try:
            car_repo = CarRepository()
            return True, car_repo.find_all()
        except Exception as e:
            e.with_traceback()
            return False, f"Error find all cars {e}"

    def find_by_code(self, code):
        try:
            car_repo = CarRepository()
            return True, car_repo.find_by_code(code)
        except Exception as e:
            return False, f"Error find cars code : {code} Error :{e}"

    def find_by_name_model(self, name, model):
        try:
            car_repo = CarRepository()
            return True, car_repo.find_by_name_model(name, model)
        except Exception as e:
            return False, f"Error find cars name : {name} - model {model} -- Error :{e}"

    def find_by_year(self, year):
        try:
            car_repo = CarRepository()
            return True, car_repo.find_by_year(year)
        except Exception as e:
            return False, f"Error find cars year : {year} -- Error :{e}"

    def find_by_model_and_color(self, model, color):
        try:
            car_repo = CarRepository()
            return True, car_repo.find_by_model_and_color(model, color)
        except Exception as e:
            return False, f"Error find cars model :color {model}:{color}  -- Error :{e}"
