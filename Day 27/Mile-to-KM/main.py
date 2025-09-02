from tkinter import *

window = Tk()
# window.minsize(350, 150)
window.title("Mile to Km Converter")
window.config(padx= 20, pady = 20)

# miles entry
miles_input = Entry(width=12)
miles_input.config(font=("Arial", 12))
miles_input.focus()
miles_input.insert(END, "0")
miles_input.grid(column= 1, row=0)

# miles label
mile_lbl = Label(text="Miles", font =("Arial", 13))
mile_lbl.grid(column= 2,row=0)

# kilometer label
km_lbl = Label(text="Km",font =("Arial", 13))
km_lbl.grid(column=2, row=1)

# result label
result_lbl = Label(text=0,font =("Arial", 13), foreground="dark blue")
result_lbl.grid(column=1, row =1)

# equal to label
equal_lbl = Label(text="is equal to",font =("Arial", 13))
equal_lbl.grid(column=0,row=1)

#conversion function
def convert():
    num = float(miles_input.get())
    kilo_meter = round((num * 1.60934),2)
    result_lbl.config(text= f"{str(kilo_meter)}")

# Calculate button
calculate_btn = Button(text="Calculate", command=convert)
calculate_btn.grid(column=1, row=2)

window.mainloop()