from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(0)


#for Scoreboard
score = Scoreboard()

#for Paddle
r_paddle =Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#for spawning ball on screen
ball = Ball()

screen.listen()

#keys for right paddle
screen.onkey(fun = r_paddle.up, key = "Up")
screen.onkey(fun= r_paddle.down, key = "Down")

#key functions for left paddle.
screen.onkey(fun = l_paddle.up, key = "w")
screen.onkey(fun= l_paddle.down, key = "s")

game_over = False
while not game_over:
    time.sleep(ball.starting_sleep)
    screen.update()
    ball.moving()

    #detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    #ball.xcor > 320 cause thats the meeting point for ball and paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.increase_speed()

    #detect when right paddle misses
    if ball.xcor() > 380 :
        ball.restart()
        score.update_l_score()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.restart()
        score.update_r_score()

screen.exitonclick()