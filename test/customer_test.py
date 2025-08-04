from model.repository.customer_repository import CustomerRepository
from model.entity.customer import Customer
from model.repository.database_creator import create_connection

create_connection()

customer = Customer(200, "ali", "bahrami", "ALI123", "ali345", "09193647381", 0)

repo = CustomerRepository()

existing_customer = repo.find_by_username(customer.username)

if existing_customer:
    repo.delete(existing_customer[0])

repo.save(customer)

print(customer)