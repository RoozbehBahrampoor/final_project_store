from model.repository.admin_repository import AdminRepository
from model.entity.admin import Admin
from model.repository.database_creator import create_connection

# اتصال به پایگاه داده را ایجاد می‌کنیم
create_connection()

# یک شیء ادمین با کد و نام کاربری ثابت ایجاد می‌کنیم
admin = Admin(1, "parsa", "ahmadi", "parsa", "parsa1234", 0)

# یک نمونه از repository ایجاد می‌کنیم
repo = AdminRepository()

# ابتدا رکورد ادمین را بر اساس نام کاربری پیدا می‌کنیم
existing_admin = repo.find_by_username(admin.username)

# اگر رکورد از قبل وجود داشت، آن را حذف می‌کنیم
if existing_admin:
    repo.delete(existing_admin[0])  # existing_admin[0] is the code

# حالا می‌توانیم رکورد جدید را بدون مشکل ذخیره کنیم
repo.save(admin)

print(admin)
print("Admin test executed successfully.")
