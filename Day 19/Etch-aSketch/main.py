from turtle import Turtle, Screen

tim = Turtle()

my_screen = Screen()

def forwards():
    tim.forward(15)

def backwards():
    tim.back(15)

def turn_right():
    tim.setheading(tim.heading() +10 )

def turn_left():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.reset()

my_screen.listen()

my_screen.onkey(fun = forwards, key= "w")
my_screen.onkey(fun=backwards, key = "s")
my_screen.onkey(fun=turn_right, key="d")
my_screen.onkey(fun=turn_left, key ="a")
my_screen.onkey(fun= clear, key= "c")

my_screen.exitonclick()