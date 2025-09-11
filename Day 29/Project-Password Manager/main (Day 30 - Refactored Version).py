from tkinter import *
import random, pyperclip, json
from tkinter import messagebox
from tkinter.ttk import Combobox

DATA_FILE = "Data.json"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- FETCHING LIST ------------------------------- #

# For refreshing the website names from the json file
def refresh_combobox():
    web_list = []
    try:
        with open(DATA_FILE, mode = "r") as passwords:
            content = json.load(passwords)
            for web in content:
                web_list.append(web.capitalize())
              
    except(FileNotFoundError, json.JSONDecodeError):
        web_list = []
      
    return web_list

# ---------------------------- FETCHING RESULTS ------------------------------- #

def search():
    # prevents data duplication
    web = web_combo.get().strip().lower()

    # checks if entry is empty then show message box else proceed
    if web == "":
        messagebox.showinfo(title="Empty Field/s", message="Fields can not be empty.")

    else:
        try:
            #open data json file and read it
            with open(DATA_FILE, mode = "r") as file:
                data = json.load(file)

            #if file does not exist then show error message
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror(title = "Error", message= "No saved data found")

            # if file exists then show the email password to user
        else:
            if web in data:
                email = data[web]["email"]
                password = data[web]["password"]

                # ask if user wants to copy the password
                answer = messagebox.askquestion(title = web.capitalize() , message = f"Email: {email}\nPassword: {password}\n\nDo you want to copy this?" )

                if answer == "yes":
                    pyperclip.copy(password)
                    messagebox.showinfo(title = "Password Copied", message= "Password Copied")

            # if website is not saved in file show warning
            else:
                messagebox.showwarning(title= "Password Not Found", message= f"No saved password was found for {web.capitalize()}.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():

    # removes previous entry
    pass_entry.delete(0, END)

    # select a random char, symbol, number from each list
    nr_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]

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
    # using strip to remove any white spaces and lower to lowercase the website name
    # prevents data duplication
    web = web_combo.get().strip().lower()
    email = email_entry.get()
    password = pass_entry.get()

    new_data = {
        web: {"email": email, "password": password}
    }

    # checks if entry is empty then show message box else proceed
    if web == "" or password == "":
        messagebox.showinfo(title="Empty Field/s", message="Fields can not be empty.")

    else:
        # asks user to check the details
        answer = messagebox.askokcancel(title=web.capitalize(), message=f"Details:\nEmail: {email}\nPassword: {password}\n\n"
                                                           f"Is this the information you want to save?")

        # if user clicks 'ok' then we proceed to save the data to the file
        if answer:

            try:
                with open(DATA_FILE, mode="r") as file:
                    # we use .load for fetching the data
                    data = json.load(file)

            # we use json.JSONDecodeError to prevent program from crashing if mistake is found in json file.
            except (FileNotFoundError, json.JSONDecodeError):
                # create a file and write the data there
                with open(DATA_FILE, mode = "w") as file:
                    json.dump(new_data, file, indent=4)
                    messagebox.showinfo(title="Saved", message="Data Saved Successfully.")

            else:
                # update the loaded file
                data.update(new_data)

                with open(DATA_FILE, mode="w") as file:
                    # write the updated data in file
                    json.dump(data, file, indent=4)
                    messagebox.showinfo(title="Saved", message="Data Saved Successfully.")

            finally:
                 # clear the entries for new input and put focus on the first field
                web_combo.delete(0, END)
                pass_entry.delete(0, END)
                web_combo.focus()
                 # refreshes the list to update the newly added website
                web_combo["values"] = refresh_combobox()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# inserts lock image on screen
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(85, 100, image=img)
canvas.grid(column=1, row=0)

# LABELS
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# COMBOBOX
website_list = refresh_combobox()

web_combo = Combobox(width=30, values= website_list)
web_combo.focus()
# using sticky to align the widget
web_combo.grid(column=1, row=1, columnspan=2, sticky="w")

# ENTRIES
email_entry = Entry(width=33)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(index=0, string="maheen.naseem@gmail.com")
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky="w")

# BUTTONS
generate_btn = Button(text="Generate", command=generate)
generate_btn.grid(column=2, row=3, sticky="w")

add_btn = Button(text="Add", width=27, command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")

search_btn = Button(text="Search", command=search)
search_btn.grid(column=2, row=1, sticky="w")

window.mainloop()
