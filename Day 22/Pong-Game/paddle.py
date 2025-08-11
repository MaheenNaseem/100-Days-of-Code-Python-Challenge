from turtle import Turtle

UP_LIMIT = 280
DOWN_lIMIT = -280

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.positions = positions
        self.shapesize(5, 1)
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(self.positions)

    def up(self):
        new_y = self.ycor() + 20
        if new_y < UP_LIMIT:
            self.goto(x = self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > DOWN_lIMIT:
            self.goto(x=self.xcor(), y=new_y)
