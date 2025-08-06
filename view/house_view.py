from controller.house_controller import HouseController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from model.entity.house import House


def format_number_with_dots(number):
    try:
        return "{:,.0f}".format(number).replace(',', '.')
    except (ValueError, TypeError):
        return str(number)


class HouseView:
    def __init__(self):
        self.win = Tk()
        self.win.title("House View")
        self.win.geometry("1000x600")

        #  code
        Label(self.win, text="Code").place(x=20, y=20)
        self.code = IntVar()
        Entry(self.win, textvariable=self.code, width=23, state="readonly").place(x=120, y=20)

        # region
        Label(self.win, text="Region").place(x=20, y=70)
        self.region = StringVar()
        Entry(self.win, textvariable=self.region, width=23).place(x=120, y=70)

        # address
        Label(self.win, text="Address").place(x=20, y=120)
        self.address = StringVar()
        Entry(self.win, textvariable=self.address, width=23).place(x=120, y=120)

        # floor
        Label(self.win, text="Floor").place(x=20, y=170)
        self.floor = StringVar()
        Entry(self.win, textvariable=self.floor, width=23).place(x=120, y=170)

        # area
        Label(self.win, text="Area").place(x=20, y=220)
        self.area = StringVar()
        Entry(self.win, textvariable=self.area, width=23).place(x=120, y=220)

        # rooms
        Label(self.win, text="Rooms").place(x=20, y=270)
        self.rooms = StringVar()
        Entry(self.win, textvariable=self.rooms, width=23).place(x=120, y=270)

        # year
        Label(self.win, text="Year").place(x=20, y=320)
        self.year = StringVar()
        Entry(self.win, textvariable=self.year, width=23).place(x=120, y=320)

        # price
        Label(self.win, text="Price").place(x=20, y=370)
        self.price = StringVar()
        Entry(self.win, textvariable=self.price, width=23).place(x=120, y=370)

        # elevator
        Label(self.win, text="Elevator").place(x=20, y=420)
        self.elevator = BooleanVar()
        Checkbutton(self.win, text="Elevator", variable=self.elevator).place(x=120, y=420)

        # parking
        Label(self.win, text="Parking").place(x=20, y=470)
        self.parking = BooleanVar()
        Checkbutton(self.win, text="Parking", variable=self.parking).place(x=120, y=470)

        # storage
        Label(self.win, text="Storage").place(x=20, y=520)
        self.storage = BooleanVar()
        Checkbutton(self.win, text="Storage", variable=self.storage).place(x=120, y=520)

        # locked
        Label(self.win, text="Locked").place(x=20, y=570)
        self.locked = BooleanVar()
        Checkbutton(self.win, text="Locked", variable=self.locked).place(x=120, y=570)

        # search
        Label(self.win, text="Search by Region").place(x=300, y=20)
        self.search_region = StringVar()
        self.search_region_txt = Entry(self.win, textvariable=self.search_region, width=23, fg="gray64")
        self.search_region_txt.bind("<KeyRelease>", self.search_region_price)
        self.search_region_txt.place(x=420, y=20)

        Label(self.win, text="Search by Price").place(x=550, y=20)
        self.search_price = StringVar()
        self.search_price_txt = Entry(self.win, textvariable=self.search_price, width=23, fg="gray64")
        self.search_price_txt.bind("<KeyRelease>", self.search_region_price)
        self.search_price_txt.place(x=670, y=20)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], show="headings")
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Region")
        self.table.heading(3, text="Address")
        self.table.heading(4, text="Floor")
        self.table.heading(5, text="Area")
        self.table.heading(6, text="Rooms")
        self.table.heading(7, text="Elevator")
        self.table.heading(8, text="Parking")
        self.table.heading(9, text="Storage")
        self.table.heading(10, text="Year")
        self.table.heading(11, text="Price")
        self.table.heading(12, text="Locked")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)
        self.table.column(9, width=100)
        self.table.column(10, width=100)
        self.table.column(11, width=100)
        self.table.column(12, width=60)

        self.table.tag_configure("OK", background="lightgreen")
        self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_house)
        self.table.place(x=300, y=100, height=460)

        Button(self.win, text="Save", command=self.save_click, width=34, height=2).place(x=20, y=600)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=670)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=670)

        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        house_controller = HouseController()
        try:
            floor_value = int(self.floor.get()) if self.floor.get() else 0
            area_value = int(self.area.get()) if self.area.get() else 0
            rooms_value = int(self.rooms.get()) if self.rooms.get() else 0
            year_value = int(self.year.get()) if self.year.get() else 0

            price_str = self.price.get()
            price_value = int(price_str.replace('$', '').replace(',', '').replace('.', '')) if price_str else 0

            status, message = house_controller.save(
                self.region.get(),
                self.address.get(),
                floor_value,
                area_value,
                rooms_value,
                self.elevator.get(),
                self.parking.get(),
                self.storage.get(),
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
            msg.showerror("Input Error", "All numeric fields must contain valid numbers.")

    def edit_click(self):
        house_controller = HouseController()
        try:
            floor_value = int(self.floor.get()) if self.floor.get() else 0
            area_value = int(self.area.get()) if self.area.get() else 0
            rooms_value = int(self.rooms.get()) if self.rooms.get() else 0
            year_value = int(self.year.get()) if self.year.get() else 0

            price_str = self.price.get()
            price_value = int(price_str.replace('$', '').replace(',', '').replace('.', '')) if price_str else 0

            status, message = house_controller.edit(
                self.code.get(),
                self.region.get(),
                self.address.get(),
                floor_value,
                area_value,
                rooms_value,
                self.elevator.get(),
                self.parking.get(),
                self.storage.get(),
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
            msg.showerror("Input Error", "All numeric fields must contain valid numbers.")

    def delete_click(self):
        house_controller = HouseController()
        status, message = house_controller.delete(
            self.code.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, house_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)

            for house in house_list:
                formatted_house = list(house)
                formatted_house[10] = format_number_with_dots(formatted_house[10])

                self.table.insert(
                    "",
                    END,
                    values=formatted_house,
                    tags="Locked" if house[11] else "OK",
                )
        else:
            msg.showerror("Error", "Error getting houses data")

    def reset_form(self):
        self.code.set(0)
        self.region.set("")
        self.address.set("")
        self.floor.set("")
        self.area.set("")
        self.rooms.set("")
        self.elevator.set(False)
        self.parking.set(False)
        self.storage.set(False)
        self.year.set("")
        self.price.set("")
        self.locked.set(False)
        house_controller = HouseController()
        status, house_list = house_controller.find_all()
        self.show_data_on_table(status, house_list)

    def search_region_price(self, event):
        house_controller = HouseController()
        region_value = self.search_region.get()
        price_str = self.search_price.get()

        if not region_value and not price_str:
            status, house_list = house_controller.find_all()
        else:
            try:
                price_value = int(price_str.replace('$', '').replace(',', '').replace('.', '')) if price_str else 0
                status, house_list = house_controller.find_by_region_price(region_value, price_value)
            except ValueError:
                msg.showerror("Input Error", "Price must be a valid number for search.")
                return

        self.show_data_on_table(status, house_list)

    def select_house(self, event):
        selected_item = self.table.focus()
        if not selected_item:
            return

        values = self.table.item(selected_item)["values"]


        self.code.set(values[0])
        self.region.set(values[1])
        self.address.set(values[2])
        self.floor.set(values[3])
        self.area.set(values[4])
        self.rooms.set(values[5])


        self.elevator.set(bool(values[6]))
        self.parking.set(bool(values[7]))
        self.storage.set(bool(values[8]))

        self.year.set(values[9])
        self.price.set(values[10])
        self.locked.set(bool(values[11]))