import turtle as t
import random

circulo=t.Turtle()
t.colormode(255)

def color_aleatorio():
    r=random.randint(0,255)
    v=random.randint(0,255)
    a=random.randint(0,255)
    color=(r,v,a)
    return color


circulo.speed("fastest")

def dibujar(gap):
    for _ in range(int(360/gap)):
        circulo.color(color_aleatorio())
        circulo.circle(100)
        circulo.setheading(circulo.heading()+gap)

dibujar(5)

screen=t.Screen()
screen.exitonclick()