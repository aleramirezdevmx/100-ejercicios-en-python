from turtle import Turtle, Screen
from Tortuga import *


cuadrado(100)
punteada()

for figura_lado_n in range(3,11):
    figura(figura_lado_n)

aleatorio()

screen = Screen()
screen.exitonclick()