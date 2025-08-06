from controller.car_controller import CarController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from model.entity.car import Car


def format_number_with_dots(number):
    try:
        return "{:,.0f}".format(number).replace(',', '.')
    except (ValueError, TypeError):
        return str(number)


class CarView:
    def __init__(self) -> None:
        self.win = Tk()
        self.win.title("Car View")
        self.win.geometry("1000x600")

        #  code
        Label(self.win, text="Code").place(x=20, y=20)
        self.code = IntVar()
        Entry(self.win, textvariable=self.code, width=23, state="readonly").place(x=120, y=20)

        # name
        Label(self.win, text="Name").place(x=20, y=70)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name, width=23).place(x=120, y=70)

        # model
        Label(self.win, text="Model").place(x=20, y=120)
        self.model = StringVar()
        Entry(self.win, textvariable=self.model, width=23).place(x=120, y=120)

        # color
        Label(self.win, text="Color").place(x=20, y=170)
        self.color = StringVar()
        Entry(self.win, textvariable=self.color, width=23).place(x=120, y=170)

        # year
        Label(self.win, text="Year").place(x=20, y=220)
        self.year = StringVar()
        Entry(self.win, textvariable=self.year, width=23).place(x=120, y=220)

        # price
        Label(self.win, text="Price").place(x=20, y=270)
        self.price = StringVar()
        Entry(self.win, textvariable=self.price, width=23).place(x=120, y=270)

        # locked
        Label(self.win, text="Locked").place(x=20, y=320)
        self.locked = BooleanVar()
        Checkbutton(self.win, text="Locked", variable=self.locked).place(x=120, y=320)

        # search
        Label(self.win, text="Search by Name").place(x=300, y=20)
        self.search_name = StringVar()
        self.search_name_txt = Entry(self.win, textvariable=self.search_name, width=23, fg="gray64")
        self.search_name_txt.bind("<KeyRelease>", self.search_name_and_model)
        self.search_name_txt.place(x=420, y=20)

        Label(self.win, text="Search by Model").place(x=550, y=20)
        self.search_model = StringVar()
        self.search_model_txt = Entry(self.win, textvariable=self.search_model, width=23, fg="gray64")
        self.search_model_txt.bind("<KeyRelease>", self.search_name_and_model)
        self.search_model_txt.place(x=670, y=20)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7, ], show="headings")
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Model")
        self.table.heading(4, text="Color")
        self.table.heading(5, text="Year")
        self.table.heading(6, text="Price")
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
        self.table.bind("<ButtonRelease>", self.select_car)
        self.table.place(x=300, y=100, height=460)

        Button(self.win, text="Save", command=self.save_click, width=34, height=2).place(x=20, y=450)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=520)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=520)

        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        car_controller = CarController()
        try:
            year_str = self.year.get()
            price_str = self.price.get()

            year_value = int(year_str) if year_str else 0
            price_value = int(price_str.replace('$', '').replace(',', '').replace('.', '')) if price_str else 0

            status, message = car_controller.save(
                self.name.get(),
                self.model.get(),
                self.color.get(),
                year_value,
                price_value,
                self.locked.get(),
            )
            if status:
                msg.showinfo("Save", message)
                self.reset_form()
            else:
                msg.showerror("Save Error", message)
        except ValueError:
            msg.showerror("Input Error", "Year and Price must be valid numbers.")

    def edit_click(self):
        car_controller = CarController()
        try:
            year_str = self.year.get()
            price_str = self.price.get()

            year_value = int(year_str) if year_str else 0
            price_value = int(price_str.replace('$', '').replace(',', '').replace('.', '')) if price_str else 0

            status, message = car_controller.edit(
                self.code.get(),
                self.name.get(),
                self.model.get(),
                self.color.get(),
                year_value,
                price_value,
                self.locked.get(),
            )
            if status:
                msg.showinfo("Edit", message)
                self.reset_form()
            else:
                msg.showerror("Edit Error", message)
        except ValueError:
            msg.showerror("Input Error", "Year and Price must be valid numbers.")

    def delete_click(self):
        car_controller = CarController()
        status, message = car_controller.delete(
            self.code.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, car_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)

            for car in car_list:
                formatted_car = list(car)

                formatted_car[5] = format_number_with_dots(formatted_car[5])

                self.table.insert(
                    "",
                    END,
                    values=formatted_car,
                    tags="Locked" if car[6] else "OK",
                )
        else:
            msg.showerror("Error", "Error getting cars data")

    def reset_form(self) -> None:
        self.code.set(0)
        self.name.set("")
        self.model.set("")
        self.color.set("")
        self.year.set("")
        self.price.set("")
        self.locked.set(False)
        car_controller = CarController()
        status, car_list = car_controller.find_all()
        self.show_data_on_table(status, car_list)

    def search_name_and_model(self, event):
        car_controller = CarController()
        status, car_list = car_controller.find_by_name_model(self.search_name.get(), self.search_model.get())
        self.show_data_on_table(status, car_list)

    def select_car(self, event):
        selected_item = self.table.focus()
        if not selected_item:
            return

        values = self.table.item(selected_item)["values"]
        car = Car(*values)
        self.code.set(car.code)
        self.name.set(car.name)
        self.model.set(car.model)
        self.color.set(car.color)
        self.year.set(car.year)

        self.price.set(format_number_with_dots(car.price))
        self.locked.set(bool(car.locked))