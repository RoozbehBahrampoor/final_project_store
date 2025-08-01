from model.repository.customer_repository import CustomerRepository
from model.entity.customer import Customer

customer = Customer(200, "ali", "bahrami", "ALI123", "ali345", "09193647381", 0)

repo = CustomerRepository()
repo.save(customer)
