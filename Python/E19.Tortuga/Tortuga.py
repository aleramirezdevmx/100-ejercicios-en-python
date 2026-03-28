from turtle import Turtle
import random

tortuga=Turtle()
tortuga2=Turtle()
tortuga3=Turtle()
tortuga4=Turtle()

direccion=[0,90,180,270]

def cuadrado(size):
    tortuga.shape("turtle")
    tortuga.color("red")
    for _ in range(4):
        tortuga.forward(size)
        tortuga.left(90)
    
def punteada():
    tortuga2.shape("turtle")
    tortuga2.color("green")
    for _ in range(15):
        tortuga2.forward(10)
        tortuga2.penup()
        tortuga2.forward(10)
        tortuga2.pendown()
    
def figura(num_lados):
    tortuga3.shape("turtle")
    tortuga3.color("blue")
    angulo=360/num_lados
    for _ in range(num_lados):
        tortuga3.forward(100)
        tortuga3.right(angulo)  

def aleatorio():
    tortuga4.shape("turtle")
    for _ in range (20):
        tortuga4.setheading(random.choice(direccion))
        tortuga4.forward(30)
        tortuga4.pensize(15)

        