from tkinter import *


def convert_to_km():
    num = float(entry.get())
    kilo = round(num * 1.609)
    answer.config(text=f"{kilo}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)


window.mainloop()