from turtle import Turtle, Screen
import random

screen = Screen()

#sets dimensions of the screen
screen.setup(width = 500, height= 400)

is_race_on = False

#takes user input via pop up
user_bet = screen.textinput(title= "Make your Bet", prompt= "Which Turtle will win the race. Enter a color").lower()

color = ["Purple","Orange","Green","Brown","Blue","Red"]

#checks if user's choice is in string
#checks if user's color is in list of not
while not user_bet.isalpha()  or user_bet.capitalize() not in color:
    statement = f"Invalid Input. Choose from the following {color}"
    user_bet = screen.textinput(title="Make your Bet", prompt=statement).lower()

turtles =[]

#initial y coordinate
y = -150

for turtle_index in range(0,6):
    #generates turtle objects
    new_turtle = Turtle(shape="turtle")

    #sets turtles color from color list
    new_turtle.color(color[turtle_index])

    #adds turtle object in the turtles list
    turtles.append(new_turtle)

    new_turtle.penup()

    #set turtle on the given coordinates
    new_turtle.goto(-230, y)

    #increases y coordinate for the next turtle to prevent overlapping
    y += 50

if user_bet :
    is_race_on = True

while is_race_on:
    for turtle in turtles:

        #checks if turtle has reached the end of the race
        if turtle.xcor() < 230:
            #if < target then continue to race
            pace = random.randint(0, 10)
            turtle.forward(pace)

        else:
            #if reached target then winning color is set to the turtle that won
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You've Won! {winning_color.capitalize()} turtle is the winner!")

            else:
                print(f"You've Lost! {winning_color.capitalize()} turtle is the winner!")

            is_race_on = False

            break
screen.bye()
