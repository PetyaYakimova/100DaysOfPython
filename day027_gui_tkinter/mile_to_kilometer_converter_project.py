from tkinter import *


def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609)
    km_result_label.config(text=f"{kilometers}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label()
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

my_button = Button(text="Calculate", command=calculate)
my_button.grid(column=1, row=2)

window.mainloop()
