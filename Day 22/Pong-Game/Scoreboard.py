from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.right(90)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.draw_partition()
        self.goto(50, 240)
        self.write(self.r_score, False, "center", ("Fixedsys", 30, "bold"))
        self.goto(-50, 240)
        self.write(self.l_score, False, "center", ("Fixedsys", 30, "bold"))

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def draw_partition(self):
        self.goto(0,230)
        self.width(5)
        self.color("white")

        for dash in range(0,12):
            self.penup()
            self.fd(20)
            self.pendown()
            self.fd(20)
            self.penup()