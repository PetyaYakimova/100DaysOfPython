from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
# Padding for the window
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# Padding for a component
my_label.config(padx=10, pady=10)

# Button
my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

# New button
new_button = Button(text="Click Me 2", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

window.mainloop()
