from turtle import Turtle, Screen
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Highscore.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0,250)
        self.write(f"Score = {self.score}  HighScore = {self.highscore}", False, "center", ("Fixedsys", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Highscore.txt", mode = "w") as file:
                file.write(str(self.highscore))
        #resets score for next player
        self.score = 0
        self.update_score()

    def game_over(self,collision):
        screen.tracer(0)
        self.screen.bgcolor("black")
        self.goto(0,0)
        self.color("Red")
        self.write(f"\nGAME\nOVER", False, "center", ("Fixedsys", 50, "bold"))
        self.reason(collision)
        self.goto(0,-80)
        self.color("white")
        self.write(f"Your score was: {self.score}", False, "center", ("Fixedsys", 20, "bold"))
        screen.update()

    def reason(self,detection):
        self.goto(0,-40)

        if detection.lower() == "wall":
            self.color("white")
            self.write(f"Snake hit the wall", False, "center", ("Fixedsys", 20, "bold"))

        elif detection.lower() == "tail":
            self.color("white")
            self.write(f"Snake bit itself", False, "center", ("Fixedsys", 20, "bold"))