from tkinter import *
import random, pyperclip
from tkinter import messagebox
EMAIL = "maheen.naseem@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # removes previous entry
    pass_entry.delete(0, END)

    # select a random char, symbol, number from each list
    nr_letters=[random.choice(letters) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    # merges the above three lists
    password_list = nr_letters + nr_symbols + nr_numbers

    # shuffles the lists elements
    random.shuffle(password_list)
    # turn it into a string
    password = "".join(password_list)

    # display the password
    pass_entry.insert(END, password)
    # copies the password for pasting to website
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():

    # retrieves the entry values
    web = web_entry.get()
    password = pass_entry.get()

    # checks if entry is empty then show message box else proceed
    if web == "" or password == "":
        messagebox.showinfo(title="Empty Field/s", message = "Fields can not be empty.")

    else:
        # asks user to check the details
        answer = messagebox.askokcancel(title = web,message = f"Details:\nEmail: {EMAIL}\nPassword:{password}\n"
                                                     f"Is this the information you want to save?")

        # if user clicks 'ok' then we proceed to save the data to the file
        if answer:
            with open("Data.txt", mode = "a") as file:
                text = f"{web} | {EMAIL} | {password}\n"
                file.write(text)
                messagebox.showinfo(title="Saved", message="Data Saved Successfully.")

            # clear the entries for new input and put focus on the first field
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

            web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)


# inserts lock image on screen
canvas = Canvas(width=200, height=200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = img)
canvas.grid(column=1,row = 0)

# LABELS
web_label = Label(text="Website:")
web_label.grid(column = 0, row =1)
email_label = Label(text="Email/Username:")
email_label.grid(column = 0, row =2 )
pass_label = Label(text="Password:")
pass_label.grid(column = 0, row =3)

# ENTRIES
web_entry = Entry(width = 45)
web_entry.focus()
# using sticky to align the entry box
web_entry.grid(column = 1, row =1, columnspan = 2 ,sticky = "w")
email_entry = Entry(width = 45)
email_entry.grid(column = 1, row =2, columnspan= 2,sticky = "w")
email_entry.insert(index=0, string = EMAIL)
pass_entry = Entry(width = 33)
pass_entry.grid(column =1, row = 3, sticky = "w")

# BUTTONS
generate_btn = Button(text = "Generate", command = generate)
generate_btn.grid(column = 2, row =3 , sticky = "w")

add_btn = Button(text = "Add", width= 38, command=save_pass)
add_btn.grid(row = 4,column = 1, columnspan = 2, sticky = "w")

window.mainloop()