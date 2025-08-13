from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Move turtle forwards by 10 paces"""
        self.fd(MOVE_DISTANCE)

    def reset_position(self):
        """Sets turtle to its initial position"""
        self.goto(STARTING_POSITION)

    def move_down(self):
        """Move turtle backwards by 10 paces"""
        self.bk(MOVE_DISTANCE)

    def move_left(self):
        """Move turtle left by 10 paces"""
        self.left(90)
        self.fd(MOVE_DISTANCE)
        self.right(90)

    def move_right(self):
        """Move turtle right by 10 paces"""
        self.right(90)
        self.fd(MOVE_DISTANCE)
        self.left(90)

    def check_reached(self):
        """Check if turtle has reached the finished line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

