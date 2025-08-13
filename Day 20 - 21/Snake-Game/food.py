from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len= 0.8, stretch_wid=0.8)
        self.color("red")
        xcor = random.randint(-275,275)
        ycor = random.randint(-275,275)
        self.goto(xcor,ycor)
        self.refresh()

    def refresh(self):
        xcor = random.randint(-275,275)
        ycor = random.randint(-275,275)
        self.goto(xcor, ycor)