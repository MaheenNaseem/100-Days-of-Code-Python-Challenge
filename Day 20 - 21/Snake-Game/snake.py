from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.x_axis = 0
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for loop to make the body follow the head instead of forwarding individually
        # len(snake_length)-1 gives the last index of the snake_length (2) and end at 0 (first index) and it has to step -1 to decrement

        for snake_body in range(len(self.segments) - 1, 0, -1):

            # it takes the index of the snake_length and - 1 so it gives the index of the segment after the index
            # this happens so that segment 3 moves to where segment 2 was and 2 moves where 1 was
            new_x = self.segments[snake_body - 1].xcor()
            new_y = self.segments[snake_body - 1].ycor()

            self.segments[snake_body].goto(new_x, new_y)
        # it moves the first segment forward to give it new position
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
