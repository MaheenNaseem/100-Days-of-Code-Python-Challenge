from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#f3f1e5"
FONT_COLOR = "#5D4F46"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg = THEME_COLOR)

        self.canvas = Canvas(
            width= 300,
            height = 250,
            highlightthickness= 1,
            highlightbackground= FONT_COLOR,
            bg= "#fcfbf9"
        )
        self.canvas_text = self.canvas.create_text(
            150, 125,
            width = 250,
            fill = FONT_COLOR,
            text ="Quizzler",
            justify= "center",
            font = ("Palatino", 20))
        self.canvas.grid(column = 1, row= 2, columnspan = 2, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}",fg = FONT_COLOR,bg=THEME_COLOR, font = ("Palatino",17))
        self.score_label.grid(row= 1, column = 1, sticky ="w")
        self.q_no_label = Label(
            text=f"Q: {self.quiz.question_number}/{len(self.quiz.question_list)}",
            fg = FONT_COLOR,
            bg=THEME_COLOR,
            font = ("Palatino", 17)
        )
        self.q_no_label.grid(row=1, column =2 , sticky = "e")

        self.tick_img = PhotoImage(file= "images/tick.png")
        self.tick_btn = Button(
            image=self.tick_img,
            borderwidth= 0,
            highlightthickness=0,
            bg = THEME_COLOR,
            activebackground= THEME_COLOR,
            command = self.is_true
        )
        self.tick_btn.grid(column = 1, row=3)

        self.cross_img = PhotoImage(file="images/wrong.png")
        self.cross_btn = Button(
            image=self.cross_img,
            borderwidth=0,
            highlightthickness=0,
            bg = THEME_COLOR,
            activebackground= THEME_COLOR ,
            command=self.is_false
        )
        self.cross_btn.grid(column = 2, row=3)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.button_enabled()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,justify= "center", text = q_text, fill = FONT_COLOR,width = 270)
        else:

            self.canvas.itemconfig(self.canvas_text,justify= "center", text = "You've completed the quiz", fill = FONT_COLOR,width = 270)
            self.button_disabled()


    def is_true(self):
        self.button_disabled()
        answer=self.quiz.check_answer("True")
        self.update()
        self.feedback(answer)

    def is_false(self):
        self.button_disabled()
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.itemconfig(self.canvas_text, text="You got that right", fill = "green",width=270)
        else:
            self.canvas.itemconfig(self.canvas_text, text="That was incorrect", fill = "red" ,width=270)

        self.window.after(ms=1000, func=self.get_next_question)

    def update(self):
        self.score_label.config(text = f"Score: {self.quiz.score}")
        self.q_no_label.config(text = f"Q: {self.quiz.question_number}/{len(self.quiz.question_list)}")

    def button_disabled(self):
        self.tick_btn.config(state = "disabled")
        self.cross_btn.config(state = "disabled")

    def button_enabled(self):
        self.tick_btn.config(state="normal")
        self.cross_btn.config(state="normal")