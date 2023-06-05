from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.carSpeedlist = STARTING_MOVE_DISTANCE

    def createCar(self):

        randomChance = random.randint(1, 10)
        if randomChance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=0.6, stretch_len=1.8)
            car.penup()
            car.color(random.choice(COLORS))
            randomYpos = random.randint(-250, 250)
            car.goto(300, randomYpos)
            self.cars.append(car)

    def moveCars(self):

        for car in self.cars:
            car.backward(self.carSpeedlist)

    def carSpeed(self):

        self.carSpeedlist += MOVE_INCREMENT








