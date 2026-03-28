from turtle import Turtle, Screen
import random

carrera_en_curso = False
screen = Screen()
screen.setup(width=500, height=400)
apuesta_usuario = screen.textinput(title="Haz tu apuesta", prompt="¿Qué tortuga ganará la carrera? Ingresa un color del arcoiris en inglés: ")
colores = ["red", "orange", "yellow", "green", "blue", "purple"]
posicion_y = [-70, -40, -10, 20, 50, 80]
tortugas = []

#Create 6 turtles
for turtle_index in range(0, 6):
    nueva_tortuga = Turtle(shape="turtle")
    nueva_tortuga.penup()
    nueva_tortuga.color(colores[turtle_index])
    nueva_tortuga.goto(x=-230, y=posicion_y[turtle_index])
    tortugas.append(nueva_tortuga)

if apuesta_usuario:
    carrera_en_curso = True

while carrera_en_curso:
    for turtle in tortugas:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            carrera_en_curso = False
            color_ganador = turtle.pencolor()
            if color_ganador == apuesta_usuario:
                print(f"¡Ganaste! La tortuga {color_ganador} es la ganadora!")
            else:
                print(f"¡Perdiste! La tortuga {color_ganador} es la ganadora!")

        #Make each turtle move a random amount.
        distancia_random = random.randint(0, 10)
        turtle.forward(distancia_random)

screen.exitonclick()
