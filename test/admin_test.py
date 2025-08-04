from model.repository.admin_repository import AdminRepository
from model.entity.admin import Admin
from model.repository.database_creator import create_connection

create_connection()

admin = Admin(1, "parsa", "ahmadi", "parsa", "parsa1234", 0)

repo = AdminRepository()

existing_admin = repo.find_by_username(admin.username)

if existing_admin:
    repo.delete(existing_admin[0])

repo.save(admin)

print(admin)