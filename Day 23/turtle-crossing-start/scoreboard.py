from turtle import Turtle
FONT = ("Fixedsys", 24, "normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.writing_level()

    def writing_level(self):
        """Prints the Level on the screen's top-left corner"""
        self.goto(-220, 255)
        self.color("white")
        self.write(f"Level: {self.level}",False,"center",FONT)

    def game_over(self):
        """Display Game Over on the screen"""
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", font = ("Fixedsys", 27, "bold"))

    def update_level(self):
        """Updates the game's level by one"""
        self.level += 1

    def new_level(self):
        """write new level on the screen"""
        self.clear()
        self.writing_level()

    def game_end(self):
        """Displays Ending message on screen"""
        self.goto(0,0)
        self.write(arg ="YOU WON",move= False ,align="center", font= ("Fixedsys", 24, "bold"))
        self.goto(20,-40)
        self.write(arg ="The turtle is back at home!",move= False , align="center", font = ("Fixedsys", 20, "normal") )

