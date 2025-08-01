from model.repository.admin_repository import AdminRepository
from model.entity.admin import Admin

admin = Admin(1, "parsa", "ahmadi", "parsa", "parsa1234", 0)

repo = AdminRepository()
repo.save(admin)
