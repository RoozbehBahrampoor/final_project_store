import os

from model.repository.database_creator import create_connection
from view.admin_view import Admin, AdminView
from view.customer_view import CustomerView
from view.car_view import CarView
from view.house_view import HouseView

admin_view = AdminView()
car_view = CarView()
customer_view = CustomerView()
house_view = HouseView()

create_connection()


