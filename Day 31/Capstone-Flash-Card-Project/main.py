from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

vocab_count = 100
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words-to-learn.csv")
except (FileNotFoundError,pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/turkish_words - Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------- FlIPPING THE CARDS ----------------------

def flip_card():

    canvas.itemconfig(lang_text, text="English", fill = "white")
    canvas.itemconfig(word_text, text = current_card['English'], fill ="white")
    canvas.itemconfig(front_img, image = bg_img)

    canvas.grid(column=1, row=1, columnspan=2)

# ---------------------- NEXT CARD ----------------------

def next_card():
    global current_card, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)

    known_words = vocab_count - len(to_learn)
    canvas.itemconfig(count, text=f"{known_words}/{vocab_count}")

    if len(to_learn) == 0:
        window.after(ms =2000)
        canvas.delete(word_text)
        canvas.delete(lang_text)
        canvas.create_text(399, 256, text="You've flipped through\n         all the cards!", font=("Berlin Sans FB", 40))

    else:

        current_card = random.choice(to_learn)
        canvas.itemconfig(lang_text, text = "Turkish", fill = "black")
        canvas.itemconfig(word_text, text = current_card['Turkish'], fill ="black")
        canvas.itemconfig(front_img, image=fg_img)
        FLIP_TIMER = window.after(ms = 4000, func=flip_card)

def is_known():
    known_words = vocab_count - len(to_learn)
    canvas.itemconfig(count, text=f"{known_words}/100")
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("words-to-learn.csv", index = False)
    next_card()

# ---------------------- UI SETUP ----------------------

window = Tk()
window.title("Dictionary Vocab Flash Cards")
window.config(bg = BACKGROUND_COLOR, padx = 50, pady= 50)

FLIP_TIMER = window.after(5000, flip_card)

canvas = Canvas(width = 800, height = 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
bg_img = PhotoImage(file = "images/card_back.png")
fg_img = PhotoImage(file = "images/card_front.png")
front_img = canvas.create_image(400,263, image = fg_img)
count = canvas.create_text(400, 400, text="", font=("Berlin Sans FB", 30))
lang_text = canvas.create_text(400, 150, text = "", font= ("Berlin Sans FB", 40, "italic"))
word_text = canvas.create_text(400, 263, text = "",font= ("Berlin Sans FB", 60, "bold"))

canvas.grid(column = 1, row = 1, columnspan = 2)

# BUTTONS
tick_img = PhotoImage(file = "images/right.png")
tick_btn = Button(image=tick_img, highlightthickness= 0, borderwidth=0, command= is_known)
tick_btn.grid(column = 2 , row = 2)

wrong_img = PhotoImage(file = "images/wrong.png")
wrong_btn = Button(image= wrong_img, highlightthickness= 0, borderwidth= 0, command = next_card)
wrong_btn.grid(column = 1, row = 2)

next_card()
window.mainloop()
