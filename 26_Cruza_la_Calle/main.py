import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player=Player()
car_manager=CarManager()
nivel=Scoreboard()

screen.listen()
screen.onkey(player.mover,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.crear_carro()
    car_manager.mover_carro()

    for car in car_manager.carros:
        if car.distance(player)<20:
            game_is_on=False
            nivel.perder()
    
    if player.exito():
        player.inicio()
        car_manager.nivel()
        nivel.incrementar_nivel()



screen.exitonclick()
