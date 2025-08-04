import turtle
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Green")

#Challenge 5: Generate random colors using tuple

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r,g,b)
    return color

#Challenge 2: Make a Dashed line

# for move in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#Challenge 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, and decagon by moving the turtle

# def drawing_shape(shapes_angle, shapes_side):
#     for moving in range(shapes_side):
#         tim.right(shapes_angle)
#         tim.forward(100)
#         if moving == shapes_side:
#             break
#
# for shapes in range(3,11):
#     angle = 360 / shapes
#
#     tim.color(random.color())
#     drawing_shape(angle,shapes)

#Challenge 4: Draw a random walk

# tim.hideturtle()
#
# def move_randomly():
#     directions = [0, 90, 180, 270]
#
#     tim.pensize(15)
#     tim.speed(100)
#
#     for _ in range(200):
#         tim.color(random_color())
#         tim.setheading(random.choice(directions))
#         tim.forward(30)
#
# for i in range(100):
#     move_randomly()

#Challenge 5: Make a Spirograph

#tim.hideturtle()

def draw_spirograph(gap_between_circles):

    for i in range(int(360/gap_between_circles)): #range = 360/5 = 72
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading()+gap_between_circles)

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()

