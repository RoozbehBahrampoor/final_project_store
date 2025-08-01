from controller import customer_controller
from controller.customer_controller import CustomerController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from model.entity.customer import Customer


class CustomerView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Customer View")
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
        Entry(self.win, textvariable=self.password, width=23).place(x=120, y=220)

        # phone_number
        Label(self.win, text="Phone_number").place(x=20, y=270)
        self.phone_number = StringVar()
        Entry(self.win, textvariable=self.phone_number, width=23).place(x=120, y=270)

        # locked
        Label(self.win, text="Locked").place(x=20, y=320)
        self.locked = BooleanVar()
        Checkbutton(self.win, text="Locked", variable=self.locked).place(x=120, y=320)

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

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Username")
        self.table.heading(5, text="Password")
        self.table.heading(6, text="Phone_number")
        self.table.heading(7, text="Locked")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=60)

        self.table.tag_configure("OK", background="lightgreen")
        self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_customer)
        self.table.place(x=300, y=100, height=460)

        Button(self.win, text="Save", command=self.save_click, width=34, height=2).place(x=20, y=450)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=520)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=520)

        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.save(
            self.name.get(),
            self.family.get(),
            self.user_name.get(),
            self.password.get(),
            self.phone_number.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.edit(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.user_name.get(),
            self.password.get(),
            self.phone_number.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.delete(
            self.code.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, customer_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)

            for customer in customer_list:
                self.table.insert(
                    "",
                    END,
                    values=customer,
                    tags="Locked" if customer[6] else "OK",
                )
        else:
            msg.showerror("Error", "Error getting customers data")

    def reset_form(self) -> None:
        self.code.set(0)
        self.name.set("")
        self.family.set("")
        self.user_name.set("")
        self.password.set("")
        self.phone_number.set("")
        self.locked.set(False)
        customer_controller = CustomerController()
        status, customer_list = customer_controller.find_all()
        self.show_data_on_table(status, customer_list)

    def search_name_family(self, event):
        customer_controller = CustomerController()
        status, customer_list = customer_controller.find_by_name_family(self.search_name.get(),
                                                                        self.search_family.get())
        self.show_data_on_table(status, customer_list)

    def select_customer(self, event):
        customer = Customer(*self.table.item(self.table.focus())["values"])
        self.code.set(customer.code)
        self.name.set(customer.name)
        self.family.set(customer.family)
        self.user_name.set(customer.username)
        self.password.set(customer.password)
        self.phone_number.set(customer.phone_number)
        self.locked.set(bool(customer.locked))
