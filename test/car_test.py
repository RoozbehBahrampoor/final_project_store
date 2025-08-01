from model.entity.car import Car
from model.repository.car_repository import CarRepository

car = Car(100, "Benz", "cls", "Black", "2022", "50000$", 0)

repo = CarRepository()
repo.save(car)
