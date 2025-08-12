from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()

    def generating_cars(self):
        """Generates cars on screen randomly"""

        # for slowing down the generation process
        random_generation = random.randint(1,6)
        if random_generation == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            self.cars_list.append(car)
            #to prevent turtle colliding with the cars as soon as new game stars
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)


    def moving_x(self):
        """Moves the cars by 5 paces on screen"""
        for each_car in self.cars_list:
            each_car.bk(self.car_speed)

    def increase_speed(self):
        """Increase cars movement speed"""
        self.car_speed += MOVE_INCREMENT
        #to increase cars generating
        self.generating_cars()