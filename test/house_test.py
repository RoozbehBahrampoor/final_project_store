from model.repository.house_repository import HouseRepository
from model.entity.house import House
from model.repository.database_creator import create_connection

# اتصال به پایگاه داده را ایجاد می‌کنیم
create_connection()

# مقادیر عددی را به جای متن، به صورت عدد صحیح وارد می‌کنیم
house = House(
    500,
    "Ekbatan",
    "Block5",
    2,
    5,
    3,
    True,   # از مقادیر بولی به جای متن استفاده می‌کنیم
    True,
    True,
    2005,
    150000,
    False
)

# یک نمونه از repository ایجاد می‌کنیم
repo = HouseRepository()

# ابتدا رکورد خانه را بر اساس کد پیدا کرده و حذف می‌کنیم
# (چون در این حالت کد را دستی وارد می‌کنیم، حذف بر اساس کد مناسب است)
existing_house = repo.find_by_code(house.code)
if existing_house:
    repo.delete(existing_house[0])

# حالا می‌توانیم رکورد جدید را بدون مشکل ذخیره کنیم
repo.save(house)

print(house)
print("House test executed successfully.")