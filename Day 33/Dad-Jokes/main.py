from tkinter import *
import requests

def get_joke():
    response = requests.get(url = "https://icanhazdadjo"
                                  "ke.com", headers={"Accept":"application/json"})
    response.raise_for_status()

    data = response.json()

    joke = data["joke"]
    canvas.itemconfig(joke_text, text = joke)

# -------------------- UI SETUP --------------------

window = Tk()
window.title("Dad Jokes")
window.config(padx= 20 , pady= 20)

canvas = Canvas(width = 300 , height =414 )
img= PhotoImage(file = "images/background.png")
canvas.create_image(150, 212, image = img)
joke_text = canvas.create_text(150,200,text="Dad Jokes", width = 250, fill = "black", font= ("Comic Sans MS", 20, "bold"))
canvas.grid(column = 2, row=2)

btn_img = PhotoImage(file = "images/smile.png")
smile_btn = Button(image = btn_img, borderwidth=0, highlightthickness=0, command=get_joke)
smile_btn.grid(column = 2, row=3)

window.mainloop()
