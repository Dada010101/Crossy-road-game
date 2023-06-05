import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createCar()
    car.moveCars()
    for x in car.cars:
        if x.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finishLine():
        player.goToStart()
        scoreboard.increase_score()
        car.carSpeed()

screen.exitonclick()


