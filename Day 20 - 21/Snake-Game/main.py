from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()

#sets screen's dimensions
screen.setup(width= 600, height=600)

#sets the background to black
screen.bgcolor("black")
screen.title("Snake Game")

#turns off showing changes on the screen
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()

screen.onkey(fun = snake.up , key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right ,key = "Right")


#move snake body
game_is_on = True
while game_is_on:

    #refreshes the screen and shows the snake altogether instead of showing the segments one by one
    screen.update()

    #to slow down the segment movement
    time.sleep(0.1)
    snake.move()

    #detect collision from food
    if snake.head.distance(food) < 15 :
        food.refresh()
        scores.increase_score()
        snake.extend()

    #detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scores.game_over("wall")
        time.sleep(2)
        scores.reset()
        snake.reset()


    #detecting collision with tail
    #we will slice the snake length to skip the head index
    for segments in snake.segments[1: ]:
        if snake.head.distance(segments) < 10:
            scores.game_over("tail")
            time.sleep(2)
            scores.reset()
            snake.reset()
            food.reset()

screen.exitonclick()