from model.entity.car import Car
from model.repository.car_repository import CarRepository
from model.repository.database_creator import create_connection

create_connection()

car = Car(100, "benz", "cls", "Black", "2022", "50000$", 0)

repo = CarRepository()
repo.delete(car.code)
repo.save(car)

print(car)