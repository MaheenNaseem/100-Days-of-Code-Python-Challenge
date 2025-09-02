from tkinter import *

#sets the window
window = Tk()
window.minsize(500, 500)
window.title("Widget Examples")

# Creating Label on screen
top_Label = Label(text = "This is new text")
top_Label.pack()

#this will run when click me button is clicked
def button_clicked():
    print("Do Something")

# Creating Button
click_me_btn = Button(text = "Click Me", command= button_clicked)
click_me_btn.pack()

# Creating an Entry
entry_1 = Entry(width=25)

# we provide it the
entry_1.insert(index=0 , string= "Some Text to begin with")
print(entry_1.get())
entry_1.pack()

# Create a Textbox
tb_1 = Text(height= 5, width= 30)
tb_1.focus()
tb_1.insert(END, "Example of multi_line text entry.")

# retrieves the whole text on the index line 1, index 0 till the end
print(tb_1.get(1.0,END))
tb_1.pack()

# Create a Spin box

# prints spinbox value
def spinbox_input():
    print(spinbox.get())

# we provide starting and ending value to the spinbox
spinbox = Spinbox(from_=0, to= 10 ,width= 5,command=spinbox_input)
spinbox.pack()

# Create a Scale

# command in scale returns the value where scale stands at, we take that value and prints it
def scale_input(value):
    print(value)

scale = Scale(from_=0, to=100, command= scale_input)
scale.pack()

# Creating Checkbutton

def checkbutton_input():

    # check_state.get() will return 1 if the box is checked, 0 if unchecked
    print(check_state.get())

# we initialize the value for the checkbutton whether its clicked or not (0,1)
check_state = IntVar()

# - "variable" = link the box to our IntVar so we can read its state
# - "command" = the function to run whenever the user clicks it
check_btn = Checkbutton(text="Is On?",variable=check_state, command= checkbutton_input)
check_btn.pack()

#Creating RadioButton

def radio_input():
    # display selected radiobutton value
    print(radio_state.get())

radio_state = IntVar()
 # value = the number assigned if this button is selected
# variable = connects the button to radio_state
# command = runs radio_input whenever this button is clicked

Radio_btn1 = Radiobutton(text= "Option 1", value=1, variable= radio_state,command= radio_input)
Radio_btn1.pack()
Radio_btn2 = Radiobutton(text= "Option 2", value=2,variable= radio_state,command= radio_input)
Radio_btn2.pack()

# Create Listbox

def listbox_input(event):
    # Get the index (position) of the selected item, e.g. (2,)
    # Then use that index to fetch the actual text, e.g. "Mango"
    print(listbox.get(listbox.curselection()))

fruits = ['Apple', 'Pear', 'Mango','Plum']
listbox = Listbox(height = 4)
# adds the fruits in the list box
for item in fruits:
    listbox.insert(END,item)

# Connect the Listbox to the function.
# "<<ListboxSelect>>" means "run this function when an item is clicked/selected"
listbox.bind("<<ListboxSelect>>", listbox_input)
listbox.pack()


window.mainloop()