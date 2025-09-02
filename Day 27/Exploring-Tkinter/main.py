import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(500,300)
window.config(padx = 10, pady = 10)

# Creating Label
my_label = tkinter.Label(text = "I am a Label", font = ["Arial",24, "bold"])

# Showing the label on the screen

# .pack() : Automatically lay and center it on the screen
# my_label.pack(side = "top", expand = 0)

# .place(): Provides precise position for the widget using x and y
# my_label.place(x =100, y= 200)

# .grid(): works on column and row 
my_label.config(text = "New Text")
my_label.grid(column = 0, row=0 )

# Creating Button

def button_clicked():
    in_data = entry.get()
    my_label.config(text = in_data)

button = tkinter.Button(text = "Click Me", command = button_clicked)
button.grid(column=1, row=1)

btn_2 = tkinter.Button(text="New arrival")
btn_2.grid(column=2, row=0)

# Entry - input field
entry = tkinter.Entry( width = 20)
entry.config(justify="center")
entry.grid(column=4, row=3)
window.mainloop()

