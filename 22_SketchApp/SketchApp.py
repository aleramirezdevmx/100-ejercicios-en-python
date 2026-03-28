from turtle import Turtle, Screen

dibujo = Turtle()
screen=Screen()

def enfrente():
    dibujo.forward(10)

def atras():
    dibujo.backward(10)

def izquierda():
    nuevo=dibujo.heading()+10
    dibujo.setheading(nuevo)

def derecha():
    nuevo=dibujo.heading()-10
    dibujo.setheading(nuevo)

def limpiar():
    dibujo.clear()
    dibujo.penup()
    dibujo.home()
    dibujo.pendown()

screen.listen()
screen.onkey(enfrente,"w")
screen.onkey(atras, "s")
screen.onkey(izquierda, "a")
screen.onkey(derecha,"d")
screen.onkey(limpiar,"c")
screen.exitonclick()