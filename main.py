import os

from model.repository.database_creator import create_connection
from view.admin_view import Admin, AdminView
from view.customer_view import CustomerView
from view.car_view import CarView
from view.house_view import HouseView

admin_view = AdminView()
customer_view = CustomerView()
car_view = CarView()
house_view = HouseView()

create_connection()
