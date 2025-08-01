from model.entity.customer import Customer
from model.repository.customer_repository import CustomerRepository


class CustomerController:
    def save(self, name, family, username, password, phone_number, locked):
        try:
            customer = Customer(None, name, family, username, password, phone_number, locked)
            customer_repo = CustomerRepository()
            customer_repo.save(customer)
            return True, f"Customer saved {customer}"
        except Exception as e:
            return False, f"Error saving customer {e}"

    def edit(self, code, name, family, username, password, phone_number, locked):
        try:
            customer = Customer(code, name, family, username, password, phone_number, locked)
            customer_repo = CustomerRepository()
            customer_repo.edit(customer)
            return True, f"Customer edited {customer}"
        except Exception as e:
            return False, f"Error editing customer {e}"

    def delete(self, code):
        try:
            customer_repo = CustomerRepository()
            customer_repo.delete(code)
            return True, f"Customer removed {code}"
        except Exception as e:
            return False, f"Error removing customer {e}"

    def find_all(self):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_all()
        except Exception as e:
            e.with_traceback()
            return False, f"Error find all customers {e}"

    def find_by_code(self, code):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_by_code(code)
        except Exception as e:
            return False, f"Error find customers code : {code} Error :{e}"

    def find_by_name_family(self, name, family):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_by_name_family(name, family)
        except Exception as e:
            return False, f"Error find customers name : {name} - family {family} -- Error :{e}"

    def find_by_username(self, username):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_by_username(username)
        except Exception as e:
            return False, f"Error find customers username : {username} -- Error :{e}"

    def find_by_username_and_password(self, username, password):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_by_username_and_password(username, password)
        except Exception as e:
            return False, f"Error find customers username :password {username}:{password}  -- Error :{e}"
