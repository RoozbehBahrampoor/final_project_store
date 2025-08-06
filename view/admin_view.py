from controller import admin_controller
from controller.admin_controller import AdminController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from model.entity.admin import Admin


class AdminView:
    def __init__(self) -> None:
        self.win = Tk()
        self.win.title("Admin View")
        self.win.geometry("1000x600")

        #  code
        Label(self.win, text="Code").place(x=20, y=20)
        self.code = IntVar()
        Entry(self.win, textvariable=self.code, width=23, state="readonly").place(x=120, y=20)

        # name
        Label(self.win, text="Name").place(x=20, y=70)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name, width=23).place(x=120, y=70)

        # family
        Label(self.win, text="Family").place(x=20, y=120)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family, width=23).place(x=120, y=120)

        # user_name
        Label(self.win, text="User Name").place(x=20, y=170)
        self.user_name = StringVar()
        Entry(self.win, textvariable=self.user_name, width=23).place(x=120, y=170)

        # password
        Label(self.win, text="Password").place(x=20, y=220)
        self.password = StringVar()
        Entry(self.win, textvariable=self.password, show="*", width=23).place(x=120, y=220)

        # locked
        Label(self.win, text="Locked").place(x=20, y=270)
        self.locked = BooleanVar()
        Checkbutton(self.win, text="Locked", variable=self.locked).place(x=120, y=270)

        # # search_by_name_family
        Label(self.win, text="Search by Name").place(x=300, y=20)
        self.search_name = StringVar()
        self.search_name_txt = Entry(self.win, textvariable=self.search_name, width=23, fg="gray64")
        self.search_name_txt.bind("<KeyRelease>", self.search_name_family)
        self.search_name_txt.place(x=420, y=20)

        Label(self.win, text="Search by Family").place(x=550, y=20)
        self.search_family = StringVar()
        self.search_family_txt = Entry(self.win, textvariable=self.search_family, width=23, fg="gray64")
        self.search_family_txt.bind("<KeyRelease>", self.search_name_family)
        self.search_family_txt.place(x=670, y=20)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6], show="headings")
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="User Name")
        self.table.heading(5, text="Password")
        self.table.heading(6, text="Locked")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=60)

        self.table.tag_configure("OK", background="lightgreen")
        self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_admin)
        self.table.place(x=300, y=100, height=460)

        Button(self.win, text="Save", command=self.save_click, width=34, height=2).place(x=20, y=450)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=520)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=520)

        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        admin_controller = AdminController()
        status, message = admin_controller.save(
            self.name.get(),
            self.family.get(),
            self.user_name.get(),
            self.password.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        admin_controller = AdminController()
        status, message = admin_controller.edit(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.user_name.get(),
            self.password.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        admin_controller = AdminController()
        status, message = admin_controller.delete(
            self.code.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, admin_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)

            for admin in admin_list:
                self.table.insert(
                    "",
                    END,
                    values=admin,
                    tags="Locked" if admin[5] else "OK",
                )
        else:
            msg.showerror("Error", "Error getting admins data")

    def reset_form(self) -> None:
        self.code.set(0)
        self.name.set("")
        self.family.set("")
        self.user_name.set("")
        self.password.set("")
        self.locked.set(False)
        admin_controller = AdminController()
        status, admin_list = admin_controller.find_all()
        self.show_data_on_table(status, admin_list)

    def search_name_family(self, event):
        admin_controller = AdminController()
        status, admin_list = admin_controller.find_by_name_family(self.search_name.get(), self.search_family.get())
        self.show_data_on_table(status, admin_list)

    def select_admin(self, event):
        selected_item = self.table.focus()
        if not selected_item:
            return

        values = self.table.item(selected_item)["values"]

        try:
            # تبدیل مقدار 'locked' به بولی قبل از ارسال به کلاس Admin
            values = list(values)
            values[5] = bool(values[5])

            admin = Admin(*values)
            self.code.set(admin.code)
            self.name.set(admin.name)
            self.family.set(admin.family)
            self.user_name.set(admin.username)
            self.password.set(admin.password)
            self.locked.set(admin.locked)
        except Exception as e:
            msg.showerror("Selection Error", f"An error occurred: {e}")
