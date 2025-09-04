import math
from tkinter import *

# CONSTANTS
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
DULL_GREEN = "#347928"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# TIMER RESET

def reset():

    # canceling the previous after that calls the countdown
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text = "Timer", fg = DULL_GREEN)
    checkmark_label.config(text ="")

    # setting Reps to 0 would start the countdown from the start
    global REPS
    REPS = 0

# TIMER MECHANISM

def start_countdown():
    global REPS
    # updating rep for the first rep
    REPS += 1

    # minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # checks and prints the checkmarks according to the reps (1 check on 2 reps)
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text ="Break", fg = RED)
    elif REPS % 2 ==0:
        countdown(short_break_sec)
        timer_label.config(text ="Break",fg = PINK)
    else:
        timer_label.config(text = "Work",fg= DULL_GREEN)
        countdown(work_sec)

# COUNTDOWN MECHANISM
def countdown(count):

    # for counting minutes remaining
    count_min = math.floor(count/60)
    # for counting seconds left
    count_sec = count % 60

    # checks if the sec are less than 10 then it will show ":00" on screen
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # this edits the canva's text 
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}", fill = "white", font = (FONT_NAME, 30, "bold"))

    # if there’s still time left, schedule another countdown call after 1 second
    if count > 0:
        global TIMER
        # window.after() calls countdown(count-1) after 1000 ms (1 second)
        TIMER = window.after(1000, countdown, count-1)

    else:
        # when one sessio end calls the new countdown based in the rep
        start_countdown()
        
        checkmark = ""
        session = REPS / 2
        # places one check mark after 2 sessions
        for check in range(int(session)):
              checkmark += "✔"
        checkmark_label.config(text= checkmark)

# UI SETUP
window = Tk()
window.title("Pomodoro")
# padding
window.config(padx = 100, pady= 50, bg = YELLOW)

#setting the canvas
canvas = Canvas(width = 200, height= 224, bg = YELLOW, highlightthickness= 0 )

# defining the file path
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = img )

# timer text
timer_text = canvas.create_text(100, 134, text = "00:00", fill = "white", font = (FONT_NAME, 30, "bold"))
canvas.grid(column= 2, row=2)

# LABELS
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg= DULL_GREEN, bg = YELLOW)
timer_label.grid(column=2, row=1)

checkmark_label = Label(text= " ", fg = DULL_GREEN,bg=YELLOW, font="bold")
checkmark_label.grid(column=2, row=4)

# BUTTONS

# for starting the timer
start_btn = Button(text = "Start", command= start_countdown ,bg = GREEN, activeforeground= "white", activebackground= DULL_GREEN,font=(FONT_NAME, 13, "bold"))
start_btn.grid(column=1, row=3)

# for resetting the timer
reset_btn = Button(text = "Reset",command = reset ,bg = GREEN, activeforeground= "white", activebackground= DULL_GREEN, font=(FONT_NAME, 13, "bold"))
reset_btn.grid(column=3, row=3)

window.mainloop()
