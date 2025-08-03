from model.repository.house_repository import HouseRepository
from model.entity.house import House
from model.repository.database_creator import create_connection

create_connection()

house = House(500,"Ekbatan","Block5",2,5,3,True,   True,True, 2005,150000,False)

repo = HouseRepository()

existing_house = repo.find_by_code(house.code)

if existing_house:
    repo.delete(existing_house[0])

repo.save(house)

print(house)




