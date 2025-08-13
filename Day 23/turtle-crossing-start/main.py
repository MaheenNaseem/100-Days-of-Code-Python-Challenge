import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

#initlize score board class
scoreboard = Scoreboard()

#initializing player class
player = Player()

#initializing car manager class
car_manager = CarManager()
screen.update()

#listen to user
screen.listen()

#bounding keys with functions from player class
screen.onkey(fun = player.move_up, key= "Up")
screen.onkey(fun = player.move_down, key = "Down")
screen.onkey(fun = player.move_left, key = "Left")
screen.onkey(fun = player.move_right, key = "Right")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    #generates cars
    car_manager.generating_cars()

    #moves cars
    car_manager.moving_x()

    #detecting collision with car
    for cars in car_manager.cars_list:
        if cars.distance(player) < 20 :
            scoreboard.game_over()
            screen.update()
            time.sleep(2)
            game_is_on = False

    # detect if player reached the finish line
    if player.check_reached():
        scoreboard.update_level()

        #if the level is 4 then print game end (this would make the game only 3 levels long)
        if scoreboard.level == 4:
            scoreboard.game_end()

            #shows the text over the screen
            screen.update()

            # freezes the screen
            time.sleep(3)

            #ends the loop
            game_is_on = False

        else:
            scoreboard.new_level()

            #sends turtle back to initial position
            player.reset_position()

            #Increases the cars movement
            car_manager.increase_speed()

screen.exitonclick()
