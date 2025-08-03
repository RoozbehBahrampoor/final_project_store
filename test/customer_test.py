from model.repository.customer_repository import CustomerRepository
from model.entity.customer import Customer
from model.repository.database_creator import create_connection

# اتصال به پایگاه داده را ایجاد می‌کنیم
create_connection()

# یک شیء مشتری با کد و نام کاربری ثابت ایجاد می‌کنیم
customer = Customer(200, "ali", "bahrami", "ALI123", "ali345", "09193647381", 0)

# یک نمونه از repository ایجاد می‌کنیم
repo = CustomerRepository()

# ابتدا رکورد مشتری را بر اساس نام کاربری پیدا می‌کنیم
existing_customer = repo.find_by_username(customer.username)

# اگر رکورد از قبل وجود داشت، آن را حذف می‌کنیم
if existing_customer:
    repo.delete(existing_customer[0])  # existing_customer[0] is the code

# حالا می‌توانیم رکورد جدید را بدون مشکل ذخیره کنیم
repo.save(customer)

print(customer)
print("Customer test executed successfully.")