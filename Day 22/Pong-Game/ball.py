from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.x_move = 10
        self.y_move = 10
        self.speed("fast")
        self.starting_sleep = 0.1
        self.moving()


    def moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        #check for ball to move within screen
        self.goto(new_x,new_y)

    # this flips the y cor so if it was 240 it will now go to -240 but with the same x
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.home()
        self.bounce_x()

    def increase_speed(self):
        self.starting_sleep= self.starting_sleep * 0.9
        time.sleep(self.starting_sleep)


