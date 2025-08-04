import turtle
from turtle import Turtle, Screen, mode
import random

turtle.colormode(255)
tim = Turtle()

#colors extracted from the picture using color gram
colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213),(168, 106, 57),(186, 158, 53),(6, 57, 83),(109, 67, 85),
          (113, 161, 175),(22, 122, 174),(64, 153, 138),(39, 36, 36),(76, 40, 48),(9, 67, 47),(90, 141, 53),
          (181, 96, 79),(132, 40, 42),(210, 200, 151),(141, 171, 155),(179, 201, 186),(172, 153, 159),(212, 183, 177),
          (176, 198, 203)]

tim.hideturtle()
tim.penup()
tim.teleport(-250, -200)
tim.setheading(0)

dot_counter = 100

for dots in range(1, dot_counter+1):
    tim.speed("fastest")
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dots % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
