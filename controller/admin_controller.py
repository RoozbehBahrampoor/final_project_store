from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository


class AdminController:
    def save(self, name, family, username, password, locked):
        try:
            admin = Admin(None, name, family, username, password, locked)
            admin_repo = AdminRepository()
            admin_repo.save(admin)
            return True, f"Admin saved {admin}"
        except Exception as e:
            return False, f"Error saving admin {e}"

    def edit(self, code, name, family, username, password, locked):
        try:
            admin = Admin(code, name, family, username, password, locked)
            admin_repo = AdminRepository()
            admin_repo.edit(admin)
            return True, f"Admin edited {admin}"
        except Exception as e:
            return False, f"Error editing admin {e}"

    def delete(self, code):
        try:
            admin_repo = AdminRepository()
            admin_repo.delete(code)
            return True, f"Admin removed {code}"
        except Exception as e:
            return False, f"Error removing admin {e}"

    def find_all(self):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_all()
        except Exception as e:
            e.with_traceback()
            return False, f"Error find all admins {e}"

    def find_by_code(self, code):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_code(code)
        except Exception as e:
            return False, f"Error find admins code : {code} Error :{e}"

    def find_by_name_family(self, name, family):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_name_family(name, family)
        except Exception as e:
            return False, f"Error find admins name : {name} - family {family} -- Error :{e}"

    def find_by_username(self, username):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_username(username)
        except Exception as e:
            return False, f"Error find admins username : {username} -- Error :{e}"

    def find_by_username_and_password(self, username, password):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_username_and_password(username, password)
        except Exception as e:
            return False, f"Error find admins username :password {username}:{password}  -- Error :{e}"
